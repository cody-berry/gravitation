# 2021.08.17 Cody
# Mutual Gravitation In 2D
# Based on Daniel Shiffman's Nature Of Code series for gravitational attraction
# v0.0  - movers with velocity, acceleration, position, show, update
# v0.0  - bounce off of walls!
# v0.0  - apply_force
# v0.0  - walls exert repulsion force
# v0.0  - attractor
# v0.0  - make each mover a random color
# v0.0  - mutual gravitation
# v0.0  - path tracing
# v0.0  - flash balls

def setup():
    size(800, 600)
    colorMode(HSB, 360, 100, 100, 100)

def draw():
    background(210, 100, 30, 100)
