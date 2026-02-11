#Shallow Copy
lst = [ 1 , 2 , 3 , 4 , 5]
lst1 = lst [:]
print(id(lst))
print(id(lst1))
lst1.append(99)
print(lst1)
print(lst)
lst1[2] = 33
print(lst1)
print(lst)

a = [[1,2] , [3,4]]
b = a [:]
print(id(a))
print(id(b))
b.append(99)
print(b)
print(a)
b[1][0] = 33
print(b)
print(a)

#Deep Copy
import copy
a1 = [[1,2],[3,4]]
b1 = copy.deepcopy(a1)
print(b1)
print(a1)
print(id(a1))
print(id(b1))
