import numpy as np
# # print(np.__version__)

# import numpy as np
# import sys
# lst = [10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,80,90,100,200,200,300]
# arr = np.array(lst)
# print(lst)
# print(arr)
# #List vs Array Size difference
# print("The size of the list is",sys.getsizeof(lst),bytes)
# print("The size of the array list is",sys.getsizeof(arr),bytes)
# #List vs Array Size difference
# print("The size of the list is",sys.getsizeof(lst)+sum(sys.getsizeof(i)for i in lst),bytes)
# print("The size of the array list is",sys.getsizeof(arr),bytes)

# lst = [10,20,30,40,50]
# myarr = np.array(lst)
# print(myarr)
# print(myarr.size)
# print(myarr.shape)
# print(myarr.dtype)
# print(myarr.ndim)

# #Creation of Array
# print(np.arange(10,101,10))

# arr = np.array([10,20,30,40,50],dtype="float")
# print(arr)

# arr1 = np.array([99,98,97,96,95],dtype="bool") #Similarly with int
# print(arr1)

#linspace function
# print(np.linspace(0,1,5))
# arr = np.linspace(0,1,endpoint=False,retstep=True)
# print(arr)

# zarr = np.zeros(10)
# zarr1 = np.zeros([3,3])
# zarr2 = np.zeros([3,3,2])
# print(zarr)
# print(zarr1)
# print(zarr2)

# arr1 = np.full(10,fill_value=0)
# print(arr1)


#Random() , randint() functions
# a = np.random.randint(10)
# print(a)
# b = np.random.randint(10,100)
# print(b)
# arr1 = np.random.randint(10,100,(2,3))
# print(arr1)
# arr2 = np.random.randint(10,100,(2,3),dtype="int8")
# print(arr2)
# print(arr1.dtype)
# print(arr2.dtype)

#eye() function
# ay = np.eye(5,5,k=-1,dtype='int')
# print(ay)

#identity() function
# arr = np.identity(5)
# print(arr)

#Diagonal()
# arr = np.array([10, 20, 30, 40, 50])
# arr2 = np.array([[10, 20], [30, 40], [50, 60]])

# print(arr)

# rarr1 = np.diag(arr, k=2)
# print(rarr1)

# rarr2 = np.diag(arr2)
# print(arr2)
# print('rarr2', rarr2)

# rarr2 = np.diag(arr2, k=1)
# print(rarr2)

# rarr2 = np.diag(arr2, k=-1)
# print(rarr2)

#reshape() function
# arr = np.arange(10,100,10)
# narr = np.reshape(arr,(3,3))
# print(narr)

#All inbuilt methods in one single block of code
# import numpy as np
# import sys

# arr = np.arange(1, 11)
# print("arange:", arr)
# print("getsizeof:", sys.getsizeof(arr))
# print("size:", arr.size)
# print("shape:", arr.shape)
# print("dtype:", arr.dtype)
# print("ndim:", arr.ndim)
# print("linspace:", np.linspace(0,1,5))
# print("zeros:\n", np.zeros((2,3)))
# print("ones:\n", np.ones((2,2)))
# print("full:\n", np.full((2,2), 9))
# print("random:\n", np.random.random((2,3)))
# print("randint:\n", np.random.randint(10,50,(2,3)))
# print("astype float:", arr.astype(float))
# print("eye:\n", np.eye(3))
# print("identity:\n", np.identity(3))
# reshaped = arr.reshape(5,2)
# print("Reshaped (5x2):\n", reshaped)
# arr1 = np.arange(1, 13)
# print("Original array:", arr1)

#rand()
# import numpy as np
# arr = np.random.rand()
# print(arr)

# arr1 = np.random.rand(10)
# print(arr1)

# arr2 = np.random.rand(2,3)
# print(arr2)

# arr3 = np.random.rand(3,2,3)
# print(arr3)

#randn()
# arr4 = np.random.randn()
# print(arr4)

# arr5 = np.random.randn(10)
# print(arr5)

# arr6 = np.random.randn(2,3)
# print(arr6)

# arr7 = np.random.randn(3,2,3)
# print(arr7)

#uniform function
# a = np.random.uniform()
# print(a)

# a1 = np.random.uniform(-1,3,size=(2,3))
# print(a1)

# ar = np.random.normal(size=10)
# print(ar)

