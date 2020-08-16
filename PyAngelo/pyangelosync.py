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
    def __init__(self, image, sprite):
        self.img = image
        self.height = image.naturalHeight
        self.width = image.naturalWidth
        self.sprite = sprite
        
class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
class Rectangle():
    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
class Circle():
    def __init__(self, x = 0, y = 0, radius = 0):
        self.x = x
        self.y = y
        self.radius = radius
        
class Colour():
    def __init__(self, r = 1.0, g = 1.0, b = 1.0, a = 1.0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        
class Text():
    def __init__(self, text, fontSize = 20, fontName = "Arial"):
        self.text = text
        self.fontSize = fontSize
        self.fontName = fontName
        self.width = graphics.measureText(text, fontName, fontSize)[0]
        self.height = graphics.measureText(text, fontName, fontSize)[1]
        
       
        
class Sprite:
    def __init__(self, image, x = 0, y = 0, width = 0, height = 0, r = 1, g = 1, b = 1):
        if (isinstance(image, str)):
            image = graphics.loadImage(image, self)   
        self.image = image
        self.r = r
        self.g = g
        self.b = b
        self.width = width
        self.height = height
        
        # user defined!
        self.type = 0
        
        if isinstance(image, Circle):
            self.x = self.image.x
            self.y = self.image.y
            self.radius = self.image.radius
        elif isinstance(image, Rectangle):
            self.x = self.image.x
            self.y = self.image.y
            self.width = self.image.width
            self.height = self.image.height
        elif isinstance(image, Text):
            self.x = x
            self.y = y
            self.width = self.image.width
            self.height = self.image.height            
        else:
            self.x = x
            self.y = y
            
    def setData(self, image):
        if isinstance(self.image, PyAngeloImage):
            self.image = graphics.loadImage(image, self) 
        elif isinstance(self.image, Text):
            self.image.text = image
            
    def getHeight(self):
        if isinstance(self.image, PyAngeloImage):
            if self.height == 0:
                return self.image.height
            else:
                return self.height
        else:
            return self.height

    def getWidth(self):
        if isinstance(self.image, PyAngeloImage):
            if self.width == 0:
                return self.image.width
            else:
                return self.width
        else:
            return self.width
        
    def overlaps(self, other):
        # TODO: BUG! If the 'other' is an image that has a shared URL with a previously loaded image, collision doesn't work!!
        if isinstance(self.image, PyAngeloImage):
            x1 = self.x
            y1 = self.y
            width1 = self.getWidth()
            height1 = self.getHeight()
        elif isinstance(self.image, Rectangle) or isinstance(self.image, Text):
            x1 = self.x
            y1 = self.y
            width1 = self.width
            height1 = self.height
        elif (isinstance(self.image, Circle)):
            x1 = self.x - self.radius
            y1 = self.y - self.radius
            width1 = self.radius * 2
            height1 = self.radius * 2
        else:
            x1 = self.x
            y1 = self.y
            width1 = self.width
            height1 = self.height        
            
        if (isinstance(other.image, PyAngeloImage)):
            x2 = other.x
            y2 = other.y
            width2 = other.getWidth()
            height2 = other.getHeight()
        elif isinstance(other.image, Rectangle) or isinstance(self.image, Text):
            x2 = other.x
            y2 = other.y
            width2 = other.width
            height2 = other.height            
        elif (isinstance(other.image, Circle)):
            x2 = other.x - other.radius
            y2 = other.y - other.radius
            width2 = other.radius * 2
            height2 = other.radius * 2
        else:
            x2 = other.x
            y2 = other.y
            width2 = other.width
            height2 = other.height            
            
        return ((x1 < (x2 + width2)) and ((x1 + width1) > x2) and (y1 < (y2 + height2)) and ((y1 + height1) > y2))   

    def contains(self, point):       
        return point.x >= self.x and point.x <= self.x + self.getWidth() and point.y >= self.y and point.y <= self.y + self.getHeight()
        
class TextSprite(Sprite):
    def __init__(self, text, x = 0, y = 0, fontSize = 20, fontName = "Arial", r = 1, g = 1, b = 1):
        textObject = Text(text, fontSize, fontName)
        Sprite.__init__(self, textObject, x, y, 0, 0, r, g, b)
        
class PyAngelo():
    STATE_STOP      =   1
    STATE_RUN       =   2
    STATE_HALT      =   3
    STATE_LOAD      =   4
    STATE_INPUT     =   5
    STATE_LOADED    =   6
    
    def __init__(self):
       
        self.commands = []
        
        # get the canvas element
        self.canvas = document["canvas"]
        self.ctx = self.canvas.getContext('2d')		
        
        self.width = self.canvas.width
        self.height = self.canvas.height
        
        self.timer_id = None
        self.main_loop = None
        
        self.stopped = False
        
        self.resources =  {}
        self.loadingResources = 0
        
        self.keys = dict([(a, False) for a in range(255)] +
                         [(a, False) for a in range(0xff00, 0xffff)]) 
        self.keys[KEY_V_LEFT] = False
        self.keys[KEY_V_RIGHT] = False
        self.keys[KEY_V_UP] = False
        self.keys[KEY_V_DOWN] = False
        self.keys[KEY_V_FIRE] = False                               

        document.bind("keydown", self._keydown)
        document.bind("keyup", self._keyup)   
        
        self.mouse_x = 0
        self.mouse_y = 0
        document.bind("mousedown", self._mousedown)
        document.bind("mouseup", self._mouseup)
        document.bind("mousemove", self._mousemove)
        
        self.touches = {}
        
        document.bind("touchstart", self._touchstart)
        document.bind("touchend", self._touchend)
        document.bind("touchmove", self._touchmove)        

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
        
        self.loading_filename = ""
        
        timer.request_animation_frame(self.update)     

    def isKeyPressed(self, key):
        return self.keys[key]             
        
    def refresh(self):
        self.execute_commands()
    
    ########################################################################################
        
    def loadSound(self, filename, loop = False, streaming = False):
        if "referrer" in document["output_run"].attrs and not filename.startswith("http"):
            filename = document["output_run"].attrs["referrer"] + filename
        howl = window.Howl
        sound = howl.new({"src": [filename], "loop": loop, "onload": self._soundLoaded})
        self.loadingResources += 1

        self.soundPlayers[filename] = sound
        self.soundPlayers[filename].begin_play = False
        return filename
        
    def _soundLoaded(self, e, f):
        window.console.log("Successfully loaded sound file:" + str(e) + "," + str(f));
        self.loadingResources -= 1

    def playSound(self, sound, loop = False, volume = 1.0):
  
        if sound not in self.soundPlayers:
            sound = self.loadSound(sound)
                        
        self.soundPlayers[sound].loop(loop)
        self.soundPlayers[sound].volume(volume)        
        self.soundPlayers[sound].play()
        
        self.soundPlayers[sound].begin_play = False
            
            
    def stopAllSounds(self):
        for sound in self.soundPlayers:
            self.stopSound(sound)

    def pauseSound(self, sound):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].pause()       

    # alias for pauseSound
    def stopSound(self, sound):
        if sound in self.soundPlayers:
            self.soundPlayers[sound].stop()   
        
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


    def _updateTouchedKeys(self):
        self.keys[KEY_V_LEFT] = False
        self.keys[KEY_V_RIGHT] = False
        self.keys[KEY_V_UP] = False
        self.keys[KEY_V_DOWN] = False
        self.keys[KEY_V_FIRE] = False      
        
        for touch in self.touches.values():
            x = touch[0]
            y = touch[1]
            
            if x < -self.width * 0.33 * 0.67 and y < self.height * 0.6 and y > self.height * 0.4:
                self.keys[KEY_V_LEFT] = True
            if x < 0 and x > -self.width * 0.33 * 0.33 and y < self.height * 0.6 and y > self.height * 0.4:
                self.keys[KEY_V_RIGHT] = True

            if y < self.height * 0.4 and y > 0 and x < -self.width * 0.33 * 0.33 and x > -self.width * 0.33 * 0.67:
                self.keys[KEY_V_DOWN] = True
            if y < self.height and y > self.height * 0.6 and x < -self.width * 0.33 * 0.33 and x > -self.width * 0.33 * 0.67:
                self.keys[KEY_V_UP] = True

            if x > self.width and y < self.height and y > 0:
                self.keys[KEY_V_FIRE] = True            

    def _touchstart(self, ev):
        #ev.preventDefault()
        for touch in ev.changedTouches:
            self.mouse_x = touch.clientX             
            self.mouse_y = touch.clientY
            
            boundingRect = self.canvas.getBoundingClientRect()    
            
            x = int(self.mouse_x - boundingRect.left)
            y = int(self.height - (self.mouse_y - boundingRect.top))
            
            self.touches[touch.identifier] = [x, y]
            
        self._updateTouchedKeys()
                        
        return False

        

    def _touchend(self, ev):   
        #ev.preventDefault()

        self.mouse_x = -1
        self.mouse_y = -1
        
        for touch in ev.changedTouches:
            del self.touches[touch.identifier]
        
        
        self._updateTouchedKeys()

        return False
        
    def _touchmove(self, ev):   
        #ev.preventDefault()
        for touch in ev.changedTouches:
            self.mouse_x = touch.clientX             
            self.mouse_y = touch.clientY
            
            boundingRect = self.canvas.getBoundingClientRect()    
            
            x = int(self.mouse_x - boundingRect.left)
            y = int(self.height - (self.mouse_y - boundingRect.top))
            
            self.touches[touch.identifier] = [x, y]
            
        self._updateTouchedKeys()            
                        
        return False
        
    def _mousemove(self, ev):
        self.mouse_x = ev.clientX             
        self.mouse_y = ev.clientY            
        
    def _mousedown(self, ev):
        self.mouse_x = ev.clientX             
        self.mouse_y = ev.clientY
        
        boundingRect = self.canvas.getBoundingClientRect()    
        
        x = int(self.mouse_x - boundingRect.left)
        y = int(self.height - (self.mouse_y - boundingRect.top))
        
        self.keys[KEY_V_LEFT] = False
        self.keys[KEY_V_RIGHT] = False
        self.keys[KEY_V_UP] = False
        self.keys[KEY_V_DOWN] = False
        self.keys[KEY_V_FIRE] = False
        
        if x < -self.width * 0.33 * 0.67 and y < self.height * 0.6 and y > self.height * 0.4:
            self.keys[KEY_V_LEFT] = True
        if x < 0 and x > -self.width * 0.33 * 0.33 and y < self.height * 0.6 and y > self.height * 0.4:
            self.keys[KEY_V_RIGHT] = True

        if y < self.height * 0.4 and y > 0 and x < -self.width * 0.33 * 0.33 and x > -self.width * 0.33 * 0.67:
            self.keys[KEY_V_DOWN] = True
        if y < self.height and y > self.height * 0.6 and x < -self.width * 0.33 * 0.33 and x > -self.width * 0.33 * 0.67:
            self.keys[KEY_V_UP] = True

        if x > self.width and y < self.height and y > 0:
            self.keys[KEY_V_FIRE] = True         
        
    def _mouseup(self, ev):
        self.mouse_x = -1
        self.mouse_y = -1
        
        self.keys[KEY_V_LEFT] = False
        self.keys[KEY_V_RIGHT] = False
        self.keys[KEY_V_UP] = False
        self.keys[KEY_V_DOWN] = False
        self.keys[KEY_V_FIRE] = False     
    
    def getMousePos(self):
        boundingRect = self.canvas.getBoundingClientRect()    
        
        return Point(int(self.mouse_x - boundingRect.left), int(self.height - (self.mouse_y - boundingRect.top)))
        
                
    def resourceError(self, e):
        self.stop()
        do_print("Error loading of resource: " + e.target.src + "\n", "red")
        #del e.target
        #e.target.parentElement.removeChild(e.target)
    
    def resourceAbort(self, e):
        self.stop()
        do_print("Aborted loading of resource: " + e.target.src + "\n", "red")  
    
    def resourceLoaded(self, e):
        
        
        window.console.log("Successfully loaded file:" + e.target.src);
            
        e.target.jmssImg.height = e.target.naturalHeight
        e.target.jmssImg.width = e.target.naturalWidth     

        if e.target.jmssImg.sprite is not None:
            if e.target.jmssImg.sprite.height == 0:
                e.target.jmssImg.sprite.height = e.target.naturalHeight
            if e.target.jmssImg.sprite.width == 0:
                e.target.jmssImg.sprite.width = e.target.naturalWidth
            #window.console.log("Setting sprite width and height:", e.target.jmssImg.sprite.height, e.target.jmssImg.sprite.width);
            
        self.loadingResources -= 1
            
       
    def loadImage(self, file, sprite = None):
        if "referrer" in document["output_run"].attrs and not file.startswith("http"):
            file = document["output_run"].attrs["referrer"] + file  
            
        if file in self.resources:
            return self.resources[file]             
        
        self.loadingResources += 1
        
        window.console.log("Attempting to load file:" + file);
        img = html.IMG()
        img.crossOrigin = "Anonymous"
        img.src = file

        img.bind('load', self.resourceLoaded)
        img.bind('error', self.resourceError)
        img.bind('abort', self.resourceAbort)
        
        jmssImg = PyAngeloImage(img, sprite)
        img.jmssImg = jmssImg
        
        self.resources[file] = jmssImg

        return jmssImg

    def drawImage(self, image, x, y, width = None, height = None, rotation=0, anchorX = None, anchorY = None, opacity=None, r=1.0, g=1.0, b=1.0, rect=None):        
        
        #window.console.log("attempting to draw image")
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
        
    def drawSprite(self, sprite, offsetX = 0, offsetY = 0):
        if isinstance(sprite.image, Rectangle):
            self.drawRect(sprite.x - offsetX, sprite.y - offsetY, sprite.width, sprite.height, sprite.r, sprite.g, sprite.b)
        elif isinstance(sprite.image, Circle):
            self.drawCircle(sprite.x - offsetX, sprite.y - offsetY, sprite.radius, sprite.r, sprite.g, sprite.b)
        elif isinstance(sprite.image, Text):
            self.drawText(sprite.image.text, sprite.x - offsetX, sprite.y - offsetY, sprite.image.fontName, sprite.image.fontSize, sprite.r, sprite.g, sprite.b)            
        else:
            self.drawImage(sprite.image, sprite.x - offsetX, sprite.y - offsetY, width = sprite.getWidth(), height = sprite.getHeight())
            
    def measureText(self, text, fontName = "Arial", fontSize = 10):
        self.ctx.font = str(fontSize) + "pt " + fontName
        textMetrics = self.ctx.measureText(text)

        return (abs(textMetrics.actualBoundingBoxLeft) + abs(textMetrics.actualBoundingBoxRight), abs(textMetrics.actualBoundingBoxAscent) + abs(textMetrics.actualBoundingBoxDescent))

    def drawText(self, text, x, y, fontName = "Arial", fontSize = 10, r = 1.0, g = 1.0, b = 1.0, a = 1.0, anchorX = "left", anchorY ="bottom"):
        self.ctx.fillStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(a) + ")"
        self.ctx.font = str(fontSize) + "pt " + fontName
        self.ctx.textBaseline = "bottom"
        self.ctx.fillText(text, x, self.height - y)        

    def clear(self, r = 0, g = 0, b = 0, a = 1):
        global array
        self.ctx.fillStyle= "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(a)+ ")"
        self.ctx.fillRect(0, 0, self.width, self.height)    
        
    def drawLine(self, x1, y1, x2, y2, r = 1.0, g = 1.0, b = 1.0, a = 1.0, width = 1):
        r = min(r, 1.0)
        g = min(g, 1.0)
        b = min(b, 1.0)
        a = min(a, 1.0)

        self.ctx.beginPath()
        self.ctx.lineWidth = width
        self.ctx.strokeStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(a) + ")"
        self.ctx.moveTo(x1, self._convY(y1))
        self.ctx.lineTo(x2, self._convY(y2))
        self.ctx.stroke()

    def drawCircle(self, x, y, radius, r=1.0, g=1.0, b=1.0, a=1.0):
        r = min(r, 1.0)
        g = min(g, 1.0)
        b = min(b, 1.0)
        a = min(a, 1.0)

        self.ctx.fillStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(a) + ")"
        self.ctx.beginPath();
        self.ctx.strokeStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(
            int(b * 255.0)) + "," + str(a) + ")"

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
        ctx.fillStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(a) + ")"        
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
            if "auto" in document["output_run"].attrs:
                button_play(None)
                del document["output_run"].attrs["auto"]
            self.clear(0.392,0.584,0.929)
            width = self.measureText("Ready", fontSize = 30)[0]
            self.drawText("Ready", 250 - width/2, 170, fontSize = 30)
        elif self.state == self.STATE_RUN:   
            if self.main_loop is not None:
                try:
                    self.main_loop()
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
        elif self.state == self.STATE_LOAD:
            self.clear(0.192,0.384,0.729)
            text = "Loading: " + self.loading_filename
            width = self.measureText(text, fontSize = 20)[0]
            self.drawText(text, 250 - width/2, 170, fontSize = 20)            
        elif self.state == self.STATE_LOADED:
            self.clear(0.192,0.384,0.729)
            
            text = "Successfully Loaded:"
            width = self.measureText(text, fontSize = 20)[0]
            self.drawText(text, 250 - width/2, 200, fontSize = 20)            
            
            text = self.loading_filename
            width = self.measureText(text, fontSize = 20)[0]
            self.drawText(text, 250 - width/2, 170, fontSize = 20)            
        
        timer.request_animation_frame(self.update)
       
        
    def start(self):
        if self.state != self.STATE_RUN:
            self.state = self.STATE_RUN
                        
    def stop(self):   
        disable_stop_enable_play() 
        if self.state != self.STATE_STOP:
            self.state = self.STATE_STOP            

            # TODO: put all these into a Reset() method
            self.resources =  {}
            self.loadingResources = 0

            self.stopAllSounds()     

    def getPixelColour(self, x, y):
        pixel = window.Int8Array.new(4)      
                   
        imageData = self.ctx.getImageData(x, self._convY(y), 1, 1)
        
        return Colour(imageData.data[0]/255.0, imageData.data[1]/255.0, imageData.data[2]/255.0, imageData.data[3]/255.0)            
              

    def sleep(self, milliseconds):
        # the sleep happens here, it's a tight loop - may hang the browser!
        currTime = window.performance.now()
        prevTime = currTime
        while (currTime - prevTime < milliseconds):
            currTime = window.performance.now()      
            
    def overlaps(self, x1, y1, width1, height1, x2, y2, width2, height2):
        return ((x1 < (x2 + width2)) and ((x1 + width1) > x2) and (y1 < (y2 + height2)) and ((y1 + height1) > y2))     


                              
