from Mover import *


# A class that we don't need anymore that attracts movers with Newton's Gravitational Law.
class Attractor(Mover):
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.G = 1
        self.r = 10
        self.c = color(0, 0, 0, 100) # the color for the inside
        
    
        
    def show(self):
        fill(90, 100, 100, 75)
        stroke(0, 0, 100, 75)
        circle(self.pos.x, self.pos.y, self.r*2)
        noStroke()
        fill(self.c)
        circle(self.pos.x, self.pos.y, 10) # Making a wheel
        
