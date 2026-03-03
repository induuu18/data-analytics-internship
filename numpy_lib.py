# import numpy as np
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
import numpy as np
import sys

arr = np.arange(1, 11)
print("arange:", arr)
print("getsizeof:", sys.getsizeof(arr))
print("size:", arr.size)
print("shape:", arr.shape)
print("dtype:", arr.dtype)
print("ndim:", arr.ndim)
print("linspace:", np.linspace(0,1,5))
print("zeros:\n", np.zeros((2,3)))
print("ones:\n", np.ones((2,2)))
print("full:\n", np.full((2,2), 9))
print("random:\n", np.random.random((2,3)))
print("randint:\n", np.random.randint(10,50,(2,3)))
print("astype float:", arr.astype(float))
print("eye:\n", np.eye(3))
print("identity:\n", np.identity(3))
reshaped = arr.reshape(5,2)
print("Reshaped (5x2):\n", reshaped)
arr1 = np.arange(1, 13)
print("Original array:", arr1)

