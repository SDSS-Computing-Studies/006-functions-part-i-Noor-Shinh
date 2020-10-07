#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""
def largest(l):
    l.sort()
    x=(l[-1])
    return x

y=largest([1,15,88,2])
print(y)

c=largest([15,99,2])
print(c)