#shuffle function
# ar = np.arange(1,19).reshape(3,2,3)
# print(ar)
# print("before shuffle\n",ar)
# np.random.shuffle(ar)
# print("after shuffle\n",ar)

#view() function - shallow copy1
# brr = np.arange(1,39)
# vrr = brr.view()
# print(brr)
# print(vrr)
# vrr[0] = 99
# print("Copy array:",vrr)
# print("Og array:",brr)

# #copy() function - Deep copy
# brr = np.arange(1,39)
# vrr = brr.copy()
# print(brr)
# print(vrr)
# vrr[0] = 99
# print("Copy array:",vrr)
# print("Og array:",brr)

#datatypes
# r = np.arange(1,10)
# print(f"Original array:{r}")
# c = np.float32(r)
# print(c)
# c = np.bool_(r)
# print(c)

#Iterate elements in array using for loop
#1D array
# arr = np.arange(1,17)
# print(arr)
# for i in arr:
#     print(i)

#2D array
# arr1 = np.arange(1,21).reshape(5,4)
# print(arr1)
# for i in arr1:
#     for j in i:
#         print(j)

#3D array 
# arr2 = np.arange(1,17).reshape(2,2,4)
# print(arr2)
# for i in arr2:
#     for j in i:
#         for k in j:
#             print(k)

# #nditer function
# arr=np.arange(1,25).reshape(2,3,4)
# for i in np.nditer(arr):
#     print(i)

# #ndenumerate function 1D
# arr=np.arange(1,10)
# print(arr)
# for i,j in np.ndenumerate(arr):
#     print(f"The element{j} is present at position{i}")

# # ndenumerate function 2D
# arr=np.arange(1,25).reshape(8,3)
# print(arr)
# for i,j in np.ndenumerate(arr):
#     print(f"The element{j} is present at position{i}")

# # ndenumerate function 3D
# arr=np.arange(1,25).reshape(2,3,4)
# print(arr)
# for i,j in np.ndenumerate(arr):
#     print(f"The element{j} is present at position{i}")

# #arithematic operations in arrays
# arr=np.arange(1,10).reshape(3,3)
# print(f"Addition of arr+2:\n{arr+2}")
# print(f"Subtraction of arr-2:\n{arr-2}")
# print(f"Multiplication of arr*2:\n{arr*2}")
# print(f"division of arr/2:\n{arr/2}")
# print(f"floor division of arr//2:\n{arr//2}")
# print(f"modulus of arr%2:\n{arr%2}")
# print(f"power of arr**2:\n{arr**2}")
# print(f"modulus of arr%2:\n{arr%2}")
# print(f"power of arr**2:\n{arr**2}")

# print(f"n/0 is:\n{arr/0}") # infinite
# arr1=np.array([0,0,0,0,0]) #nan
# print(f"0/0 is:\n {arr1/0}")

# #check size, shape and dim before operations
# arr1=np.arange(1,11)
# arr2=np.arange(1,101,10)
# print(f"he dimension of arr1 is{arr1.ndim}, the shape of arr1 is {arr1.shape}, the size of arr1 is {arr1.size}")
# print(f"he dimension of arr2 is{arr2.ndim}, the shape of arr2 is {arr2.shape}, the size of arr2 is {arr2.size}")
# print(arr1+arr2)

# # 2D Array
# arr1=np.arange(1,11).reshape(2,5)
# arr2=np.arange(1,101,10).reshape(2,5)
# print(f"he dimension of arr1 is{arr1.ndim}, the shape of arr1 is {arr1.shape}, the size of arr1 is {arr1.size}")
# print(f"he dimension of arr2 is{arr2.ndim}, the shape of arr2 is {arr2.shape}, the size of arr2 is {arr2.size}")
# print(arr1+arr2)

# # 3D Array
# arr1=np.arange(1,11).reshape(1,2,5)
# arr2=np.arange(1,101,10).reshape(1,2,5)
# print(f"he dimension of arr1 is{arr1.ndim}, the shape of arr1 is {arr1.shape}, the size of arr1 is {arr1.size}")
# print(f"he dimension of arr2 is{arr2.ndim}, the shape of arr2 is {arr2.shape}, the size of arr2 is {arr2.size}")
# print(arr1+arr2)

#transpose()
#for 1D array
# import numpy as np
# arr1 = np.arange(1,6)
# print(arr1)
# tarr1 = np.transpose(arr1)
# print(tarr1)

