#Creation of list in square brackets seperated by comma
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(type(numbers)) #prints type of list

#indexing in list 
print(numbers[0]) #element at index 0
print(numbers[1]) #element at index 1
print(numbers[-1]) #element at last index
print(numbers[-2]) #element at last but one index

#checking the length of list
print(len(numbers))
lst = [1,2,3,4,5,6,7,8,9,10]
filist = []
def fi_arry(lst):
    for i in lst:
        if( i % 2 == 0): 
            filist.append(i)
fi_arry(lst)
print(filist)

#In lambda function
lst = [1,2,3,4,5,6,7,8,9,10]  
res = list(filter (lambda i:i % 2 == 0,lst))
print(res)

lst1 = [1,2,3,4,5]
def red_list(lst1):
    s = 0
    for i in lst1:
        s = s + i
    return s
res = red_list(lst1)
print(res)

#In Lambda function using reduce()
from functools import reduce
lst1 = [1,2,3,4,5]
res = reduce(lambda x , y : x + y , lst1)
print(res)