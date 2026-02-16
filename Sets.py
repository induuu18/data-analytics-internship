#Creating empty set
a = {} #In python this is considered as a dictionary
print(type(a))
a1 = set()
print(type(a1))

a2 = {{'A':10,'B':20}}
a3 = {[30,40]}
a4 = {{50,60}}

a5 = {(90,100)}
print(a5)

#16-02-2026
#Union
S1 = {1,2,3,4}
S2 = {3,5,6,7} #why not for alphabets
print(S1. union (S2)) #or print(S1 | S2)

#Intersection
print(S1.intersection(S2)) #or print(S1 & S2)

#Difference 
print(S1.difference(S2)) #OR print(S1 - S2) / print( S2 - S1)

#Symmetric Difference
print(S1.symmetric_difference(S2)) #Or print(S1 ^ S2)

#Subset and Superset 
A = {1,2,3,4,5,6}
B = {1,2,3}
print(A >= B) #Superset
print(A <= B) #Subset 

C = {1,2,3,4,5,6}
D = {10,1,12}
print(C.isdisjoint(D))

