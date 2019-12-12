"""Web Worker script."""

# In web workers, "window" is replaced by "self".
import time
#from browser import bind, self
import sys
import time
import traceback
import javascript
import random
import json
from browser import bind, self
KEY_HOME          = 0xff50
KEY_ESC           = 27
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

console = self.console
window = self

def run_code(src, globals, locals):
    global array
    self.console.log("running code...")
    try:
        exec(src , globals, locals)
    except Exception as e:
        self.console.log(str(e))
    #graphics.reveal()
       
def send_message(message):
    self.console.log("Worker sending to main thread..")
    self.send(message)    
    
class PyAngeloWorker():
    def __init__(self):
        self.test_data = None
        self.commands = []
                     
        self.timer_id = None
                
        self.revealed = False
        
        self.keys = dict([(a, False) for a in range(255)] +
                         [(a, False) for a in range(0xff00, 0xffff)])         
                         
        self.prevTime = 0
        self.currTime = self.prevTime

    def clear(self, r=0, g=0, b=0, a=1):
        global array
        
        #kwargs = {"r": r, "g": g, "b": b, "a": a}
        kwargs = {"r": r, "g": g, "b": b, "a": a}
        
        self.commands.append(["clear", kwargs])
        
    def drawLine(self, x1, y1, x2, y2, r=1.0, g=1.0, b=1.0, a=1.0, width=1):
        kwargs = {"x1": x1, "y1": y1, "x2": x2, "y2": y2, "r": r, "g": g, "b": b,
                  "a": a, "width": width}
        self.commands.append(["drawLine", kwargs])
        
    def isKeyPressed(self, key):
    
        global array
        if key <= 255:
            return array[key] == 1
            
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
        
    def reveal(self):
        
        # send and then block
        global array, console, window
        console.log("array[0]:" + str(array[0]))
        
        self.prevTime = self.currTime
        
        self.currTime = window.performance.now()
        
        while (self.currTime - self.prevTime < 16):
            self.currTime = window.performance.now()
                                       
        send_message(["reveal",self.commands])
        self.commands = []
        
        if array[KEY_ESC] == 1:
            console.log("Escape detected!")
            raise Exception("QUIT requested")
               
        return True
        
graphics = PyAngeloWorker()
array = None
shared = None


@bind(self, "message")
def onmessage(evt):
    global graphics, clear, array, shared
    """Handle a message sent by the main script.
    evt.data is the message body.
    """
    if not isinstance(evt.data, list):
        self.console.log("Receiving shared data...")
        shared = evt.data
        array = self.Int8Array.new(evt.data)
        workerResult = f'Result: {array[0]}'
        self.console.log(workerResult)  
        return    
    
    command = evt.data[0]
    if command.lower() == "run":
        #alert("Executing!")
        self.console.log("Executing on the worker thread!");
        src = evt.data[1]    
        success = True
        try:
            namespace = globals()
            namespace["__name__"] = "__main__"
            graphics.commands = []
            
            #exec(src, namespace, namespace)
            
            run_code(src, namespace, namespace)                            
        except Exception as exc:
            self.console.log("exception attempting to run code:" + str(exc))
            #self.send(["return",[1, str(exc)]])
        #self.send(["return",[0, graphics.commands]])     
