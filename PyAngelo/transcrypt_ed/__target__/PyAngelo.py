import sys
import time
import random

KEY_HOME          = 0xff50
KEY_ENTER         = 13
KEY_ESC           = 27
KEY_LEFT          = 37
KEY_UP            = 38
KEY_RIGHT         = 39
KEY_DOWN          = 40
KEY_W             = 87
KEY_A             = 65
KEY_S             = 83
KEY_D             = 68
KEY_Q             = 81
KEY_J             = 74
KEY_CTRL          = 17
KEY_PAGEUP        = 0xff55
KEY_PAGEDOWN      = 0xff56
KEY_END           = 0xff57
KEY_BEGIN         = 0xff58
KEY_V_LEFT        = "v_left"
KEY_V_RIGHT       = "v_right"
KEY_V_UP          = "v_up"
KEY_V_DOWN        = "v_down"
KEY_V_FIRE        = "v_fire"

CMD_DRAWLINE      = 1
CMD_CLEAR         = 2
CMD_DRAWIMAGE     = 3
CMD_LOADSOUND     = 4
CMD_PLAYSOUND     = 5
CMD_PAUSESOUND    = 6
CMD_DRAWTEXT      = 7
CMD_DRAWPIXEL     = 8
CMD_DRAWRECT      = 9
CMD_DRAWCIRCLE    = 10
CMD_REVEAL        = 11
CMD_HALT          = 12
CMD_PRINT         = 13
CMD_INPUT         = 14


#load("howler.js")

__pragma__ ('kwargs')

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
    def __init__(self, image, x = 0, y = 0, r = 1, g = 1, b = 1):
        if (isinstance(image, str)):
            image = graphics.loadImage(image, self)   
        self.image = image
        self.r = r
        self.g = g
        self.b = b
        self.width = 0
        self.height = 0
        
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
            
    def getHeight(self):
        if isinstance(self.image, PyAngeloImage):
            return self.image.height
        else:
            return self.height

    def getWidth(self):
        if isinstance(self.image, PyAngeloImage):
            return self.image.width
        else:
            return self.width
        
    def overlaps(self, other):
        # TODO: BUG! If the 'other' is an image that has a shared URL with a previously loaded image, collision doesn't work!!
        if isinstance(self.image, PyAngeloImage):
            x1 = self.x
            y1 = self.y
            width1 = self.image.width
            height1 = self.image.height
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
            width2 = other.image.width
            height2 = other.image.height
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
        return point.x >= self.x and point.x <= self.x + self.image.width and point.y >= self.y and point.y <= self.y + self.image.height
        
class TextSprite(Sprite):
    def __init__(self, text, fontSize = 20, fontName = "Arial", x = 0, y = 0, r = 1, g = 1, b = 1):
        textObject = Text(text, fontSize, fontName)
        Sprite.__init__(self, textObject, x, y, r, g, b)
        
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
        self.canvas = document.getElementById('canvas')
        self.width = self.canvas.getAttribute("width")
        self.height = self.canvas.getAttribute("height")
        self.ctx = self.canvas.getContext('2d')
        
        self.timer_id = None
        self.main_loop = None
        
        self.stopped = False
        
        self.resources =  {}
        self.loadingResources = 0
        
        self.keys = dict([(a, False) for a in range(255)]) 
        self.keys[KEY_V_LEFT] = False
        self.keys[KEY_V_RIGHT] = False
        self.keys[KEY_V_UP] = False
        self.keys[KEY_V_DOWN] = False
        self.keys[KEY_V_FIRE] = False       


        document.onkeydown = self._keydown
        document.onkeyup = self._keyup
        document.onmousemove = self._mousemove
        document.onmousedown = self._mousedown
        document.onmouseup = self._mouseup
        document.ontouchstart = self._touchstart
        document.ontouchmove = self._touchmove
        document.ontouchend = self._touchend        

        self.mouse_x = 0
        self.mouse_y = 0
        
        self.touches = {}
     
        self.soundPlayers = {}        
        
        self.state = self.STATE_RUN
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
        
        #window.setInterval(self.update, 17.0)
        window.requestAnimationFrame(self.update)     

    def isKeyPressed(self, key):
        return self.keys[key]             
        
    def refresh(self):
        self.execute_commands()
    
    ########################################################################################
        
    def loadSound(self, filename, streaming = False):
        '''
        howl = window.Howl
        return __new__(howl({"src": [filename]}))    
        howl = window.Howl
        sound = howl.new({"src": [filename]})
        self.soundPlayers[filename] = sound
        return filename
        '''
        howl = window.Howl
        sound = __new__(howl({"src": [filename]}))

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
                           
    def resourceLoaded(self, e):
        
        
        window.console.log("Successfully loaded file:" + e.target.src);
            
        e.target.jmssImg.height = e.target.naturalHeight
        e.target.jmssImg.width = e.target.naturalWidth     

        if e.target.jmssImg.sprite is not None:
            
            e.target.jmssImg.sprite.height = e.target.naturalHeight
            e.target.jmssImg.sprite.width = e.target.naturalWidth
            window.console.log("Setting sprite width and height:", e.target.jmssImg.sprite.height, e.target.jmssImg.sprite.width);
            
        self.loadingResources -= 1
            
       
    def loadImage(self, file, sprite = None):
    
        if file in self.resources:
            return self.resources[file]       
        
        self.loadingResources += 1
        
        window.console.log("Attempting to load file:" + file);
        
        img = document.createElement("img")
        
        img.setAttribute("src", file)
        img.setAttribute("crossOrigin", "Anonymous")
        img.addEventListener('load', self.resourceLoaded, False)
                
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
            self.drawImage(sprite.image, sprite.x - offsetX, sprite.y - offsetY)
            
    def measureText(self, text, fontName = "Arial", fontSize = 10):
        self.ctx.font = str(fontSize) + "pt " + fontName
        textMetrics = self.ctx.measureText(text)

        return (abs(textMetrics.actualBoundingBoxLeft) + abs(textMetrics.actualBoundingBoxRight), abs(textMetrics.actualBoundingBoxAscent) + abs(textMetrics.actualBoundingBoxDescent))

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
        if self.state == self.STATE_STOP:       
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
        
        window.requestAnimationFrame(self.update)
       
        
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
        #pixel = window.Int8Array.new(4)   

        pixel = __new__(window.Int8Array(4))        
                   
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

                              
