import sys
import time
import traceback
import javascript
import random
import json
from browser import document, window, alert, timer, worker, bind, html, load
from browser.local_storage import storage

load("howler.js")

# Cursor control and motion
KEY_HOME          = 0xff50
KEY_LEFT          = 37
KEY_UP            = 38
KEY_RIGHT         = 39
KEY_DOWN          = 40
KEY_W             = 87
KEY_A             = 65
KEY_S             = 83
KEY_D             = 68
KEY_PAGEUP        = 0xff55
KEY_PAGEDOWN      = 0xff56
KEY_END           = 0xff57
KEY_BEGIN         = 0xff58


# In web workers, "window" is replaced by "self".
import time
#from browser import bind, self
import sys
import time
import traceback
import javascript
import random
import json
from browser import bind, self, window
KEY_ESC           = 27
KEY_HOME          = 0xff50
KEY_LEFT          = 37
KEY_UP            = 38
KEY_RIGHT         = 39
KEY_DOWN          = 40
KEY_PAGEUP        = 0xff55
KEY_PAGEDOWN      = 0xff56
KEY_END           = 0xff57
KEY_BEGIN         = 0xff58

PyAngeloWorker = worker.Worker("executor")

test_buff = None
array = None

class PyAngeloImage():
    def __init__(self, image):
        self.img = image
        self.height = image.naturalHeight
        self.width = image.naturalWidth

class PyAngelo():
    def __init__(self):
        global test_buff, PyAngeloWorker, array
        
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
        
        # clear to cornflower blue (XNA!) by default        
        self.__clear(0.392,0.584,0.929)
        
        
        test_buff = window.SharedArrayBuffer.new(255)
        array = window.Int8Array.new(test_buff)
        array[0] = 0  
        window.console.log("Attempting to send shared data")
        PyAngeloWorker.send(test_buff)            
        
    def clear(self, r=0, g=0, b=0, a=1):
        window.console.log("Clearing...")
        kwargs = {"r": r, "g": g, "b": b, "a": a}
        self.commands.append(["clear", kwargs])
        
    def drawLine(self, x1, y1, x2, y2, r=1.0, g=1.0, b=1.0, a=1.0, width=1):
        kwargs = {"x1": x1, "y1": y1, "x2": x2, "y2": y2, "r": r, "g": g, "b": b,
                  "a": a, "width": width}
        self.commands.append(["drawLine", kwargs])
        
    def isKeyPressed(self, key):
        return self.keys[key]        
                
    def drawImage(self, image, x, y, width=None, height=None, rotation=0, anchorX=None, anchorY=None, opacity=1.0,
                  r=1.0, g=1.0, b=1.0, rect=None):
        kwargs = {"image": image, "x": x, "y": y, "width": width, "height": height, "rotation": rotation,
                  "anchorX": anchorX,
                  "anchorY": anchorY, "opacity": opacity, "r": r, "g": g, "b": b, "rect": rect}
        self.commands.append(["drawImage", kwargs])   

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

    def __pauseSound(self, sound):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].pause()        
        
    def _keydown(self, ev):
        window.console.log("key pressed!" + str(ev.which));
        
        self.keys[ev.which] = True
        
        global array
        array[ev.which] = 1

    def _keyup(self, ev):
        self.keys[ev.which] = False      

        global array
        array[ev.which] = 0
        
        
    def resourceLoaded(self, e):
        self.loadingResources -= 1
        e.target.jmssImg.height = e.target.naturalHeight
        e.target.jmssImg.width = e.target.naturalWidth        
        
    def loadImage(self, file):
    
        if file in self.resources:
            return self.resources[file]       
        
        self.loadingResources += 1
        
        img = html.IMG(src = file)
        #alert("Attempting to draw image");
        img.bind('load', self.resourceLoaded)
        jmssImg = PyAngeloImage(img)
        img.jmssImg = jmssImg
        
        self.resources[file] = jmssImg
        
        return jmssImg

    def __drawImage(self, image, x, y, width = None, height = None, rotation=0, anchorX = None, anchorY = None, opacity=None, r=1.0, g=1.0, b=1.0, rect=None):        
        
        if (isinstance(image, str)):
            image = self.loadImage(image)
        
        if self.loadingResources > 0:
            return
            
        #alert("Attempting to draw image");    
        
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

    def __clear(self, r = 0, g = 0, b = 0, a = 1):
        global array
        window.console.log("Clearing for reals!");
        self.ctx.fillStyle= "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0))+ ")"
        self.ctx.fillRect(0, 0, self.width, self.height)    
        
        '''
        # testing the shared memory        
        if array is not None:
            array[0] += 1
            if array[0] >= 255:
                array[0] = 0
        '''
        
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
        
    def _convY(self, y):
        return self.height - y

    def _convColor(self, c):
        return (int(c[0] * 255.0), int(c[1] * 255.0), int(c[2] * 255.0), int(c[3] * 255.0))                
       
    def execute_commands(self, do_frame = True):   
        if not self.stopped:
            window.console.log("before frame()")
      

            while len(self.commands) > 0:
                command = self.commands[0]
                
                if command[0] == "drawLine":
                    command[0] = self.__drawLine
                elif command[0] == "clear":
                    window.console.log("clear command read")
                    window.console.log(command[1])
                    command[0] = self.__clear
                elif command[0] == "drawImage":                
                    command[0] = self.__drawImage
                elif command[0] == "loadSound":                
                    command[0] = self.__loadSound                
                elif command[0] == "playSound":                
                    command[0] = self.__playSound
                elif command[0] == "pauseSound":                
                    command[0] = self.__pauseSound                
                else:
                    # not a valid command
                    del self.commands[0]
                    continue
                    
                command[0](**command[1])    
                del self.commands[0]
            window.console.log("before frame()")        

            #timer.set_timeout(self.execute_commands, 16)  
        # get ready for next frame

    def pause(self):
        
        window.console.log("pausing code...")
        self.stopped = True
       
    def resume(self):        
        window.console.log("resuming code...")
        self.stopped = False

        timer.set_timeout(self.execute_commands, 16)          

        
    def start(self):
        self.commands = []
        
        window.console.log("running code...")
        self.stopped = False

        timer.set_timeout(self.execute_commands, 16)       

    def stop(self):        
        self.stopped = True        
        # clear to cornflower blue (XNA!) by default        
        self.__clear(0.392,0.584,0.929)		
        
        
