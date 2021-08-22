# 2021.08.17 Cody
# Mutual Gravitation In 2D
# Based on Daniel Shiffman's Nature Of Code series for gravitational attraction
# v0:
# v0.1  - movers with velocity, acceleration, position, show, update, apply_force
# bounce off of walls
# v0.2  - attractor
# v0.3  - repulsor
# v0.4  - mutual gravitation
# v0.41 - draw force vector
# v0.5  - path tracing
# v0.51 - flash balls
# v1:
# v1.   - P3D and PeasyCam
# v1.   - gravitation in 3D
# v1.   - 


add_library("PeasyCam")
from Mover import *
from Attractor import *
from Repulser import *

def setup():
    noStroke()
    global movers, attractors, cam
    size(1000, 700, P3D)
    #filter(BLUR, 6)
    cam = PeasyCam(this, width/2, height/2, 0, 1000)
    colorMode(HSB, 360, 100, 100, 100)
    attractors = []
    movers = []



def draw():
    global movers, attractors
    background(209, 95, 33, 10)
    # fill(0, 3)
    # fill(209, 95, 33, 10)
    # rectMode(CORNER)
    # rect(0, 0, width, height)
    
    # saved_movers keeps track of what needs to be drawn last. For example, in 2D the normal
    # movers need to be kept in saved_movers because they'll be drawn last.
    saved_movers = []   
    
    
    
    total = 0
    
    for i in range(len(movers)):
        for j in range(len(movers)):
            if j != i:
                movers[j].apply_force(movers[i].attract(movers[j]))
        if movers[i].flash == False:
            total += 1
            movers[i].show()
            movers[i].showArrow()
        else:
            total += 8
            saved_movers.append(movers[i])
            
        movers[i].update()
        # movers[i].check_edges()
        
    # for saved_mover in saved_movers:
    #     saved_mover.show()
    #     saved_mover.glow()
    #     saved_mover.showArrow()
    #     saved_mover.update()
    #     saved_mover.check_edges()
        
        
        
    fill(map(total, 0, 60, 180, 0), 100, 100)
    text(str(total) + "movers", width-50, height-50)
    lights()


# This function does gravitation with attractors.
def attractor_gravitation():
    global movers, attractors
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
            
def keyPressed():
    global attractors, movers
    # if mouseButton == LEFT:
    #     attractors.append(Attractor(mouseX, mouseY, random(1, 3)))  
    # if mouseButton == RIGHT:
    #     attractors.append(Repulser(mouseX, mouseY, random(1, 3)))
    if key == "a":
        for i in range(1): 
            movers.append(Mover(random(width), random(height), random(height)))
    if key == "g":
        for mover in movers:
            if dist(mover.pos.x, mover.pos.y, mouseX, mouseY) < mover.r:
                mover.flash = not mover.flash
        
    
        
    
