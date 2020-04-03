import sys
import time
import traceback
import javascript
import random
import json
from browser import document, window, alert, timer, bind, html, load
from browser.local_storage import storage

load("howler.js")

# In web workers, "window" is replaced by "self".
import time
#from browser import bind, self
import sys
import time
import traceback
import javascript
import random
import json
import copy

from browser import bind, self, window

from pyangelo_consts import *

class PyAngeloImage():
    def __init__(self, image):
        self.img = image
        self.height = image.naturalHeight
        self.width = image.naturalWidth

class PyAngelo():
    STATE_STOP      =   1
    STATE_RUN       =   2
    STATE_HALT      =   3
    STATE_LOAD      =   4
    STATE_INPUT     =   5
    
    def __init__(self):
       
        self.commands = []
        
        # get the canvas element
        self.canvas = document["canvas"]
        self.ctx = self.canvas.getContext('2d')		
        
        self.width = self.canvas.width
        self.height = self.canvas.height
        
        self.timer_id = None
        
        self.stopped = False
        
        self.resources =  {}
        self.loadingResources = 0
        
        self.keys = dict([(a, False) for a in range(255)] +
                         [(a, False) for a in range(0xff00, 0xffff)]) 

        document.bind("keydown", self._keydown)
        document.bind("keyup", self._keyup)   

        self.soundPlayers = {}        
        
        self.state = self.STATE_STOP
        self.anim_timer = 0
        self.anim_time = 200        
        
        self.starting_text = "Starting up"   
        self.loading_text = "Loading resources"        
        
        
        # clear to cornflower blue (XNA!) by default        
        self.clear(0.392,0.584,0.929)
        
        self.pixel_id = self.ctx.createImageData(1, 1)
        self.pixel_color = self.pixel_id.data
        
        self.last_frame_commands = []
        
        self.just_halted = False
        
        self.input_concluded = False
        
        self.input_buffer_index = 0
        
        timer.request_animation_frame(self.update)     

    def isKeyPressed(self, key):
        return self.keys[key]             
        
    def refresh(self):
        self.execute_commands()
    
    ########################################################################################
        
    def loadSound(self, filename, streaming = False):
        howl = window.Howl
        sound = howl.new({"src": [filename]})
        self.soundPlayers[filename] = sound
        return filename

    def playSound(self, sound, loop = False):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].loop = loop
            self.soundPlayers[sound].play()
        else:
            self.loadSound(sound)
            self.soundPlayers[sound].loop = loop
            self.soundPlayers[sound].play()            
            
    def stopAllSounds(self):
        for sound in self.soundPlayers:
            self.pauseSound(sound)

    def pauseSound(self, sound):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].pause()       

    # alias for pauseSound
    def stopSound(self, sound):
        self.pauseSound(sound)
        
    def _keydown(self, ev):
       
        self.keys[ev.which] = True
               
        # pressing escape when the program has halted
        if ev.which == KEY_ESC and self.state == self.STATE_HALT:
            self.stop()
            
        # TODO: support stopping during INPUT state
            
        if self.state == self.STATE_INPUT:
            if ev.which != KEY_ENTER and (ev.which < 32 or ev.which > KEY_A + 26):
                return
            array[len(array) - 1 - self.input_buffer_index] = ev.which
            if ev.which == KEY_ENTER:
                self.input_concluded = True
            else:
                returned_string = ""
                n = self.input_buffer_index
                while n >= 0:
                
                    returned_string = chr(array[len(array) - 1 - n]) + returned_string
                    n -= 1
                
                self.input_buffer_index += 1
                self.drawText(returned_string + "_", 0, 0)

    def _keyup(self, ev):
        self.keys[ev.which] = False      
                
    def resourceError(self, e):
        self.stop()
        do_print("Error loading of resource: " + e.target.src + "\n", "red")
        #del e.target
        #e.target.parentElement.removeChild(e.target)
    
    def resourceAbort(self, e):
        self.stop()
        do_print("Aborted loading of resource: " + e.target.src + "\n", "red")  
    
    def resourceLoaded(self, e):
        self.loadingResources -= 1
        
        window.console.log("Successfully loaded file:" + e.target.src);
            
        e.target.jmssImg.height = e.target.naturalHeight
        e.target.jmssImg.width = e.target.naturalWidth        
       
    def loadImage(self, file):
    
        if file in self.resources:
            return self.resources[file]       
        
        self.loadingResources += 1
        
        window.console.log("Attempting to load file:" + file);
        img = html.IMG(src = file)

        img.bind('load', self.resourceLoaded)
        img.bind('error', self.resourceError)
        img.bind('abort', self.resourceAbort)
        
        jmssImg = PyAngeloImage(img)
        img.jmssImg = jmssImg
        
        self.resources[file] = jmssImg
        
        return jmssImg

    def drawImage(self, image, x, y, width = None, height = None, rotation=0, anchorX = None, anchorY = None, opacity=None, r=1.0, g=1.0, b=1.0, rect=None):        
        
        window.console.log("attempting to draw image")
        if (isinstance(image, str)):
            image = self.loadImage(image)
                   
        self.ctx.save()

        if width is None:
            width = image.width

        if height is None:
            height = image.height

        if opacity is not None:
            if opacity > 1.0:
                opacity = 1.0
            elif opacity < 0.0:
                opacity = 0.0
            self.ctx.globalAlpha = opacity

        if rotation != 0.0:
            # TODO: Buggy!!!
            self.ctx.save()
            self.ctx.translate(x, self._convY(y))
            self.ctx.rotate(- rotation)# - 3.1415926535)# + math.PI / 180)
            self.ctx.drawImage(image.img, -anchorX * width, -anchorY * height, width, height)
            self.ctx.restore()
        else:
            self.ctx.drawImage(image.img, x, self._convY(y + height), width, height)


        self.ctx.restore()    

    def drawText(self, text, x, y, fontName = "Arial", fontSize = 10, r = 1.0, g = 1.0, b = 1.0, a = 1.0, anchorX = "left", anchorY ="bottom"):
        self.ctx.fillStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0)) + ")"
        self.ctx.font = str(fontSize) + "pt " + fontName
        self.ctx.textBaseline = "bottom"
        self.ctx.fillText(text, x, self.height - y)        

    def clear(self, r = 0, g = 0, b = 0, a = 1):
        global array
        self.ctx.fillStyle= "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0))+ ")"
        self.ctx.fillRect(0, 0, self.width, self.height)    
        
    def drawLine(self, x1, y1, x2, y2, r = 1.0, g = 1.0, b = 1.0, a = 1.0, width = 1):
        r = min(r, 1.0)
        g = min(g, 1.0)
        b = min(b, 1.0)
        a = min(a, 1.0)

        self.ctx.beginPath()
        self.ctx.lineWidth = width
        self.ctx.strokeStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0)) + ")"
        self.ctx.moveTo(x1, self._convY(y1))
        self.ctx.lineTo(x2, self._convY(y2))
        self.ctx.stroke()

    def drawCircle(self, x, y, radius, r=1.0, g=1.0, b=1.0, a=1.0):
        r = min(r, 1.0)
        g = min(g, 1.0)
        b = min(b, 1.0)
        a = min(a, 1.0)

        self.ctx.fillStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0)) + ")"
        self.ctx.beginPath();
        self.ctx.strokeStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(
            int(b * 255.0)) + "," + str(int(a * 255.0)) + ")"

        self.ctx.arc(x, self._convY(y), radius, 0, 2 * 3.1415926535, True);

        self.ctx.fill();

        self.ctx.stroke()        
        
    def drawPixel(self, x, y, r = 1.0, g = 1.0, b = 1.0, a = 1.0):
        r = min(r, 1.0)
        g = min(g, 1.0)
        b = min(b, 1.0)
        a = min(a, 1.0)

        self.pixel_color[0] = int(r * 255.0)
        self.pixel_color[1] = int(g * 255.0)
        self.pixel_color[2] = int(b * 255.0)
        self.pixel_color[3] = int(a * 255.0)
        self.ctx.putImageData(self.pixel_id, x, self._convY(y))
        
    def drawRect(self, x, y, w, h, r = 1.0, g = 1.0, b = 1.0, a = 1.0):
        r = min(r, 1.0)
        g = min(g, 1.0)
        b = min(b, 1.0)
        a = min(a, 1.0)

        ctx = self.ctx
        ctx.fillStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0)) + ")"        
        ctx.beginPath();
        ctx.moveTo(x, self._convY(y))
        ctx.lineTo(x + w, self._convY(y))
        ctx.lineTo(x + w, self._convY(y + h))
        ctx.lineTo(x, self._convY(y + h))
        ctx.closePath()
        ctx.fill()                  
        
    def _convY(self, y):
        return self.height - y

    def _convColor(self, c):
        return (int(c[0] * 255.0), int(c[1] * 255.0), int(c[2] * 255.0), int(c[3] * 255.0))      

    def __input(self, msg):
        # input mode triggered
        self.state = self.STATE_INPUT
        self.input_concluded = False
        self.input_buffer_index = 0
        
    def loop(self, func):
        self.main_loop = func

        
    def update(self, deltaTime):           
        document["runPlay"].style.cursor = "pointer"
        document["runPause"].style.cursor = "pointer"   
        document["output_runPlay"].style.cursor = "pointer"
        document["output_runPause"].style.cursor = "pointer"          

        if self.state == self.STATE_STOP:       
            self.clear(0.392,0.584,0.929)
        elif self.state == self.STATE_RUN:   
            try:
                self.main_loop()
            except Exception as e:
                do_print("Error: " + str(e) + "\n" + traceback.format_exc(), "red")       
                #self.stop()
            	   
        elif self.state == self.STATE_INPUT:
            # display the commands in the queue to date
            if self.input_concluded:
                # TODO: if the program halts after the input, then this causes
                # Pyangelo to keep looping in it's run state ===> FIX!
                self.state = self.STATE_RUN
                self.input_concluded = False
        
        timer.request_animation_frame(self.update)
       
        
    def start(self):
        if self.state != self.STATE_RUN:
            self.state = self.STATE_RUN
                        
    def stop(self):   
        if self.state != self.STATE_STOP:
            self.state = self.STATE_STOP            

            # TODO: put all these into a Reset() method
            self.resources =  {}
            self.loadingResources = 0

            self.stopAllSounds()
            
            disable_stop_enable_play()   

    def sleep(self, milliseconds):
        # the sleep happens here, it's a tight loop - may hang the browser!
        currTime = window.performance.now()
        prevTime = currTime
        while (currTime - prevTime < milliseconds):
            currTime = window.performance.now()      
            
    def overlaps(self, x1, y1, width1, height1, x2, y2, width2, height2):
        return ((x1 < (x2 + width2)) and ((x1 + width1) > x2) and (y1 < (y2 + height2)) and ((y1 + height1) > y2))            
                              
