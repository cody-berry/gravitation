# 2021.08.17 Cody
# Mutual Gravitation In 2D
# Based on Daniel Shiffman's Nature Of Code series for gravitational attraction
# v0.01  - movers with velocity, acceleration, position, show, update, apply_force
# bounce off of walls
# v0.02  - attractor
# v0.02  - draw force vector
# v0.0   - walls exert repulsion force
# v0.0   - make each mover a random color
# v0.0   - mutual gravitation
# v0.0   - path tracing
# v0.0   - flash balls

from Mover import *
from Attractor import *

def setup():
    global movers, attractors
    size(800, 600)
    colorMode(HSB, 360, 100, 100, 100)
    attractors = []
    movers = []
    frameRate(30)
    for i in range(10):
        movers.append(Mover(random(70, width-70), random(70, height-70)))

def draw():
    global movers, attractors
    background(210, 100, 30, 100)
    
    #gravity = PVector(0, 9.8/frameRate)
    #wind = PVector(random(-1, 1), random(-1, 1))
    for attractor in attractors:
        attractor.show()
        for mover in movers:
            attractor.attract(mover)
            mover.show()
            mover.update()
            # mover.check_edges()
            
def mousePressed():
    global attractors
    attractors.append(Attractor(mouseX, mouseY, random(1, 3)))            
