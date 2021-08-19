# 2021.08.17 Cody
# Mutual Gravitation In 2D
# Based on Daniel Shiffman's Nature Of Code series for gravitational attraction
# v0.01  - movers with velocity, acceleration, position, show, update, apply_force
# bounce off of walls
# v0.02  - attractor
# v0.0   - repulser
# v0.0   - draw force vector
# v0.0   - walls exert repulsion force
# v0.0   - make each mover a random color
# v0.0   - mutual gravitation
# v0.0   - path tracing
# v0.0   - flash balls

from Mover import *
from Attractor import *
from Repulser import *

def setup():
    global movers, attractors
    size(1500, 800)
    colorMode(HSB, 360, 100, 100, 100)
    attractors = []
    movers = []

def draw():
    global movers, attractors
    background(210, 100, 30, 100)
    
    #gravity = PVector(0, 9.8/frameRate)
    #wind = PVector(random(-1, 1), random(-1, 1))
    # If we nest the mover for loop inside the attractor for loop, there isn't going
    # to be any movers shown. Luckily, we have 0 movers to start with, so it doesn't
    # matter. 
    for attractor in attractors:
        attractor.show()
    
    for mover in movers:
        for attractor in attractors:
            mover.apply_force(attractor.attract(mover))
        mover.show()
        mover.update()
        mover.check_edges()
            
            
def mousePressed():
    global attractors, mover
    if mouseButton == LEFT:
        attractors.append(Attractor(mouseX, mouseY, random(1, 3)))  
    if mouseButton == RIGHT:
        attractors.append(Repulser(mouseX, mouseY, random(1, 3)))
    for i in range(3): 
        movers.append(Mover(mouseX, mouseY))
