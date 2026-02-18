#Creation of Dictionary
#1. Flower brackets
D = {}
print(D)
print(type(D))

#2.Using Typecasting
T = dict()
print(type(T))

D1 = {1:'A',2:'B'}
D2 = {1.1:'a',1.2:'b'}
D3 = {1:'AB',2:True,3:4}
D4 = {(10,):'ab',(20,):'ac'}
D5 = {'A':2+3j,'B':3+7j}
print(D1,D2,D3,D4,D5)

# Updating the existing dictionary
T1 = {1:'a',2:'b',3:'c'}
T1[4] = 'd'
print(T1)

T1.update({5:'e',6:'f'})
T1.update(one='a',two='b')
print(T1)

# Accessing elements in the dictionary
T2 = {1:'a',2:'b',3:[10,20,30,40],4:'d'}
print(T2[2])
lst = T2[3]
print(lst)
lst.append(99)
print(lst)
print(T2)
print(T2.get(5))
print(T2.get(4))

# Deleting or removing items from dictionarY
T2[1] = 'skyllx'
print(T2)
print(T2.pop(2))
print(T2)
del T2[1]
print(T2)
T2.clear()
print(T2)

# Accessing keys , values , items using built in functions
D = {1:'AB',2:'CD',3:'EF',4:'GH',5:'IJ'}
for i in D:
    print(i)
print(D.keys())
print(D.values())
print(D.items())
# or
for i in D.keys() , D.values() , D.items():
    print(i)

# Membership check
# FOR KEYS
print(1 in D)
print(6 in D)

# FOR K-V pairs
print('AB' in D.values())
print((1,'AB') in D.items())

# Concatenation of two dictionaries
d1 = {1:'apple',2:'banana',3:'Cherry'}
d2 = {4:'dragonfruit',5:'elderberry',6:'fig'}
d3 = {**d1 , **d2}
print(d3)

a = [1,2,3,4,5]
for i in a:
    po2 = {}

# Printing K-V pairs where key is element and value is element of power of 2
a = [1,2,3,4,5]
di = {}
for i in a:
    di[i]=i**2
print(di)

# Using lambda function
a = [1,2,3,4,5]
di = {i:i**2 for i in a}
print(di)

# Printing K-V pairs where key is power of 2 and value is element of a list
a1 = [1,2,3,4,5]
d = {}
for i in a1:
    if i % 2 ==0:
        d[i**2] = i
    else:
        d[i**3] = i
print(d)

#Using Lambda function
d = {(i**2 if i%2==0 else i**3): i for i in a1}
print(d)
#OR
d = {(i**2 if i%2==0 else i**3) : (i if i%2==0 else i) for i in a1}
print(d)

# zip function
Veh = ['Bicycle','Auto','Car','Bus']
Whe = [2,3,4,6]
M = ['road','road','road','road']
print(list(zip(Veh,Whe,M)))

for i in zip(Veh,Whe,M):
    print(i)

#all function
lst = [True,True,True]
res = all(lst)
print(res)

lst1 = [0==0,1==1,False]
res1 = all(lst1)
print(res1)

#Any function
lst2 = [True,True,False]
res2 = any(lst2)
print(res)

lst2 = [False,False,False]
res2 = any(lst2)
print(res2)

