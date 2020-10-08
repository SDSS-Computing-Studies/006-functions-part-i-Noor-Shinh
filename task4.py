#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""
import math
def isInteger(x):
    b=math.floor(x)
    if b==x:
        print("is an integer")
    else:
        print("not an integer")
