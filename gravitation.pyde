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
# v1.1  - P3D and PeasyCam and gravitation in 3D
# v1.11 - 3-body problem representation when len(movers) = 3
# v1.12 - Making seperate function for applying the force, updating the movers, showing the movers,
# and drawing the 3-body representation


add_library("PeasyCam")
from Mover import *
from Attractor import *
from Repulser import *

def setup():
    noStroke()
    global movers, attractors, cam
    size(1000, 700, P3D)
    #filter(BLUR, 6)
    cam = PeasyCam(this, width/2, height/2, 0, 4000)
    colorMode(HSB, 360, 100, 100, 100)
    # attractors = []
    movers = []
    



def draw():
    global movers, attractors, total
    background(209, 95, 33, 10)
    
    sphereDetail(mouseX/120 + 5)
    
    show_movers()
    apply_mutual_gravitation_force()
    update_movers()    
    draw_three_body_representation()
    draw_3D_axes()
        
    textAlign(RIGHT)
    fill(map(len(movers), 0, 60, 180, 0), 100, 100)
    
    cam.beginHUD()
    text("{} movers".format(len(movers)), width-50, height-50)
    cam.endHUD()
    lights()


# Draws the bounding box
def draw_bounding_box():
    pushMatrix()
    translate(0, 0, -height) # To the back edge!
    fill(0, 0, 100, 15)
    noStroke()
    rectMode(CENTER)
    rect(
    popMatrix()

# Draws the y, x, and z axes
def draw_3D_axes():
    # line doesn't work in 3D, so we have to use thin boxes.
    strokeWeight(1)
    stroke(86, 89, 86)
    line(0, 0, 0, 0, -40000, 0) # y-axis
    stroke(86, 89, 86, 30)
    line(0, 0, 0, 0, 40000, 0)
    stroke(5, 84, 90)
    line(0, 0, 0, 40000, 0, 0) # x-axis
    stroke(5, 84, 90, 30)
    line(0, 0, 0, -40000, 0, 0)
    stroke(212, 84, 90)
    line(0, 0, 0, 0, 0, 40000) # z-axis
    stroke(212, 84, 90, 30)
    line(0, 0, 0, 0, 0, -40000)
    

# This method isn't needed anymore because there is no glow.
def draw_saved_movers():
    # saved_movers keeps track of what needs to be drawn last. For example, in 2D the normal
    # movers need to be kept in saved_movers because they'll be drawn last. Since glow isn't there
    # anymore, we don't need saved_movers.
    # saved_movers = []   
    for saved_mover in saved_movers:
        saved_mover.show()
        saved_mover.glow()
        saved_mover.showArrow()
        saved_mover.update()
        saved_mover.check_edges()


# For drawing a triangle for the 3-body problem
def draw_three_body_representation():
    if len(movers) == 3:
        # If we don't fill, we won't see the triangle.
        fill(0, 0, 100, 15)
        beginShape()
        # The vertex for movers[0] below, the first vertex of the triangle
        vertex(movers[0].pos.x, movers[0].pos.y, movers[0].pos.z)
        # The vertex for movers[1] below, the second vertex of the triangle
        vertex(movers[1].pos.x, movers[1].pos.y, movers[1].pos.z)
        # The vertex for movers[2] below, the third vertex of the triangle
        vertex(movers[2].pos.x, movers[2].pos.y, movers[2].pos.z)
        endShape()


# Applies mutual gravitation force
def apply_mutual_gravitation_force():
    global movers
    for i in range(len(movers)):
        for j in range(len(movers)):
            if j != i:
                movers[j].apply_force(movers[i].attract(movers[j]))

                
# Shows the movers
def show_movers():
    global movers
    for i in range(len(movers)):

        movers[i].show()
        movers[i].showArrow()
            
        
# Updates the movers
def update_movers():
    global movers
    for i in range(len(movers)):
        movers[i].update()
        movers[i].check_edges()        



def path_trace_in_2D():
    fill(0, 3)
    fill(209, 95, 33, 10)
    rectMode(CORNER)
    rect(0, 0, width, height)

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
            movers.append(Mover(random(-width, width), random(-height, height), random(-height, height)))
            
            

        
    
        
    
