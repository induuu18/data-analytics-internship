#Advance datatyprs - List
#Add data to a list
lst = [10,30,60,90,120]
lst.append(160)
print(lst)
#Remove data from list
lst.remove(90)
print(lst)
#Update data from the list
lst[2]=50
print(lst)
#Remove the last index closet from the list
lst.pop() #Remove using value
print(lst)
lst.pop(1) #Removing value by index
print(lst)

#Advance Data Types - Tuples
tup = (10,20,30,40,50)
print(tup)

#Advance Data Types - Sets
S = {'Anil','Bob','Catheline','Drake','Elf','Anil','Drake'} #Removes duplicate by default
print(S)
# Add , remove and pop the data in set
S.add('Frank')
print(S)
S.remove('Anil')
print(S)
S.pop()
print(S)

#Advance Data Types - Dictonaries
# Create Dict , Add , Update , delete a dictionaries
a = {1:'apple',2:'ball',3:'cat'}
print(a)
a[3]="cone"
print(a)
a[1]="animal"
print(a)
del a[3]
print(a)

#H.W - Using in-build functions of list , implement a question and print list after it

#LIST IN-BUILT FUNCTIONS 
#i) len()
li = ["apple","mango","cherry","banana"]
print(len(li))

#ii) list()
A = list(('apple','mango','banana','orange'))
print(A)

#Range of indexes
fruits = ['apple','mango']