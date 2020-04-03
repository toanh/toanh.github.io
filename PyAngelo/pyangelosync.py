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
        
        #timer.set_interval(self.update, 16)   
        
        # clear to cornflower blue (XNA!) by default        
        self.__clear(0.392,0.584,0.929)
        
        self.pixel_id = self.ctx.createImageData(1, 1)
        self.pixel_color = self.pixel_id.data
        
        self.last_frame_commands = []
        
        self.just_halted = False
        
        self.input_concluded = False
        
        self.input_buffer_index = 0
        
        timer.request_animation_frame(self.update)
        
    def clear(self, r=0, g=0, b=0, a=1):
        kwargs = {"r": r, "g": g, "b": b, "a": a}
        self.commands.append([CMD_CLEAR, kwargs])  

    def drawImage(self, image, x, y, width=None, height=None, rotation=0, anchorX=None, anchorY=None, opacity=1.0,
                  r=1.0, g=1.0, b=1.0, rect=None):
        kwargs = {"image": image, "x": x, "y": y, "width": width, "height": height, "rotation": rotation,
                  "anchorX": anchorX,
                  "anchorY": anchorY, "opacity": opacity, "r": r, "g": g, "b": b, "rect": rect}
        self.commands.append([CMD_DRAWIMAGE, kwargs])    

    def drawRect(self, x1, y1, x2, y2, r = 1.0, g = 1.0, b = 1.0, a = 1.0):           
        kwargs = {"x1":x1, "y1": y1, "x2":x2, "y2": y2, "r": r, "g": g, "b": b, "a": a}
        self.commands.append([CMD_DRAWRECT, kwargs])    

    def drawText(self, text, x, y, fontName = "Arial", fontSize = 10, r = 1.0, g = 1.0, b = 1.0, a = 1.0, anchorX = "left", anchorY ="bottom"):
        kwargs = {"text": text, "x": x, "y": y, "fontName": fontName, "fontSize": fontSize, "r": r, "g": g, "b": b, "a": a, "anchorX": anchorX, "anchorY": anchorY}
        self.commands.append([CMD_DRAWTEXT, kwargs])   

    def drawLine(self, x1, y1, x2, y2, r=1.0, g=1.0, b=1.0, a=1.0, width=1):
        kwargs = {"x1": x1, "y1": y1, "x2": x2, "y2": y2, "r": r, "g": g, "b": b,
                  "a": a, "width": width}
        self.commands.append([CMD_DRAWLINE, kwargs])            

    def isKeyPressed(self, key):
        return self.keys[key]             
        
    def refresh(self):
        self.execute_commands()
    
    ########################################################################################
        
    

    def loadSound(self, filename, streaming = False):
        kwargs = {"filename": filename, "streaming": streaming}
        self.commands.append(["loadSound", kwargs])   
        return filename        

    def playSound(self, sound, loop = False):
        kwargs = {"sound": sound, "loop": loop}
        self.commands.append(["playSound", kwargs])   

    def pauseSound(self, sound):
        kwargs = {"sound": sound}
        self.commands.append(["pauseSound", kwargs])             
        
    def __loadSound(self, filename, streaming = False):
        howl = window.Howl
        sound = howl.new({"src": [filename]})
        self.soundPlayers[filename] = sound
        return filename

    def __playSound(self, sound, loop = False):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].loop = loop
            self.soundPlayers[sound].play()
            
    def __stopAllSounds(self):
        for sound in self.soundPlayers:
            self.__pauseSound(sound)

    def __pauseSound(self, sound):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].pause()        
        
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
                self.__drawText(returned_string + "_", 0, 0)

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

    def __drawImage(self, image, x, y, width = None, height = None, rotation=0, anchorX = None, anchorY = None, opacity=None, r=1.0, g=1.0, b=1.0, rect=None):        
        
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

    def __drawText(self, text, x, y, fontName = "Arial", fontSize = 10, r = 1.0, g = 1.0, b = 1.0, a = 1.0, anchorX = "left", anchorY ="bottom"):
        self.ctx.fillStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0)) + ")"
        self.ctx.font = str(fontSize) + "pt " + fontName
        self.ctx.textBaseline = "bottom"
        self.ctx.fillText(text, x, self.height - y)        

    def __clear(self, r = 0, g = 0, b = 0, a = 1):
        global array
        self.ctx.fillStyle= "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0))+ ")"
        self.ctx.fillRect(0, 0, self.width, self.height)    
        
    def __drawLine(self, x1, y1, x2, y2, r = 1.0, g = 1.0, b = 1.0, a = 1.0, width = 1):
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

    def __drawCircle(self, x, y, radius, r=1.0, g=1.0, b=1.0, a=1.0):
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
        
    def __drawPixel(self, x, y, r = 1.0, g = 1.0, b = 1.0, a = 1.0):
        r = min(r, 1.0)
        g = min(g, 1.0)
        b = min(b, 1.0)
        a = min(a, 1.0)

        self.pixel_color[0] = int(r * 255.0)
        self.pixel_color[1] = int(g * 255.0)
        self.pixel_color[2] = int(b * 255.0)
        self.pixel_color[3] = int(a * 255.0)
        self.ctx.putImageData(self.pixel_id, x, self._convY(y))
        
    def __drawRect(self, x1, y1, x2, y2, r = 1.0, g = 1.0, b = 1.0, a = 1.0):
        r = min(r, 1.0)
        g = min(g, 1.0)
        b = min(b, 1.0)
        a = min(a, 1.0)

        ctx = self.ctx
        ctx.fillStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0)) + ")"        
        ctx.beginPath();
        ctx.moveTo(x1, self._convY(y1))
        ctx.lineTo(x2, self._convY(y1))
        ctx.lineTo(x2, self._convY(y2))
        ctx.lineTo(x1, self._convY(y2))
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
            self.__clear(0.392,0.584,0.929)
        elif self.state == self.STATE_RUN:   
            try:
                self.main_loop()
                self.refresh()
            except Exception as e:
                do_print("Error: " + str(e) + "\n" + traceback.format_exc(), "red")       
                self.stop()
            	   
        elif self.state == self.STATE_INPUT:
            # display the commands in the queue to date
            if self.input_concluded:
                # TODO: if the program halts after the input, then this causes
                # Pyangelo to keep looping in it's run state ===> FIX!
                self.state = self.STATE_RUN
                self.input_concluded = False
        
        timer.request_animation_frame(self.update)
       
    def execute_commands(self, do_frame = True): 
        if len(self.commands) > 0:
            self.last_frame_commands = copy.deepcopy(self.commands)
        
        while len(self.commands) > 0:
            command = self.commands[0]
            
            if command[0] == CMD_DRAWLINE:
                command[0] = self.__drawLine
            elif command[0] == CMD_CLEAR:
                command[0] = self.__clear
            elif command[0] == CMD_DRAWIMAGE:                
                command[0] = self.__drawImage
            elif command[0] == CMD_LOADSOUND:                
                command[0] = self.__loadSound                
            elif command[0] == CMD_PLAYSOUND:                
                command[0] = self.__playSound
            elif command[0] == CMD_PAUSESOUND:                
                command[0] = self.__pauseSound    
            elif command[0] == CMD_DRAWTEXT:                
                command[0] = self.__drawText    
            elif command[0] == CMD_DRAWPIXEL:                
                command[0] = self.__drawPixel   
            elif command[0] == CMD_DRAWRECT:
                command[0] = self.__drawRect
            elif command[0] == CMD_DRAWCIRCLE:
                command[0] = self.__drawCircle
            elif command[0] == CMD_INPUT:
                command[0] = self.__input
            else:
                # not a valid command
                del self.commands[0]
                continue
                
            command[0](**command[1])    

            del self.commands[0]       
        
    def start(self):
        if self.state != self.STATE_RUN:
            self.state = self.STATE_RUN
            self.commands = []
            self.last_frame_commands = []
                        
    def stop(self):   
        if self.state != self.STATE_STOP:
            self.state = self.STATE_STOP            

            # TODO: put all these into a Reset() method
            self.commands = []
            self.resources =  {}
            self.loadingResources = 0

            self.__stopAllSounds()
            
            disable_stop_enable_play()   

    def sleep(self, milliseconds):
        # flush the command buffer to this point
        self.refresh()
        
        # the sleep happens here
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
    graphics.commands = []
    
    run_code(src, namespace, namespace)        
    
def run_code(src, globals, locals):
    #self.console.log("running code...")
    try:
        exec(src , globals, locals)
        graphics.start()
    except Exception as e:
        do_print("Error: " + str(e) + "\n" + traceback.format_exc(), "red") 

            
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
