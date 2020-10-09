#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""

import math 

def distance(a,b):
    x=(a[0]-b[0])
    x=math.pow(x,2)
    y=(a[1]-b[1])
    y=math.pow(y,2)
    z=(x+y)
    z=math.sqrt(z)
    return z

d=round(distance([-3,2.2],[1,2]),3)
print(d)
