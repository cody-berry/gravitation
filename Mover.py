

class Mover(object):
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector.random2D().mult(random(10, 15))
        self.acc = PVector(0, 0)
        self.r = 16
        
    
    # If we don't do this, how are we going to see where the movers are?
    def show(self): 
        fill(0, 0, 100, 50)
        stroke(0, 0, 100, 50)
        circle(self.pos.x, self.pos.y, self.r*2)
        
        
    def apply_force(self, force): # force is the force we're going to apply
        # mass = 1, and a = F/m, so a = F.
        self.acc.add(force)
        
    
    # If we don't do this, we'll never see the movers move, if we call the show
    # function.
    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc = PVector(0, 0)
        
    
   
    def check_edges(self):
        # vertical edges
        # right edge
        if self.pos.x + self.r > width:
            self.pos.x = width - self.r
            self.vel.x *= -1
        # left edge
        if self.pos.x - self.r < 0:
            self.pos.x = self.r
            self.vel.x *= -1
        
        # horizontal edges
        # bottom edge
        if self.pos.y + self.r > height:
            self.pos.y = height - self.r
            self.vel.y *= -1
        # top edge
        if self.pos.y - self.r < 0:
            self.pos.y = self.r
            self.vel.y *= -1
            
    
