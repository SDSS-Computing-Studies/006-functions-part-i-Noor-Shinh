#!python3

def sum(a,b):
    #inputs
    # a : float 
    # b : float
    # return value: returns the sum of the 2 numbers
    x=(a+b)
    return x
    


#this should return a value of 7
x = sum(3,4)
print(x)
#this should return a value of 12.5
y = sum(11,1.5)
print(y)

a=float(input("Enter a number"))
b=float(input("Enter a number"))

c=sum(a,b)
print(c)
