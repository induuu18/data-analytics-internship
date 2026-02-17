#Functions
#Add - To add a single elemenets in a set
P = {1,2,3,4,5,6}
P.add(5)
print(P)

#Update - To add multiple elemenets in a set
Q = {1,2,3,4}
Q1 = {5,6,7,8,9,10}
Q.update(Q1)
print(Q)

#Remove To remove a single elemenet from a set
P.remove(3)
print(P)

#Clear() - To remove all elements from a set 
s = {1,2,3,4,5,6,7,8,9,10}
s.clear()
print(s)

#Discard 
P.discard(4)
print(P)

#Frozen set
S1 = frozenset({1,2,3})
S1.add(4)
print(S1) #Poses error since it is frozen set
print(type(S1))

#Q1.Print power of 2 for all elements in set 
A = {1,2,3,4,5}
B = set()
for i in A:
    B.add(i**2)
print(B)

#Using Lambda function , print power of 2 for all elements in set 
B = set()
B = {i**2 for i in A}
print(B)

#Q2.Printing power of 3 for odd and power of 2 for even using lambda function
S = {1,2,3,4,5}
P = {i**3 if i%2 !=0 else i**2 for i in S}
print(P)

#Printing power of 3 for odd and power of 2 for even using for loop
S = {1,2,3,4,5}
eve = set()
odd = set()
for i in S:
    if i % 2 == 0:
        eve.add(i**2)
    else:
        odd.add(i**3)
print(eve)
print(odd)

S = {1,2,4}
P = {i if i%2 == 0 else '#' for i in S}
print(P)
#The above program would not work as set doesnt allow duplicates

S = {1,2,3,4,5}
P = set()
for i in S:
    if i%2 == 0:
        P.add(i)
    else:
        P.add('#')
print(P)

#Q3.Extract common elements from both the set and power 2
S1 = {1,2,3,4,5,6}
S2 = {3,4,5,7,8,9}
S3 = S1 & S2
A = set()
for i in S3:
    A.add(i**2)
print(A)