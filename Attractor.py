from Mover import *

class Attractor:
    def __init__(self, x, y, gravitational_constant):
        self.pos = PVector(x, y)
        self.G = gravitational_constant
        self.r = 10
        self.c = color(0, 0, 0, 100) # the color for the inside
        
    
        
    def show(self):
        fill(90, 100, 100, 75)
        stroke(0, 0, 100, 75)
        circle(self.pos.x, self.pos.y, self.r*2)
        noStroke()
        fill(self.c)
        circle(self.pos.x, self.pos.y, 10) # Making a wheel
        
