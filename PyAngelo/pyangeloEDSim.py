import sys
import time
import traceback
import javascript
import random
import json
import math

from vector import *

from browser import document, window, alert, timer, worker, bind, html, load
from browser.local_storage import storage

load("howler.js")

# Cursor control and motion
KEY_HOME          = 0xff50
KEY_ESC           = 27
KEY_LEFT          = 37
KEY_UP            = 38
KEY_RIGHT         = 39
KEY_DOWN          = 40
KEY_W             = 87
KEY_A             = 65
KEY_C             = 67
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

PyAngeloWorker = worker.Worker("executor")

test_buff = None
array = None

class EDSim():
    # Unique constants
    V2                  =   1
    CM                  =   2
    TEMPO_MEDIUM        =   3
    ON                  =   True
    OFF                 =   False
    FORWARD             =   6
    BACKWARD            =   7
    SPIN_RIGHT          =   8
    SPIN_LEFT           =   9
    TIME_MILLISECONDS   =  10
    
    # values       
    SPEED_1             =   1
    SPEED_2             =   2
    SPEED_3             =   3
    SPEED_4             =   4
    SPEED_5             =   5
    SPEED_6             =   6
    SPEED_7             =   7
    SPEED_8             =   8
    SPEED_9             =   9
    SPEED_10            =  10    
    SPEED_FULL          =   0
    
    CLAP_DETECTED       = True
    CLAP_NOT_DETECTED   = False
        
    #settings
    EdisonVersion   = V2
    DistanceUnits   = CM
    Tempo           = TEMPO_MEDIUM
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.position           = Vector(250, 200)
        self.speed              = 0
        self.heading            = Vector(0, 1)
        self.orientation        = 0
        
        self.current_rotation   = 0
        self.target_rotation    = 0
        self.rotation_speed     = 0
        
        self.current_distance   = 0
        self.target_distance    = 0
        
        self.leftLED            = False
        self.rightLED           = False
                
        self.img = html.IMG(src = "ed.png")  
        self.led_img = html.IMG(src = "led.png")
        
        self.height = 64
        self.width = 62
        
    def update(self):
        if self.current_rotation < self.target_rotation:
            self.current_rotation += abs(self.rotation_speed)
            self.orientation += self.rotation_speed
            # correct for overshoot
            if self.current_rotation > self.target_rotation:
                self.orientation -= math.copysign(self.current_rotation - self.target_rotation, self.rotation_speed)
            
        if self.current_distance < self.target_distance:
            self.current_distance += abs(self.speed)            
            self.position += self.heading.rotate(self.orientation) * self.speed 
               

class PyAngeloEDSim():
    # states
    STATE_WAIT      =   0
    STATE_STOP      =   1
    STATE_RUN       =   2
    
    def __init__(self):
        global array
        self.ed = EDSim()
        
        self.canvas = document["canvas"]
        self.ctx = self.canvas.getContext('2d')		
        
        self.width = self.canvas.width
        self.height = self.canvas.height   

        self.bg = html.IMG(src = "carpet.jpg")           
        
        self.bgcolor = Vector(0, 0, 0, 1)
        
        self.clap_timer = 0
        self.clap_time = 500
        
        self.anim_timer = 0
        self.anim_time = 200
        
        self.blink_running = 300
        
        self.starting_text = "Starting up"
        self.show_playing_text = True
        
        self.keys = dict([(a, False) for a in range(255)] +
                         [(a, False) for a in range(0xff00, 0xffff)]) 
                         
        document.bind("keydown", self._keydown)
        document.bind("keyup", self._keyup)           
                
        test_buff = window.SharedArrayBuffer.new(255)
        array = window.Int8Array.new(test_buff)
        
        window.console.log("Attempting to send shared data")
        PyAngeloWorker.send(test_buff) 
        
        howl = window.Howl
        self.clap_sound = howl.new({"src": ["clap.mp3"]})

        self.state = self.STATE_WAIT
        self.interval_timer = timer.set_interval(self.update, 16)
        self.reset()

    def reset(self):
        self.ed.reset()
        global array
        array[KEY_ESC] = 0
        
        
    def _keydown(self, ev):
        window.console.log("key pressed!" + str(ev.which));
        
        self.keys[ev.which] = True
        
        global array
        
        if ev.which == KEY_C:
            if self.clap_timer <= 0:
                # clapping
                self.clap_timer = self.clap_time
                self.clap_sound.play()
                        
        array[ev.which] = 1

    def _keyup(self, ev):
        self.keys[ev.which] = False      

        global array
        array[ev.which] = 0        
        
    def stop(self):        
        #timer.clear_interval(self.interval_timer)
        self.ed.reset()
        
    def clearclap(self):
        self.clap_timer = 0
        # no need to change the shared array because the worker would have done this
                
    def update(self):    
        self.anim_timer -= 16
        if self.anim_timer <= 0:
            self.anim_timer = 0
            
        if self.state == self.STATE_WAIT:
            self.ctx.fillStyle = "#000000"; 
            self.ctx.fillRect(0, 0, self.width, self.height)   
            self.ctx.fillStyle = "#ffffff"; 
            self.ctx.font = "40px Georgia";
            
            if self.anim_timer <= 0:
                self.anim_timer = self.anim_time
                
                self.starting_text += "."
                if self.starting_text.count(".") > 5:
                    self.starting_text = self.starting_text[:-5]
            self.ctx.fillText(self.starting_text, 100, 200);            
        else:
            # update
            
            # count down the clap for debounce
            self.clap_timer -= 16
            if self.clap_timer <= 0:
                self.clap_timer = 0
                array[KEY_C] = 0
            else:
                array[KEY_C] = 1
                
            self.ed.update()
            
            # check for borders
            pos_x = self.ed.position[0]
            pos_y = self.ed.position[1]
            if pos_y > self.height -  self.ed.height//2:
                pos_y = self.height -  self.ed.height//2
            elif pos_y < self.ed.height//2:
                pos_y = self.ed.height//2
            self.ed.position = Vector(pos_x, pos_y)
                                
            # render
            # clear the screen
            
            self.ctx.fillStyle= "rgba(" + str(int(self.bgcolor[0] * 255.0)) + \
                                "," + str(int(self.bgcolor[1] * 255.0)) + \
                                "," + str(int(self.bgcolor[2] * 255.0)) + \
                                "," + str(int(self.bgcolor[3] * 255.0))+ ")"
            
            self.ctx.fillRect(0, 0, self.width, self.height)   
            
            
            self.ctx.drawImage(self.bg, 0, 0)#, self.width, self.height)
            
            self.ctx.save()
            x = self.ed.position[0]
            y = self.height - self.ed.position[1]
            width = self.ed.width
            height = self.ed.height
            anchorX = 0.5
            anchorY = 0.75
            
            orientation = math.radians(self.ed.orientation)
            
            self.ctx.translate(x, y)
            self.ctx.rotate(- orientation)# - 3.1415926535)# + math.PI / 180)
            self.ctx.drawImage(self.ed.img, -anchorX * width, -anchorY * height, width, height)
            
            if self.ed.leftLED:
                anchorX = 0.3
                anchorY = 0.75            
                self.ctx.drawImage(self.ed.led_img, -anchorX * width, -anchorY * height)
            
            if self.ed.rightLED:
                anchorX = -0.15
                anchorY = 0.75            
                self.ctx.drawImage(self.ed.led_img, -anchorX * width, -anchorY * height)
            
            self.ctx.restore()
            
            if self.state == self.STATE_RUN:
                if self.anim_timer <= 0:
                    self.anim_timer = self.blink_running
                
                    self.show_playing_text = not self.show_playing_text
                if self.show_playing_text:
                    self.ctx.fillStyle = "#ffffff"; 
                    self.ctx.font = "20px Georgia";                    
                    self.ctx.fillText("Running...", 10, 30);  
            
            #self.ctx.drawImage(self.ed.img, self.ed.position[0] - self.ed.width//2, \
            #                                self.height - self.ed.position[1] - self.ed.height//2)
                                        
