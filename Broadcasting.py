#Broadcasting 1D & 3D Arrays
# import numpy as np
# arr1 = np.arange(1,3)
# arr2 = np.arange(10,50,10).reshape(1,2,2)
# print(f"The dimension of first array is{arr1.ndim}","The size of first array is {arr1.size}","The shape of the first array {arr1.shape}")
# print(f"The dimension of second array is {arr2.ndim}","The size of second array is {arr2.size}","The shape of the second array {arr2.shape}")
# print(arr1+arr2)

#Array Manipulation Function
#i)reshape()
# import numpy as np
# arr = np.arange(1,10,1)
# varr = np.reshape(arr,(3,3))
# carr = arr.reshape(3,3)
# print(f"varr \n {varr}")
# print(f"carr \n {carr}")
# carr1 = arr.reshape(3,3,order='F')
# carr2 = arr.reshape(3,-1)
# print(f"carr1 \n {carr1}")
# print(f"carr2 \n {carr2}")

#ii)resize()
# import numpy as np
# a = np.arange(6)
# a[1] = 98
# a.resize((2,5))
# print(a)
# b = np.arange(6)
# b[1] = 99
# brr = np.resize(b,(2,9))
# print(brr)

#iii)flatten()
# import numpy as np
# arr = np.arange(10,91,10).reshape(3,3)
# print(arr)
# print(arr.flatten('F'))
# print(arr.flatten('C'))

#iv)flat variable
# import numpy as np
# arr = np.arange(10,91,10).reshape(3,3)
# arr[1][1] = 99
# varr = arr.flatten()
# print(varr)
# print(arr)
# for i in arr.flat:
#     print(i)

#for 3D array
# arr3 = np.arange(1,19,1).reshape(1,3,6)
# print(arr3)
# for i in arr3.flat:
#     print(i)

#vi) ravel()
# import numpy as np
# arr = np.arange(10,91,10).reshape(3,3)
# arr[1][1] = 99
# varr = arr.ravel()
# print(varr)
# print(arr)