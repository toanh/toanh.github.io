"""Web Worker script."""

# In web workers, "window" is replaced by "self".
import time
#from browser import bind, self
import sys
import traceback
import javascript
import random
import json

import traceback

from browser import bind, self
from pyangelo_consts import *

console = self.console
window = self
   
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
        
        # hardcoded for now
        self.width = 500
        self.height = 400
        
        self.reveal_on_clear = True

    def clear(self, r=0, g=0, b=0, a=1):
        # TODO: check for escape in every API call?
        
        if self.reveal_on_clear:
            self.reveal()
        elif array[KEY_ESC] == 1:
                console.log("Escape detected!")
                array[KEY_ESC] = 0
                raise SystemExit("QUIT requested")    
                
        global array
        
        kwargs = {"r": r, "g": g, "b": b, "a": a}
        
        self.commands.append([CMD_CLEAR, kwargs])
        
    '''def overlaps(self, x1, y1, width1, height1, x2, y2, width2, height2):
        return not ( ((x1 + width1) < x2) or 
                     ((x2 + width2) < x1) or
                     ((y1 + height1) < y2) or
                     ((y2 + height2) < y1) )
    '''
                     
    def overlaps(self, x1, y1, width1, height1, x2, y2, width2, height2):
        return ((x1 < (x2 + width2)) and ((x1 + width1) > x2) and (y1 < (y2 + height2)) and ((y1 + height1) > y2))
        
        '''return not ( ((x1 + width1) < x2) or 
                     ((x2 + width2) < x1) or
                     ((y1 + height1) < y2) or
                     ((y2 + height2) < y1) )                     
        '''
        
    def drawLine(self, x1, y1, x2, y2, r=1.0, g=1.0, b=1.0, a=1.0, width=1):
        kwargs = {"x1": x1, "y1": y1, "x2": x2, "y2": y2, "r": r, "g": g, "b": b,
                  "a": a, "width": width}
        self.commands.append([CMD_DRAWLINE, kwargs])
        
    def isKeyPressed(self, key):
    
        global array
        if key <= 255:
            return array[key] == 1
            
        return self.keys[key]      

    def drawText(self, text, x, y, fontName = "Arial", fontSize = 10, r = 1.0, g = 1.0, b = 1.0, a = 1.0, anchorX = "left", anchorY ="bottom"):
        kwargs = {"text": text, "x": x, "y": y, "fontName": fontName, "fontSize": fontSize, "r": r, "g": g, "b": b, "a": a, "anchorX": anchorX, "anchorY": anchorY}
        self.commands.append([CMD_DRAWTEXT, kwargs])
    
                
    def drawImage(self, image, x, y, width = None, height = None, rotation = 0, anchorX = None, anchorY = None, opacity = 1.0, r = 1.0, g = 1.0, b = 1.0, rect = None):
        kwargs = {"image": image, "x": x, "y": y, "width": width, "height": height, "rotation": rotation,
                  "anchorX": anchorX,
                  "anchorY": anchorY, "opacity": opacity, "r": r, "g": g, "b": b, "rect": rect}
        self.commands.append([CMD_DRAWIMAGE, kwargs])   
        
    def drawPixel(self, x, y, r = 1.0, g = 1.0, b = 1.0, a = 1.0):
        kwargs = {"x":x, "y": y, "r": r, "g": g, "b": b, "a": a}
        self.commands.append([CMD_DRAWPIXEL, kwargs])
        
    def drawRect(self, x1, y1, x2, y2, r = 1.0, g = 1.0, b = 1.0, a = 1.0):           
        kwargs = {"x1":x1, "y1": y1, "x2":x2, "y2": y2, "r": r, "g": g, "b": b, "a": a}
        self.commands.append([CMD_DRAWRECT, kwargs])    
        
    def drawCircle(self, x, y, radius, r=1.0, g=1.0, b=1.0, a=1.0):
        kwargs = {"x": x, "y": y, "radius": radius, "r": r, "g": g, "b": b, "a": a}
        self.commands.append([CMD_DRAWCIRCLE, kwargs])
        
    def input(self, msg):
        kwargs = {"msg": msg}
        self.commands.append([CMD_INPUT, kwargs])
        
        self.reveal()
        # should now pause until the finish signal is received
        while array[KEY_ENTER] == 0:
            if array[KEY_ESC] == 1:
                console.log("Escape detected!")
                array[KEY_ESC] = 0
                raise SystemExit("QUIT requested")    

            
        returned_string = ""
        n = len(array) - 1
        while array[n] != KEY_ENTER:
            returned_string += chr(array[n])
            #array[n] = KEY_A
            n -= 1
        return returned_string
            

    def loadSound(self, filename, streaming = False):
        kwargs = {"filename": filename, "streaming": streaming}
        self.commands.append([CMD_LOADSOUND, kwargs])   
        return filename        

    def playSound(self, sound, loop = False):
        kwargs = {"sound": sound, "loop": loop}
        self.commands.append(["playSound", kwargs])   

    def pauseSound(self, sound):
        kwargs = {"sound": sound}
        self.commands.append(["pauseSound", kwargs])        

    # just an alias for pauseSound for now
    def stopSound(self, sound):
        kwargs = {"sound": sound}
        self.commands.append(["pauseSound", kwargs])

    def sleep(self, milliseconds):
        # flush the command buffer to this point
        self.reveal()
        
        # the sleep happens here
        currTime = window.performance.now()
        prevTime = currTime
        while (currTime - prevTime < milliseconds):
            currTime = window.performance.now()        
        
    def reveal(self):
    
        if array[KEY_ESC] == 1:
            console.log("Escape detected!")
            array[KEY_ESC] = 0
            raise SystemExit("QUIT requested")    
        
        # send and then block
        global array, console, window
        console.log("array[0]:" + str(array[0]))
        
        self.prevTime = self.currTime
        
        self.currTime = window.performance.now()
        
        while (self.currTime - self.prevTime < 16):
            self.currTime = window.performance.now()
            if array[KEY_ESC] == 1:
                console.log("Escape detected!")
                array[KEY_ESC] = 0
                raise SystemExit("QUIT requested")    
                                       
        send_message([CMD_REVEAL,self.commands])
        self.commands = []        
               
        return True
        