Ed = PyAngeloEDSim()

@bind(PyAngeloWorker, "message")
def onmessage(e):
    """Handles the messages sent by the worker."""
    if e.data[0] == "drive":
        speed = int(e.data[2]) * 0.25
        if e.data[1] == EDSim.BACKWARD or e.data[1] == EDSim.FORWARD: 
            if e.data[1] == EDSim.BACKWARD: 
                Ed.ed.speed = -speed
            else:
                Ed.ed.speed = speed 
            Ed.ed.current_distance = 0
            Ed.ed.target_distance = int(e.data[3] * 5)  # depends on UNITs                
        elif e.data[1] == EDSim.SPIN_RIGHT or e.data[1] == EDSim.SPIN_LEFT:
            if e.data[1] == EDSim.SPIN_RIGHT:
                Ed.ed.rotation_speed = -speed
            else:            
                Ed.ed.rotation_speed = speed
            Ed.ed.current_rotation = 0
            Ed.ed.target_rotation = int(e.data[3])
    elif e.data[0] == "clearclap":
        Ed.clearclap()
    elif e.data[0] == "LED":
        if e.data[1] == True:
            Ed.ed.rightLED = e.data[2]
        else:
            Ed.ed.leftLED = e.data[2]
    elif e.data[0] == "waitdone":
        window.console.log("finished waiting");
        if Ed.state == Ed.STATE_WAIT:
            Ed.state = Ed.STATE_STOP    
        else:
            Ed.state = Ed.STATE_RUN                           
    elif e.data[0] == "stop":
        window.console.log("stopped");            
        Ed.state = Ed.STATE_STOP
    elif e.data[0] == "print":
        do_print(e.data[1])
    elif e.data[0] == "error":
        do_print(e.data[1], "red")        

def format_string_HTML(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>").replace("\"", "&quot;").replace("'", "&apos;").replace(" ", "&nbsp;")

def do_print(s, color=None):
    if color is not None: window.writeOutput("<p style='display:inline;color:" + color + ";'>" + format_string_HTML(s) + "</p>", True)
    else: window.writeOutput("<p style='display:inline;'>" + format_string_HTML(s) + "</p>", True)

def clear_button_run():
    document["runPlay"].style.display = "none"
    document["runPlayLoad"].style.display = "none"
    document["runPause"].style.display = "none"
    document["runResume"].style.display = "none"
    for event in document["run"].events("click"):
        document["run"].unbind("click", event)
    document["run"].bind("click", save_code)

def button_play(event):   
    if Ed.state == Ed.STATE_WAIT:
        return
    window.console.log("resetting..")
    Ed.reset()
    
    clear_button_run()
    document["runPlayLoad"].style.display = "inherit"
    document["run"].bind("click", button_pause)
    do_play()

def do_play():
    window.console.log("Getting code")
    src = window.getCode()
    
    window.console.log(src)
    try:
        success = True
        try:
            # try and run the code in the web worker!!!!
            PyAngeloWorker.send(["run", src])
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
    Ed.stop()
    global array
    array[KEY_ESC] = 1
    clear_button_run()
    document["runResume"].style.display = "inherit"
    document["run"].bind("click", button_play)

def button_resume(event):
    clear_button_run()
    document["runPause"].style.display = "inherit"
    document["run"].bind("click", button_pause)

def save_code(event):
    window.saveCode()        
        
###################################################################################        




