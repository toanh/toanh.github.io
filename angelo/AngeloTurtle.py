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
        
        self.dest_x = self.x
        self.dest_y = self.y
        
        # the absolute angle in degrees
        self.dest_dir = self.dir
        
        self.prev_x = self.x
        self.prev_y = self.y
        
        self.stepSize = 3
        self.angleStepSize = 10
        
        self.commands = []
        
        if "turtle" in document:        
            document["turtle"].remove()
        
        self.width = 500
        self.height = 400
        self.canvas = html.CANVAS(width = self.width, height = self.height, id="turtle")

        self.canvas.style= {"z-index": 2, "position": "absolute", "left":"0px", "right":"0px", "background-position": "center"}
        self.ctx = self.canvas.getContext('2d');
        self.ctx.fillStyle= "rgba(0,0,0,0)"
        self.ctx.fillRect(0, 0, self.width, self.height)    

        outputBox = document["outputBox"] 
        outputBox <= self.canvas
        
        self.array = None
        
    def set_shared_memory(self, array):
    
        print("setting shared memory!", array)
        # shared memory
        self.array = array
        
        self.array[SEMAPHORE1] = 0
        
    def update(self):
        if len(self.commands) > 0:
            command = self.commands[0]
            #print("executing: ", str(command))
            command[0](**command[1])
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
        
    def draw(self):
        if self.trail:
            self.__drawLine(self.prev_x, self.prev_y, self.x, self.y)
        
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
            del self.commands[0]
            
    def __move(self):
        #print("executing move command", len(self.commands))
        self.prev_x = self.x
        self.prev_y = self.y
        
        angle = radians(self.dir)
        
        self.x = self.prev_x + self.stepSize * cos(angle)
        self.y = self.prev_y + self.stepSize * sin(angle)
        
        # check for overshoot
        # TODO: fix! Doesn't work for all step sizes, check and/or and <= >= logic
        if (self.dest_x - self.x) * (self.dest_x - self.prev_x) < 0 or (self.dest_y - self.y) * (self.dest_y - self.prev_y) < 0:
            #if abs(self.x - self.dest_x) < 0.5 and abs(self.y - self.dest_y) < 0.5:
            # have I reached my destination
            # pop off commands
            self.x = self.dest_x
            self.y = self.dest_y
            #print("done move", len(self.commands))
            self.array[SEMAPHORE1] = 0
            del self.commands[0]
            
    def receiveCommand(self, command):
        #print("receiving forward", len(self.commands))
        self.commands.insert(len(self.commands),command)
        #print("added forward trigger", len(self.commands))
    
    def forward(self, steps):
        # do math! 
        #print("executing forward trigger", len(self.commands))
        angle = radians(self.dir)
        
        dx = steps * cos(angle)
        dy = steps * sin(angle)
        
        # set self.dest_x and self.dest_y
        self.dest_x = self.x + dx
        self.dest_y = self.y + dy
        
        # pop off the trigger command and replace with executor
        del self.commands[0]
        #print("deleting forward trigger", len(self.commands))
        
        self.commands.insert(0, [self.__move, {}])
        #print("added move command", len(self.commands))
        
        
    def clear(self, r, g, b, a):
        self.ctx.clearRect(0, 0, self.width, self.height)
        
        self.ctx.fillStyle= "rgba(" + str(int(r * 255.0)) + "," + str(int(g * 255.0)) + "," + str(int(b * 255.0)) + "," + str(int(a * 255.0))+ ")"        
        self.ctx.fillRect(0, 0, self.width, self.height) 
        
        del self.commands[0]
        
    def left(self, angle):       
        self.dest_dir = self.dir + angle
        
        del self.commands[0]
        # pop off the trigger command and replace with executor
        self.commands.insert(0, [self.__rotate, {}])
        