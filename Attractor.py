from Mover import *

class Attractor:
    def __init__(self, x, y, gravitational_constant):
        self.pos = PVector(x, y)
        self.G = gravitational_constant
        self.r = 70
        
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
        strength = constrain(self.G/dist(self.pos.x, self.pos.y, 
                            mover.pos.x, mover.pos.y),
                            8, 9)
        
        force.setMag(strength)
        
        mover.apply_force(force)
        
    def show(self):
        fill(0, 0, 100, 75)
        circle(self.pos.x, self.pos.y, self.r*2)
        
