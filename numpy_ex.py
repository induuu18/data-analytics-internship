#Question 1
import numpy as np
# arr = [1,2,3,4,5]
# inarr = np.resize(arr,(2,3))
# print(inarr**3)
# inarr1 = np.resize(arr,(2,6))
# print(inarr1**3)

#Question 2
# a1 = np.array([['A','B','C'],
#       ['D','E','F']])
# print(a1)
# print(a1.ndim)
# a2=np.array([['G','H','I'],
#              ['J','K','L']])
# print(a2)
# a3=np.concatenate((a1,a2))
# print(a3)

# #Question 3
# a=np.arange(1,25).reshape(2,3,4)
# # print(a)
# # c=np.transpose(a)
# # print(c)
# b=np.swapaxes(a,2,0)
# print(b)

# #Question 3
# arr=np.array([0,1])
# b=arr.astype(bool)
# res=np.concatenate((b,b)).reshape(2,2)
# print(res)

#Question 4
# a=np.full(6,fill_value=4).reshape(2,3)
# print(a)
# for i in np.nditer(a):
#     print(i)

#Question
# import numpy as np
# a1 = np.array([[1,2,3],[4,5,6]])
# a2 = np.array(["one","two","three"])
# varr = np.vstack((a1,a2))
# print(varr)
# print(np.strings.multiply(varr,0))

# a3 = np.array([[1,2,3],['one','two','three']])
# narr = a3.transpose()
# print(narr)
# farr=narr.flatten()
# print(farr)
#or
# a3 = np.array([[1,2,3],['one','two','three']])
# narr = a3.flatten(order='F')
# print(narr)
