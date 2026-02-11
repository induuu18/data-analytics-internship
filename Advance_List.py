#List 
lst = [[1,2,3] , (4,5,6) , {7 , 8 , 9 } , {'A':10 , 'B' : 20 }]
print(lst[1][0])
print(lst[1][1])
print(lst[2].pop()) 

#List Slicing
lst = [1,2,3,4,56,7,8,9,10]
print(lst[2:7])
print(lst[:6])
print(lst[2:])
print(lst[1::2])

#List Indexing
L = [1,2,3,0,4]
L[3] = 33 #or L.insert(3,33)
print(L)
L.extend([5,6,7]) #Extend() adds multiple elements to the existing list
print(L)
a = [1,2,3,4,5,6,7,8,9,10]
del a[6:9]
print(a)

#Remove elements
l = [10,20,30,40]
del l[2:]
print(l)
l.pop()
print(l)
l.remove(10)
print(l)

#Add list in between the existing list using slicing
A = [1,2,3,4]
s1 = A[0:2]
s2 = A[2:]
print(s1)
print(s2)
B = [11,12,13]
Li = s1 + B + s2
print(Li)

#Replicate a list 10 times
C = [1,2,3]
rep = C * 10
print(rep)

# Copy a list in 2 ways - 2 Approaches
# Using Append
A1 = [1,2,3,4,5]
B1 = A1[0:]
print(B1)
print(id(A1))
print(id(B1))

#Using typecasting
A1 = [1,2,3,4,5]
B1 = list([A1])
print(id(A1))
print(id(B1))