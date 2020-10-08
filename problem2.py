#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""

def distance(a,b):
    import math
    c=math.dist(a,b)
    return c

d=round(distance([-3,2.2],[1,2]),3)
print(d)
