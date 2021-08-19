from Mover import *

class Attractor:
    def __init__(self, x, y, gravitational_constant):
        self.pos = PVector(x, y)
        self.G = gravitational_constant
        self.r = 10
        self.c = color(0, 0, 0, 100) # the color for the inside
        
    def attract(self, mover):
        # Newton's Gravitational Law says that gravity is equal to the mass'a the
        # two objects, and in this case, one of them is 1, the mover, and another 
        # one is the attractor, so both 1, and then divided by the distance between
        # the 2 objects. Also times teh gravitational constant.
        
        force = PVector.sub(self.pos, mover.pos)
        
        # the first argument of the constrain is the gravitational formula. I
        # had to assume that both of the masses were 1, so I placed self.G on the
        # numerator. The second and third arguments are just the range. I decided
        # on a very short one.
        if dist(self.pos.x, self.pos.y, mover.pos.x, mover.pos.y) != 0:
            strength = constrain(self.G/dist(self.pos.x, self.pos.y, 
                                 mover.pos.x, mover.pos.y),
                                 1, 2)
            force.setMag(strength)
        else: # to avoid getting aZeroDivisionError
            force.setMag(0) # To make the force in a random direction
            force.setMag(2) # To make the force have the appropriate strength
        
        return force # We have repulser, and it's simply the oppisite. 
        
    def show(self):
        fill(90, 100, 100, 75)
        stroke(0, 0, 100, 75)
        circle(self.pos.x, self.pos.y, self.r*2)
        noStroke()
        fill(self.c)
        circle(self.pos.x, self.pos.y, 10) # Making a wheel
        
