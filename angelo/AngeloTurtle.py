from math import *

class AngeloTurtle: 
    def update(self):
        if len(self.commands) > 0:
            command = self.commands[0]
            #print("executing: ", str(command))
            command[0](**command[1])
        return
        
    def __init__(self):
        self.x = 200
        self.y = 250
        self.dir = 0
        self.visible = True
        self.trail = True
        
        self.dest_x = self.x
        self.dest_y = self.y
        
        # the absolute angle in degrees
        self.dest_dir = self.dir
        
        self.prev_x = self.x
        self.prev_y = self.y
        
        self.stepSize = 1
        self.angleStepSize = 5
        
        self.commands = []
        
        
    def __rotate(self):
        self.dir += self.angleStepSize
        # rotate first
        # TODO: improve precision here
        if abs(self.dir - self.dest_dir) < 0.1:
            # have I reached my destination
            # pop off commands
            self.dir = self.dest_dir
            del self.commands[0]
            
    def __move(self):
        #print("executing move command", len(self.commands))
        self.prev_x = self.x
        self.prev_y = self.y
        
        angle = radians(self.dir)
        
        self.x = self.prev_x + self.stepSize * cos(angle)
        self.y = self.prev_y + self.stepSize * sin(angle)
            
        if abs(self.x - self.dest_x) < 0.5 and abs(self.y - self.dest_y) < 0.5:
            # have I reached my destination
            # pop off commands
            self.x = self.dest_x
            self.y = self.dest_y
            #print("done move", len(self.commands))
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
        
        
    def left(self, angle):
        self.dest_dir = self.dir + angle
        
        del self.commands[0]
        # pop off the trigger command and replace with executor
        self.commands.insert(0, [self.__rotate, {}])
        