graphics = PyAngelo()

def startLoading(filename):
    window.console.log("starting load")
    graphics.state = graphics.STATE_LOAD
    graphics.loading_filename = filename
    
def doneLoading():
    window.console.log("finish load")
    graphics.state = graphics.STATE_LOADED
    
    disable_stop_enable_play() 
    graphics.resources =  {}
    graphics.loadingResources = 0
    graphics.stopAllSounds()       

window.startLoading = startLoading
window.doneLoading = doneLoading

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
    
pre_globals = []
def do_play():
    global pre_globals
    
    graphics.main_loop = None

    start_tag = "@loop_animation"
    end_tag = "@loop_animation"
    
    src = window.getCode()
        
    lines = src.split("\n")
    
    non_frame_code = []
    
    frame_code = []

    line_num = 0
    while line_num < len(lines):
        line = lines[line_num]
        line_num += 1
        if line.lower()[:len(start_tag)] != start_tag:
            non_frame_code.append(line)            
        else:            
            break
        
            
    while line_num < len(lines):
        line = lines[line_num]
        line_num += 1
        if line.lower()[:len(end_tag)] != end_tag:
            frame_code.append(" " + line +"\n")
        else:
            break
                
    while line_num < len(lines):
        line = lines[line_num]
        non_frame_code.append(line + "\n")
        line_num += 1                
        
    src = "\n".join(non_frame_code)
    src += "\n"
    
    window.console.log("Non frame code:")
    window.console.log(src)
        
    if len(pre_globals) == 0:
        pre_globals = list(globals().keys())

    namespace = globals()
    namespace["__name__"] = "__main__"        

   
    if len(frame_code) > 0:   

        run_code(src, namespace, namespace, False)    
        
        post_globals = list(globals().keys())
        global_code = ""
        for g in post_globals:
            if g not in pre_globals:
                global_code += g + ","
        if len(global_code) > 0:
            frame_code.insert(0, " global " + global_code[:-1] + "\n")
        
        frame_code.insert(0, "def frame_code():")
        
        frame_code.insert(0, "@graphics.loop")
        
        
        src = "\n".join(frame_code)
        window.console.log("Frame code:")
        window.console.log(src)
       
        run_code(src, namespace, namespace, True)    
    else:
        run_code(src, namespace, namespace, True)
              
            
    
def run_code(src, globals, locals, is_frame_code = True):
    #self.console.log("running code...")
    try:
        
        if is_frame_code:
            graphics.start()  
        exec(src , globals, locals)
        
    except Exception as e:
        do_print("Error in parsing: " + str(e) + "\n" + traceback.format_exc(), "red") 
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
        do_print(data, "green") 
    def flush(self):
        pass


sys.stdout = PrintOutput()
sys.stderr = ErrorOutput()    
        
###################################################################################        
