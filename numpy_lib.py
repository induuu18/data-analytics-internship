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
r = np.arange(1,10)
print(f"Original array:{r}")
c = np.float32(r)
print(c)
c = np.bool_(r)
print(c)

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
arr=np.arange(1,10).reshape(3,3)
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