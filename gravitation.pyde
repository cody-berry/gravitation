# 2021.08.17 Cody
# Mutual Gravitation In 2D
# Based on Daniel Shiffman's Nature Of Code series for gravitational attraction
# v0.0:
# v0.01  - movers with velocity, acceleration, position, show, update, apply_force
# bounce off of walls
# v0.02  - attractor
# v0.03  - repulsor
# v0.04  - mutual gravitation
# v0.041 - draw force vector
# v0.05  - path tracing
# v0.051 - flash balls
# v0.1:
# v0.1   - P3D and PeasyCam
# v0.1   - gravitation in 3D
# v0.1   - 

from Mover import *
from Attractor import *
from Repulser import *

def setup():
    global movers, attractors
    size(1500, 1000)
    filter(BLUR, 6)
    stroke(5)
    background(209, 95, 33, 10)
    colorMode(HSB, 360, 100, 100, 100)
    attractors = []
    movers = []



def draw():
    global movers, attractors
    
    fill(0, 3)
    fill(209, 95, 33, 10)
    rectMode(CORNER)
    rect(0, 0, width, height)
    saved_movers = [] 
    
    
    #gravity = PVector(0, 9.8/frameRate)
    #wind = PVector(random(-1, 1), random(-1, 1))
    # If we nest the mover for loop inside the attractor for loop, there isn't going
    # to be any movers shown. Luckily, we have 0 movers to start with, so it doesn't
    # matter. 
    # for attractor in attractors:
    #     attractor.show()
    
    # for mover in movers:
    #     for attractor in attractors:
    #         mover.apply_force(attractor.attract(mover))
    #     mover.show()
    #     mover.update()
    #     mover.check_edges()
    
    for i in range(len(movers)):
        for j in range(len(movers)):
            if j != i:
                movers[j].apply_force(movers[i].attract(movers[j]))
        if movers[i].flash == False:
            saved_movers.append(movers[i])
        else:
            movers[i].showArrow()
            movers[i].glow()
        movers[i].update()
        # movers[i].check_edges()
        
    for saved_mover in saved_movers:
        saved_mover.show()
        saved_mover.showArrow()
        saved_mover.update()
        # saved_mover.check_edges()
        
        
        
    fill(map(len(movers), 0, 60, 180, 0), 100, 100)
    text(len(movers), width-50, height-50)
    

                
            
def mousePressed():
    global attractors, movers
    # if mouseButton == LEFT:
    #     attractors.append(Attractor(mouseX, mouseY, random(1, 3)))  
    # if mouseButton == RIGHT:
    #     attractors.append(Repulser(mouseX, mouseY, random(1, 3)))
    if mouseButton == LEFT:
        for i in range(1): 
            movers.append(Mover(random(width/1.5), random(height/1.25)))
    else:
        for mover in movers:
            if dist(mover.pos.x, mover.pos.y, mouseX, mouseY) < mover.r:
                mover.flash = not mover.flash
        
    
        
    