graphics = PyAngeloWorker()
array = None
shared = None

def run_code(src, globals, locals):
    global array
    self.console.log("running code...")
    try:
        exec(src , globals, locals)
        
        # execute the command in the queue (to show the results if they didn't call reveal())
        graphics.reveal()
        send_message([CMD_HALT])
    except Exception as e:
        self.console.log(str(e))
        
        send_message(["error", "Error: " + str(e) + "\n" + traceback.format_exc()])
        
    except SystemExit as se:
        send_message(["quit"])
       
def send_message(message):
    self.console.log("Worker sending to main thread..")
    self.send(message)   

@bind(self, "message")
def onmessage(evt):
    global graphics, clear, array, shared
    """Handle a message sent by the main script.
    evt.data is the message body.
    """
    if not isinstance(evt.data, list):
        self.console.log("Receiving shared data...")
        
        array = self.Int8Array.new(evt.data)
        workerResult = f'Result: {array[0]}'
        self.console.log(workerResult)  
        
        send_message(["ready"])
        return    
    
    command = evt.data[0]
    if command.lower() == "run":
        self.console.log("Executing on the worker thread!");
        src = evt.data[1]    
        success = True

        namespace = globals()
        namespace["__name__"] = "__main__"
        graphics.commands = []
        
        run_code(src, namespace, namespace)                            
   

class ErrorOutput:
    def write(self, data):
        send_message(["error", str(data)])
    def flush(self):
        pass
        
class PrintOutput:
    def write(self, data):
        send_message([CMD_PRINT, str(data)])
    def flush(self):
        pass


sys.stdout = PrintOutput()
sys.stderr = ErrorOutput()