graphics = PyAngelo()

@bind(PyAngeloWorker, "message")
def onmessage(e):
    """Handles the messages sent by the worker."""
    #result.text = e.data
    if e.data[0] == "reveal":
        window.console.log("Executing on the main thread...")
        graphics.commands = e.data[1]
        graphics.execute_commands()

def format_string_HTML(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>").replace("\"", "&quot;").replace("'", "&apos;").replace(" ", "&nbsp;")

def do_print(s, color=None):
    if color is not None: window.writeOutput("<p style='display:inline;color:" + color + ";'>" + format_string_HTML(s) + "</p>", True)
    else: window.writeOutput("<p style='display:inline;'>" + format_string_HTML(s) + "</p>", True)

def do_print_formatted(s):
    window.writeOutput(s, True)

class PrintOutput:
    def write(self, data):
        alert(str(data));
        #add_event(EventPrint(do_print, [str(data)]))
        #do_print(data)
    def flush(self):
        pass

class ErrorOutput:
    def write(self, data):
        #alert(str(data));
        #PynodeCoreGlobals.error += "<p style='display:inline;color:red;'>" + format_string_HTML(str(data)) + "</p>"
        document["console"].innerHTML += "<p style='display:inline;color:red;'>" + format_string_HTML(str(data)) + "</p>"
    def flush(self):
        pass

sys.stdout = PrintOutput()
sys.stderr = ErrorOutput()

def end_playing():
    if not PynodeCoreGlobals.has_ended:
        clear_button_run()
        document["runPlay"].style.display = "inherit"
        document["run"].bind("click", button_play)
        do_print("Done\n", color="green")

def clear_button_run():
    document["runPlay"].style.display = "none"
    #document["runPlayLoad"].style.display = "none"
    document["runPause"].style.display = "none"
    document["runResume"].style.display = "none"
    for event in document["run"].events("click"):
        document["run"].unbind("click", event)
    document["run"].bind("click", save_code)

def button_play(event):    
    #reset()
    clear_button_run()
    #document["runPlayLoad"].style.display = "inherit"
    document["run"].bind("click", button_pause)
    do_play()
    #timer.set_timeout(do_play, 20)

# attempt to replace the first while True: loop with a function
import re
def preProcess(src):
    preProcessed = str(src)
    pos = src.find("while True:")
    if pos != -1:
        namespace = globals()
        namespace["__name__"] = "__main__"

        # execute the code up to the loop
        # grab all the globals and put them as 'globals' into the first line of the new function
        exec(src[:pos], namespace, namespace)

        globals_str = ""
        g = globals()
        for v in g:
            if not callable(g[v]) and v[:2] != "__":
                globals_str += v + ","
        if len(globals_str) > 0:
            globals_str = globals_str[:-1]                

        # now find the whitespace sequence after the "while True:\n" substring
        # => this is the indent sequence
        match = re.search(r"\s+", src[pos + 12:])
        window.console.log(match.span())

        indentStr = src[pos + 12 + match.span()[0]:pos + 12 + match.span()[1]]

        
	
        replaceStr = "def loop():\n" + indentStr + "global " + globals_str +"\n"
        window.console.log(replaceStr)
        # TODO: remember to call the function with setInterval()!
        preProcessed = preProcessed.replace("while True:", replaceStr, 1)
        preProcessed = preProcessed + "\ninterval_001 = timer.set_interval(loop, 16)\n"
    return preProcessed

def do_play():
    window.console.log("Getting code")
    src = window.getCode()
    
    window.console.log(src)
    try:
        success = True
        try:
            # try and run the code in the web worker!!!!
            PyAngeloWorker.send(["run", src])
            '''
            # running the code locally 
            src = preProcess(src)
            namespace = globals()
            namespace["__name__"] = "__main__"
            graphics.commands = []
            graphics.stopped = False
            exec(src, namespace, namespace) 
            graphics.execute_commands(False)
            graphics.start()
            '''
        except Exception as exc:
            alert("Error!");
            traceback.print_exc(file=sys.stderr)
            handle_exception()
            success = False
        clear_button_run()
        document["runPause"].style.display = "inherit"
        document["run"].bind("click", button_pause)
    except:
        pass

def button_pause(event):
    clear_button_run()
    document["runResume"].style.display = "inherit"
    document["run"].bind("click", button_resume)
    graphics.pause()


def button_resume(event):
    clear_button_run()
    document["runPause"].style.display = "inherit"
    document["run"].bind("click", button_pause)
    graphics.resume()


def button_stop(event):
    clear_button_run()
    document["runPlay"].style.display = "inherit"
    document["run"].bind("click", button_play)

    graphics.stop()
    # only for local execution with preprocessing
    # timer.clear_interval(interval_001)
    
def button_restart(event):
    button_play(event)

def save_code(event):
    window.saveCode()        
        
###################################################################################        




