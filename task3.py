#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""
def perimeter(x):
    b=0
    for i in x:
        b=b+i
    return b

c=perimeter([1,15,16])
print(c)
