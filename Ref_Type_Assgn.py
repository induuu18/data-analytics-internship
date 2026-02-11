a = 10
print(a)
print(id(a))

b = a
print(b)
print(id(b))

b = 20
print(b)
print(id(b))

lst = [1,2,3,4,5]
print(id(lst))
a = lst
print(id(a))
lst.remove(4)
print(a)
print(lst)
print(id(a))
print(id(lst))