# #For 2D array
# arr2 = np.arange(1,10).reshape(3,3)
# print(arr2)
# tarr2 = np.transpose(arr2)
# print(tarr2)

# #For 3D array
# arr3 = np.arange(1,13).reshape(2,2,3)
# print(arr3)
# tarr3 = np.transpose(arr3)
# print(tarr3)

#using axes
# arr4 = np.arange(1,25).reshape(2,3,4)
# print(arr4)
# tarr4 = np.transpose(arr4,axes=(1,2,0))
# print(tarr4)

# arr5 = np.arange(1,121).reshape(4,5,6)
# print(arr5)
# tarr5 = np.transpose(arr5,axes=(1,2,0))
# print(tarr5)

#is it view or copy?
# arr2 = np.arange(1,10).reshape(3,3)
# arr2[2] = 89
# print(arr2)
# tarr2 = np.transpose(arr2)
# print(tarr2)

#swapaxes()
# srr = np.arange(1,61).reshape(3,4,5)
# print(srr)
# sarr = np.swapaxes(srr,2,0)
# sarr[1] = 99 #creates view
# print(sarr)
# print(srr) 

#Joining of n arrays with I arrays (concatentate())
# array1 = np.arange(5)
# array2 = np.arange(1,61,10)
# carr = np.concatenate([array1,array2])
# print(carr)

#Adding three arrays
# arr1 = np.arange(1,4)
# arr2 = np.arange(4,10)
# arr3 = np.arange(100,201,100)
# res = np.concatenate([arr1,arr2,arr3])
# print(res)

# ar1 = np.arange(1,4)
# ar2 = np.arange(4,10)
# ar3 = np.arange(100,201,100)
# emp = np.empty(11)
# res = np.concatenate([ar1,ar2,ar3],out=emp)
# print(res)

# a1 = np.arange(1,13).reshape(2,2,3)
# a2 = np.arange(1,25).reshape(2,3,4)
# ca = np.concatenate((a1,a2),axis=None)
# print(ca)

#stack()
# ar1 = np.array([10,20,30,40])
# ar2 = np.array([50,60,70,80])
# ar3=np.stack((ar1,ar2))
# print(ar3)

#vstack() - only for vertical stacking
# a1 = np.array([['A','B','C'],
#       ['D','E','F']])
# a2=np.array([['G','H','I'],
#              ['J','K','L']])
# a3=np.vstack((a1,a2))
# print(a3)

#hstack - only for horizontal stacking 
# a1 = np.array([['A','B','C'],
#       ['D','E','F']])
# a2=np.array([['G','H','I'],
#              ['J','K','L']])
# a3=np.hstack((a1,a2))
# print(a3)

#dstack() - only for 
# a1 = np.array([['A','B','C'],
#       ['D','E','F']])
# a2=np.array([['G','H','I'],
#              ['J','K','L']])
# a3=np.dstack((a1,a2))
# print(a3)

#Splitting of Arrays(based on sections)
# import numpy as np
# arr = np.arange(1,7)
# sarr = np.split(arr,2) #Split occurs in equal division
# print(sarr)

# arr1 = np.arange(1,25).reshape(6,4)
# sarr1 = np.split(arr1,2,axis=1) #Splitting done based on axes
# print(sarr1)

# arr3 = np.arange(1,25).reshape(2,3,4)
# sarr3 = np.split(arr3,2) #Splitting done based on axes
# print(sarr3)

#Splitting of Arrays(based on indexes)
# arr = np.arange(1,7)
# sparr = np.split(arr,[1,3])
# print(sparr)

#for 2D Array
# arr = np.arange(1,25).reshape(6,4)
# sparr = np.split(arr,[1,3],axis=0) #by default axis = 0
# print(sparr)

# arr = np.arange(1,25).reshape(6,4)
# sparr = np.split(arr,[1,3],axis=1)
# print(sparr)

# #for 3D array
# arr = np.arange(1,25).reshape(2,3,4)
# sparr = np.split(arr,[1,3]) 
# print(sparr)

#Vertical split is only possible for dimensions >= 2
#vsplit() - axis=0
# arr = np.array([[10,20,30],[40,50,60]])
# varr = np.vsplit(arr,2)
# print(varr)

# arr1 = np.arange(1,25).reshape(6,4)
# varr1 = np.split(arr1,[1,2])
# print(varr1)

#hsplit() - axis = 1
# arr1 = np.arange(1,7)
# varr1 = np.hsplit(arr1,[1,3])
# print(varr1)

