# MAP FUNCTION

# Let's say you have a list of data (a list or tuple):
# Data: a, b, c,...

# And, let's say you have a function you want to apply to each piece of that data
# Function: f

# With the map function, you specify the function, then the data you want to iterate over
# map(f, data):

# The map function then returns an iterator over the collection of f applied to
# each piece of data
# f(a), f(b), f(c),...

######################################################################################

# EXAMPLE:

# Let's say we have a function that computes the area of a circle with radius "r"

import math


def area(r):
    return math.pi * (r**2)


radii = [2, 5, 7.1, 0.3, 10]

# So, how would we apply this function to the entire list?

# Method 1: make an empty list and use a for loop to go through the radii

areas = []

for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

# Method 2: use the 'map' function

map(area, radii)

# This returns a map object, which will need to be converted to a list using list()

print(list(map(area, radii)))

######################################################################################

# EXAMPLE
# Take a list of cities and temps in C and convert them to F

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Tokyo", 27)]


def c_to_f(data): return (data[0], (9/5)*data[1] + 32)


print(list(map(c_to_f, temps)))
