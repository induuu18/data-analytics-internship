#Creation of tuples
Tup = (10,20,30,40)
Tup1 = tuple(Tup)
print(type(Tup1))
Tupz = ((10,20) , [30,40] , {50,60} , {'a':70 , 'b':80})
print(type(Tupz))

#Creation of Singleton tuple
a = (10,)   #Adding a comma next to the element it creates a singleton tuple
print(a)
print(type(a))

#Creating tuple without parantheses
a = 10, #This is called packing of element 
b = 10,20,30
print(type(a))
print(type(b))

#13-02-2026
tup = 10, 20, 30, 40, 50
a, _, c, _, e = tup
print(a, c, e)

#Accessing elements in tuple 
a = (10,20,30,40,50)
print(a[0])
print(a[-1])
print(a[2])

b = ((10,20) , [30,40] , {50,60} , {'A':70 , 'B':80})
print(b[0][0])
print(b[1][0])
print(b[2].pop)

#Printing a tuple
tup1 = 10,20,30,40,50
for i in tup1:
    print(i)

#Printing nested tuple
u = ((10,20) , (30,40))
for i,j in u:
    print(i)
    print(j)

#Index and element retrival
f = 11,12,13,14,15
for i,j in enumerate(f):
    print('Index:',i,'Element:',j)

f1 = 11,12,13,14,15
for i in range(len(f)):  #for i in range(len(f1))
    print('element:',i,'index:',f1[i])

f5 = 10,11,12,13,14,15
print(f5)
del f5

#Concatenation of tuples
p = 10,20
q = 50,60
r = p + q
print(r)

#Tuple Slicing
tup = 10,20,30,40,50,60,70,80,90,100
tup1 = tup[2:6]
tup2 = tup[:5]
tup3 = tup[-4:]
tup4 = tup[::-1]
print(tup1,tup2,tup3,tup4)
