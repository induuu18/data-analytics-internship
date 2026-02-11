#Lambda Function example
res=(lambda num,power : num ** power )(5,2)
print(res)

#To excecute multiple times
add = (lambda a , b : a + b)
print(add(10,20))
print(add(20,500))

#Filter function
lst = [1,2,3,4,5,6,7,8,9,10]  
res = list(filter (lambda i:i % 2 == 0,lst))
print(res)

#Map function
lst = [5,6,7,8,9,10]
res = list(map(lambda i : i*2 , lst))
print(res)

#Reduce function (must import functools)
from functools import reduce
lst1 = [1,2,3,4,5]
res = reduce(lambda x , y : x + y , lst1) #in def function we use two iterable variables s and i , similarly in lambda function x and y is used one to store sum and another to iterate
print(res)

# 09/02/2026
# Tripler
def tripler(n):
    return lambda x : x*n
res = tripler(3)
print(res(5))

# Write a funciton which takes input from user and print table
# Using lambda function
def table(n):
    return lambda x : x*n
a = int(input('Enter the number :'))
res = table(a)
for i in range(1,11):
    # print(res(i))
    print(a,'x', i ,'=',res(i))
#Usind def function
def table(n):
    for i in range(1,11):
        print(i*n)
a = int(input('Enter the number:'))
table(a)

#NOTE - Using lambda function , we can write a function returning a function as a output
