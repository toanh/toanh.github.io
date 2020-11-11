from math import *

class AngeloTurtle:
	def __init__(self):
		self.x = 0
		self.y = 0
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
        self.angleStepSize = 1
		
	def update(self):
        self.prev_x = self.x
        self.prev_y = self.y
        
        # rotate first
        # TODO: improve precision here
        if int(self.dir) != int(self.dest_dir):
            self.dir += self.angleStepSize
            # early return if rotation is not finished yet
            return
        
        angle = radians(self.dir)
        # then move
        if int(self.x) != int(self.dest_x) or int(self.y) != int(self.dest_y)
            self.x = self.prev_x + self.stepSize * cos(angle)
            self.y = self.prev_y + self.stepSize * sin(angle)
            
		return
        
    def forward(self, steps):
        # do math! 
        angle = radians(self.dir)
        
        dx = steps * cos(angle)
        dy = steps * sin(angle)
        
        # set self.dest_x and self.dest_y
        self.dest_x = self.x + dx
        self.dest_y = self.y + dy
        
        
    def right(self, angle):
        self.dest_dir = self.dir + angle
        