# arr1 = np.arange(1,25).reshape(4,6)
# print(arr1)
# varr1 = np.hsplit(arr1,[1,3])
# print(varr1)

#dsplit() - axis=2
# arr1 = np.arange(1,25).reshape(2,3,4)
# print(arr1)
# varr1 = np.dsplit(arr1,2)
# print(varr1)

#array_split()
# arr1 = np.arange(1,11)
# varr1 = np.array_split(arr1,2)
# print(varr1)

# arr = np.array([1,2,3,4,56,7,8,9,10])
# lst = [1,4,7]
# sarr = arr[lst]
# narr = sarr+10
# print(np.resize(narr,(3,3)))

# #Sorting of array
# arr = np.array([10,15,29,25,3,45,21,99,27])
# srr = np.sort(arr)
# print(srr)

# #Revesing of an array
# rev = np.sort(arr)[::-1]
# print(rev)

#Sorting array of strings
# a = ['Alia','Fioana','Daisy','Gojo Satoro','Saikiki','Tanjiro','Inosuke','Zeinstzu']
# arr = np.sort(a)
# print(np.array(arr))

#Sorting of 2D Array
# arr = np.array([[9, 2, 7],
#                 [4, 8, 1],
#                 [6, 3, 5]])
# col_sorted = np.sort(arr, axis=0) #column-wise sorting
# print(col_sorted)


# rarr = np.array([[9, 2, 7],
#                 [4, 8, 1],
#                 [6, 3, 5]])
# row_sorted = np.sort(rarr, axis=1) #row-wise sorting
# print(row_sorted)

#Working of order keyword arguement
# dtype = [('name','S10'),('age','int'),('marks','float')] #S10 here is a byte string (fixed-length string)
# values = [('Ram',21,89.56),('Nemma',19,70.9),('Daisy',22,89.3)]
# arr = np.array(values,dtype=dtype)
# print(arr)
# print(np.sort(arr))
# agearr = np.sort(arr,order='age')
# print(agearr)

#where function
# arr = np.array([1,2,1,2,3,4,5,6])
# lst = np.where(arr==2)
# print(np.array(lst))

#Prinitng only even numbers and display 1 in place of odd numbers
# arr = np.array([1,2,1,2,3,4,5,6])
# lst = np.where(arr%2==0,arr,"1")
# print(np.array(lst))

#insert()
#for 1D Array
# arr = np.array([1,32,56,23,89,9,5,30,99])
# inserted = np.insert(arr,3,7)
# print(inserted)

# #for 2D array
# arr1 = np.array([[10,20],[30,40]])
# res = np.insert(arr1,1,100)
# print(res) #2D array flattens and then add the element
# print(arr1.ndim)
# print(res.ndim)

#without flattening
# arr1 = np.array([[10,20],[30,40]])
# res = np.insert(arr1,1,100,axis=0)
# print(res) #2D array flattens and then add the element
# print(arr1.ndim)
# print(res.ndim)

#append() function
# arr = np.array([[10,20],[30,40]])
# arr2=np.append(arr,[[99],[100]],axis=1)
# print(arr2)

#delete() function
#for 1d array
# arr = np.array([1,2,3,4,5])
# darr = np.delete(arr,1)
# print(darr)

#for 2d array
# arr = np.arange(1,10).reshape(3,3)
# print(arr)
# darr = np.delete(arr,1,axis=0) #for column;axis=1
# print(darr)

#Deleting a part of array using range and slicing
#using range
# arr = np.array([1,2,3,4,5,6,7]) #Range is exclusive
# darr = np.delete(arr,range(1,5))
# print(darr)

#using slicing
# arr = np.array([1,2,3,4,5,6,7]) #Range is exclusive
# darr = np.delete(arr,np.s_[1:5])
# print(darr)

#Printing numbers divisible with 3 as * if not #
# arr = np.array([[1,2,3],
#                 [4,5,6],
#                 [7,8,9]])
# lst = np.where(arr%3==0,"*","#")
# print(lst)


# arr = np.array([[1,2,3],[4,5,6]])
# app = np.append(arr,[[99],[100]],axis=1)
# print(app)

#Change element 3 to index 2
import random
arr = np.array([1,2,3,4,5,6])
np.random.shuffle(arr)

#change array
arr0 = np.zeros([3,3])
print(arr0)
res = arr0+1 #or 1-A
print(res)