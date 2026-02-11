#User defined function
#Types of User defined function
#1.No input and No output function
def add():
    a = 10
    b = 20
    c = a+b
    print(c)
add()

#2.Input and no output function
def add(a,b):
    c = a + b
    print(c)
x = 10
y = 20
add(x,y)

#3.No input and output function
def add():
    a = 10
    b = 20
    c = a + b
    return c
res = add()
print(res)

#4.Input and output function
def add (a,b):
    c = a+b
    return c
x = 10
y = 20 
res = add(x,y)
print(res)

#Power of python
def calc(a,b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    return c , d , e , f
res1 , res2 , res3 , res4 = calc(10,20)
print(res1 , res2 , res3 , res4)

#Docstring
"""This is adding two numbers and displaying"""
print(2+3)
print(__doc__)

#Docstring in function
def greet():
    """This functions displays a greeting message"""
    print("Hello!")
print(greet.__doc__)