graphics = PyAngelo()

def format_string_HTML(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>").replace("\"", "&quot;").replace("'", "&apos;").replace(" ", "&nbsp;")

def do_print(s, color=None):
    if color is not None: window.writeOutput("<p style='display:inline;color:" + color + ";'>" + format_string_HTML(s) + "</p>", True)
    else: window.writeOutput("<p style='display:inline;'>" + format_string_HTML(s) + "</p>", True)

def clear_button_run():
    document["runPlay"].style.display = "none"
    document["runPause"].style.display = "none"
    
    for event in document["run"].events("click"):
        document["run"].unbind("click", event)
    document["run"].bind("click", save_code)
    
    document["output_runPlay"].style.display = "none"
    document["output_runPause"].style.display = "none"    
    for event in document["output_run"].events("click"):
        document["output_run"].unbind("click", event)
    document["output_run"].bind("click", save_code)    

def button_play(event):   
    clear_button_run()
    document["runPause"].style.display = "inherit"
    document["run"].bind("click", button_stop)
    document["run"].style.backgroundColor = "#FF0000"; 

    document["output_runPause"].style.display = "inherit"
    document["output_run"].bind("click", button_stop)
    document["output_run"].style.backgroundColor = "#FF0000";     
    do_play()
    
def disable_stop_enable_play():
    clear_button_run()
    document["runPlay"].style.display = "inherit"
    document["run"].bind("click", button_play)    
    document["run"].style.backgroundColor = "#00FF00";   

    document["output_runPlay"].style.display = "inherit"
    document["output_run"].bind("click", button_play)    
    document["output_run"].style.backgroundColor = "#00FF00";       
    
def button_stop(event):
    graphics.stop()
    
def do_play():
    src = window.getCode()
    
    window.console.log(src)

    namespace = globals()
    namespace["__name__"] = "__main__"
    
    
    #pre_globals = list(globals().keys())
    
    run_code(src, namespace, namespace)        
    
    #post_globals = list(globals().keys())

    #for g in post_globals:
    #    if g not in pre_globals:
    #        print(g)
    
def run_code(src, globals, locals):
    #self.console.log("running code...")
    try:
        exec(src , globals, locals)
        graphics.start()
    except Exception as e:
        do_print("Error: " + str(e) + "\n" + traceback.format_exc(), "red") 
        graphics.stop()

            
def save_code(event):
    window.saveCode()      

class ErrorOutput:
    def write(self, data):
        do_print(data, "red") 
    def flush(self):
        pass
        
class PrintOutput:
    def write(self, data):
        do_print(data, "blue") 
    def flush(self):
        pass


sys.stdout = PrintOutput()
sys.stderr = ErrorOutput()    
        
###################################################################################        
