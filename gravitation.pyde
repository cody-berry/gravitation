# 2021.08.17 Cody
# Mutual Gravitation In 2D
# Based on Daniel Shiffman's Nature Of Code series for gravitational attraction
# v0.0  - movers with velocity, acceleration, position, show, update, apply_force
# v0.0  - bounce off of walls!
# v0.0  - draw force vector
# v0.0  - walls exert repulsion force
# v0.0  - attractor
# v0.0  - make each mover a random color
# v0.0  - mutual gravitation
# v0.0  - path tracing
# v0.0  - flash balls

from Mover import *


def setup():
    global mover
    size(800, 600)
    colorMode(HSB, 360, 100, 100, 100)
    mover = Mover(random(width), random(height))

def draw():
    global mover
    background(210, 100, 30, 100)
    gravity = PVector(0, 9.8/frameRate)
    wind = PVector(random(-10, 10), random(-10, 10))
    mover.show()
    mover.apply_force(gravity)
    mover.update()
