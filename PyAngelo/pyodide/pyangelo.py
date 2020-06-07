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

        #document.addEventListener("keydown", self._keydown)
        #document.addEventListener("keyup", self._keyup)   
        
        self.mouse_x = 0
        self.mouse_y = 0
        #document.addEventListener("mousedown", self._mousedown)
        #document.addEventListener("mouseup", self._mouseup)
        #document.addEventListener("mousemove", self._mousemove)
        
        self.touches = {}
        
        #document.addEventListener("touchstart", self._touchstart)
        #document.addEventListener("touchend", self._touchend)
        #document.addEventListener("touchmove", self._touchmove)        
        

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
        
        '''
        canvas = iodide.output.element('canvas')
        canvas.setAttribute('width', 450)
        canvas.setAttribute('height', 300)        
        '''
        
        img = document.createElement("IMG");
        img.crossOrigin = "Anonymous"
        img.src = file
        
        jmssImg = PyAngeloImage(img, sprite)       
        self.resources[file] = jmssImg        
        

        #img = html.IMG()
        #img.crossOrigin = "Anonymous"
        #img.src = file

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