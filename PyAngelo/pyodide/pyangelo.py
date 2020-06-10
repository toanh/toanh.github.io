from js import document, window

from pyangelo_consts import *

class PyAngeloImage():
    def __init__(self, image, sprite):
        self.img = image
        self.height = image.naturalHeight
        self.width = image.naturalWidth
        self.sprite = sprite

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
        self.canvas = document.getElementById("canvas")
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

        document.addEventListener("keydown", self._keydown)
        document.addEventListener("keyup", self._keyup)   
        
        self.mouse_x = 0
        self.mouse_y = 0
        document.addEventListener("mousedown", self._mousedown)
        document.addEventListener("mouseup", self._mouseup)
        document.addEventListener("mousemove", self._mousemove)
        
        self.touches = {}
        
        document.addEventListener("touchstart", self._touchstart)
        document.addEventListener("touchend", self._touchend)
        document.addEventListener("touchmove", self._touchmove)        
        

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
        
        window.requestAnimationFrame(self.update)
        
    def imageLoaded(self, e):
        window.console.log("Successfully loaded file:" + e.target.src);
        
        jmssImg = self.resources[e.target.src]
            
        jmssImg.height = e.target.naturalHeight
        jmssImg.width = e.target.naturalWidth     

        if jmssImg.sprite is not None:
            if jmssImg.sprite.height == 0:
                jmssImg.sprite.height = e.target.naturalHeight
            if jmssImg.sprite.width == 0:
                jmssImg.sprite.width = e.target.naturalWidth
            #window.console.log("Setting sprite width and height:", e.target.jmssImg.sprite.height, e.target.jmssImg.sprite.width);
            
        self.loadingResources -= 1        
        
    def loadImage(self, file, sprite = None):
        #if "referrer" in document["output_run"].attrs:
        #    file = document["output_run"].attrs["referrer"] + file  
            
        if file in self.resources:
            return self.resources[file]             
        
        self.loadingResources += 1
        
        window.console.log("Attempting to load file:" + file);
        
        img = document.createElement("IMG");
        img.crossOrigin = "Anonymous"
        img.src = file
        
        jmssImg = PyAngeloImage(img, sprite)       
        self.resources[file] = jmssImg        
        
        img.addEventListener('load', self.imageLoaded)
        #img.bind('error', self.resourceError)
        #img.bind('abort', self.resourceAbort)
        


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

    def isKeyPressed(self, key):
        return self.keys[key]             
        

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
        


    def drawText(self, text, x, y, fontName = "Arial", fontSize = 10, r = 1.0, g = 1.0, b = 1.0, a = 1.0, anchorX = "left", anchorY ="bottom"):
        self.ctx.fillStyle = "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(a) + ")"
        self.ctx.font = str(fontSize) + "pt " + fontName
        self.ctx.textBaseline = "bottom"
        self.ctx.fillText(text, x, self.height - y)        
        
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

    def loop(self, func):
        self.main_loop = func
        
    def update(self, dt):
        if self.main_loop is not None:
            self.main_loop()
        window.requestAnimationFrame(self.update);
                
    def clear(self, r = 0, g = 0, b = 0, a = 1):
        self.ctx.fillStyle= "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(a)+ ")"
        self.ctx.fillRect(0, 0, self.width, self.height)            
        
    def _convY(self, y):
        return self.height - y        