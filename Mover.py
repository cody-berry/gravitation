

# Mover is a sphere that gravitates along other movers or attractors.
class Mover(object):
    def __init__(self, x, y, z):
        self.pos = PVector(x, y, z)
        self.vel = PVector(0, 0, 0)
        self.acc = PVector(0, 0, 0)
        self.m = random(3, 8)
        self.r = self.m*2
        self.G = random(1, 3)
        self.flash = False # This is whether or not we wanna call glow or show.
        
    
    # If we don't do this, how are we going to see where the movers are?
    def show(self): 
        fill(0, 0, 100, 50)
        # blendMode(DIFFERENCE)
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        sphere(self.r*2)
        popMatrix()
        
        
    def showArrow(self):
        fill(0, 0, 0, 0)
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotate(self.acc.heading())
        line(0, 
             0, 
             self.acc.mag()*6,
             0)
        line(self.acc.mag()*6,
             0, 
             self.acc.mag()*6 - 3,
             -3)
        line(self.acc.mag()*6,
             0,
             self.acc.mag()*6 - 3,
             3)
        popMatrix()
    
    
    def apply_force(self, force): # force is the force we're going to apply
        # mass = 1, and a = F/m, so a = F.
        fill(0, 0, 0, 100)
        self.acc.add(PVector.div(force, self.m))
        
    
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
        if self.pos.x - self.r < -width:
            self.pos.x = -width + self.r
            self.vel.x *= -1
        
        # horizontal edges
        # bottom edge
        if self.pos.y + self.r > height:
            self.pos.y = height - self.r
            self.vel.y *= -1
        # top edge
        if self.pos.y - self.r < -height:
            self.pos.y = -height + self.r
            self.vel.y *= -1
            
        # back edge
        if self.pos.z - self.r < -height:
            self.pos.z = -height + self.r
            self.vel.z *= -1
        
        # front edge
        if self.pos.z + self.r > height:
            self.pos.z = height - self.r
            self.vel.z *= -1
            
    
    # for mutual gravitation        
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
            
    
