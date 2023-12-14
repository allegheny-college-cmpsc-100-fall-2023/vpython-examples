from vpython import * # import vpython

xs = range(10) # list with range 10

doubles = list(map(lambda x: x * 2, xs)) #writes doubles of list xs list to doubles

# funciton that draws a sphere with x position argument
# NOTE: this does not work in trinket.io
def sphere_x(x):
    return sphere(pos = vector(x, 0, 0)) 

# list of spheres with x position of doubles
balls = list(map(sphere_x, doubles))