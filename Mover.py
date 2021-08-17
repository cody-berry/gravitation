

class Mover(object):
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.r = 16
        
    def show(self): # If we don't do this, how are we going to see where the movers
        # are?
        fill(0, 0, 100, 50)
        circle(self.pos.x, self.pos.y, self.r)
        
    def apply_force(self, force): # force is the force we're going to apply
        # mass = 1, and a = F/m, so a = F.
        self.acc.add(force)
        
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc = PVector(0, 0)
    
