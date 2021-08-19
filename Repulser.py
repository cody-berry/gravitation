from Attractor import *

class Repulser(Attractor):
    # We don't need a constructer because if we did, then it would be the exact
    # same. Python allows us to not contain a constructer if it is the exact
    # same as the class's constructer that it is 'inheriting' from.
    def show(self):
        # The difference here is that we're filling red, not green.
        fill(0, 100, 100, 75)
        circle(self.pos.x, self.pos.y, self.r*2)
        fill(self.c)
        circle(self.pos.x, self.pos.y, 10)
        
    def attract(self, mover):
        # Repulsing is the opposite of attracting.
        return -1*Attractor.attract(Attractor(self.pos.x, self.pos.y, self.G), 
                                    # how it would be to be an attractor with the
                                    # same arguments as the arguments passed into
                                    # self, this class
                                    mover)
        
