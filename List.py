#
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