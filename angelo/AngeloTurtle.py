from math import *
from browser import bind, self, window
from browser import document, window, alert, timer, worker, bind, html, load

from pyangelo_consts import *

class AngeloTurtle: 
    def __init__(self):
        self.x = 250
        self.y = 200
        self.dir = 0
        self.visible = True
        self.trail = True
        self.filling = False
        
        self.dest_x = self.x
        self.dest_y = self.y
        
        # the absolute angle in degrees
        self.dest_dir = self.dir
        
        self.prev_x = self.x
        self.prev_y = self.y
        
        self.stepSize = 20
        self.angleStepSize = 10
        
        self.commands = []
        
        # kill any existing canvases
        if "turtle_canvas" in document:        
            document["turtle_canvas"].remove()
        if "turtle_icon" in document:        
            document["turtle_icon"].remove()
        
        self.width = 500
        self.height = 400
        
        # for the turtle canvas
        self.canvas = html.CANVAS(width = self.width, height = self.height, id="turtle_canvas")
        self.canvas.style= {"z-index": 2, "position": "absolute", "left":"0px", "right":"0px", "background-position": "center"}
        self.ctx = self.canvas.getContext('2d');
        self.ctx.fillStyle= "rgba(0,0,0,0)"
        self.ctx.fillRect(0, 0, self.width, self.height)    
        outputBox = document["outputBox"] 
        outputBox <= self.canvas
        
        # for the turtle icon
        self.turtle = html.CANVAS(width = self.width, height = self.height, id="turtle_icon")
        self.turtle.style= {"z-index": 3, "position": "absolute", "left":"0px", "right":"0px", "background-position": "center"}
        self.turtle_ctx = self.turtle.getContext('2d');
        self.turtle_ctx.fillStyle= "rgba(0,0,0,0)"
        self.turtle_ctx.fillRect(0, 0, self.width, self.height)   
        outputBox = document["outputBox"] 
        outputBox <= self.turtle
        
        self.array = None
        
        self.instant_render = False
        
        self.fill_path = []
        
    def hide(self):
        self.visible = False
        self.turtle_ctx.clearRect(0, 0, self.width, self.height)
        return True
        
    def show(self):
        self.visible = True
        return True
        
    def penup(self):
        self.trail = False
        return True
        
    def pendown(self):
        self.trail = True
        return True
        
    def set_shared_memory(self, array):
    
        print("setting shared memory!", array)
        # shared memory
        self.array = array
        
        self.array[SEMAPHORE1] = 0
        
    def update(self):
        if len(self.commands) > 0:
            command = self.commands[0]
            #print("executing: ", str(command))
            if command[0](**command[1]):
                self.commands.remove(command)
        return
        
    def _convY(self, y):
        return self.height - y        
        
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

    def begin_fill(self):
        self.filling = True
        self.fill_path = []
        self.fill_path.append([self.x, self.height - self.y])
        return True
        
        
    def end_fill(self):
        self.filling = False
        self.ctx.beginPath()
        self.ctx.moveTo(self.fill_path[0][0], self.fill_path[0][1])
        for i in range(1, len(self.fill_path)):
            self.ctx.lineTo(self.fill_path[i][0], self.fill_path[i][1])
        self.ctx.closePath()
        self.ctx.fillStyle = "red";
        self.ctx.fill()
        return True
        
    def draw(self):
        if self.trail:
            self.__drawLine(self.prev_x, self.prev_y, self.x, self.y)
        if self.visible:
            self.turtle_ctx.clearRect(0, 0, self.width, self.height)
            
            self.turtle_ctx.fillStyle = "rgba(0,255,0,1)"
            self.turtle_ctx.font = "20pt arial bold"
            self.turtle_ctx.textBaseline = "bottom"
            
            icon_width = 40
            icon_height = 40
            self.turtle_ctx.save()
            self.turtle_ctx.translate(self.x, self._convY(self.y))
            self.turtle_ctx.rotate(- radians(self.dir))# - 3.1415926535)# + math.PI / 180)
            self.turtle_ctx.fillText("👻", -icon_width/2, icon_height/2) 
            #self.ctx.drawImage(image.img, -anchorX * width, -anchorY * height, width, height)
            self.turtle_ctx.restore()           
        
    def __rotate(self):
        prev_dir = self.dir
        
        self.dir += self.angleStepSize

        # check for crossover
        if (self.dest_dir - self.dir) * (self.dest_dir - prev_dir) <= 0:
            #if abs(self.dir - self.dest_dir) < 0.1:
            # have I reached my destination
            # pop off commands
            self.dir = self.dest_dir
            self.array[SEMAPHORE1] = 0
            return True
        else:
            return False
            
            
    def __move(self):
        #print("executing move command", len(self.commands))
        self.prev_x = self.x
        self.prev_y = self.y
        
        angle = radians(self.dir)
        
        eps = 0.001
        
        if abs(self.x - self.dest_x) > eps:
            self.x = self.prev_x + self.stepSize * cos(angle)
            
        if abs(self.y- self.dest_y) > eps:
            self.y = self.prev_y + self.stepSize * sin(angle)
        
        # check for overshoot
        # TODO: fix! Doesn't work for all step sizes, check and/or and <= >= logic
        
        if (self.dest_x - self.x) * (self.dest_x - self.prev_x) <= 0:
            self.x = self.dest_x
            
        if (self.dest_y - self.y) * (self.dest_y - self.prev_y) <= 0:
            self.y = self.dest_y
            
        if abs(self.x - self.dest_x) < eps and abs(self.y - self.dest_y) < eps:
            print("reached destination")
            self.array[SEMAPHORE1] = 0
            if self.filling:
                self.fill_path.append([self.dest_x, self.height - self.dest_y])
            
            return True
        else:
            return False
            
        #print(self.x, self.y, self.dest_x, self.dest_y)
            
            
    def receiveCommand(self, command):
        #print("receiving forward", len(self.commands))
        self.commands.insert(len(self.commands),command)
        #print("added forward trigger", len(self.commands))
        
    def speed(self, speed):
    
        if speed == 0:
            self.instant_render = True
        else:
            self.instant_render = False
            #print("Setting speed", speed)
            self.stepSize = speed
            self.angleStepSize = speed * 5
            
        return True
    
    def forward(self, steps):
        
        if steps < 0:
            self.stepSize = -abs(self.stepSize)
        else:
            self.stepSize = abs(self.stepSize)
            
        # do math! 
        #print("executing forward trigger", len(self.commands))
        angle = radians(self.dir)
        
        dx = steps * cos(angle)
        dy = steps * sin(angle)
        
        # set self.dest_x and self.dest_y
        self.dest_x = self.x + dx
        self.dest_y = self.y + dy
        
        
        # pop off the trigger command and replace with executor
        #del self.commands[0]
        #print("deleting forward trigger", len(self.commands))
        
        if self.instant_render:
            self.prev_x = self.x
            self.prev_y = self.y
            
            self.x = self.dest_x
            self.y = self.dest_y
            self.array[SEMAPHORE1] = 0
            
            if self.filling:
                self.fill_path.append([self.dest_x, self.height - self.dest_y])
        else:
            self.commands.insert(0, [self.__move, {}])
            
        return True
        
        
    def clear(self, r, g, b, a):
        self.ctx.clearRect(0, 0, self.width, self.height)
        
        self.ctx.fillStyle= "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0))+ ")"        
        self.ctx.fillRect(0, 0, self.width, self.height) 
        
        return True
        
        #del self.commands[0]
        
    def left(self, angle):   
        if angle < 0:
            self.angleStepSize = -abs(self.angleStepSize)
        else:
            self.angleStepSize = abs(self.angleStepSize)
            
        self.dest_dir = self.dir + angle
        
        #del self.commands[0]
        # pop off the trigger command and replace with executor
        
        if self.instant_render:
            self.prev_dir = self.dir
            self.dir = self.dest_dir
            self.array[SEMAPHORE1] = 0
        else:
            self.commands.insert(0, [self.__rotate, {}])
            
        return True
        