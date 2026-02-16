#Write lines of code to do cube of each element in a list
lst = [1,2,3,4,5]
clst = []
for i in lst:
    clst.append(i**3)
print(clst)

#Another way of doing the above program
lst1 = [1,2,3,4,5]
cubelst2 = [i**3 for i in lst]
print(cubelst2)

#Printing only even numbers from the list
lst1 = [1,2,3,4,5,6,7,8,9,10]
evelst= [i for i in lst1 if i % 2 == 0 ]
print(evelst)

#Print only single character from the list 
s = ['a','b',1,2,'Skyllx']
for i in s:
    if type(i) == str:
        if len(i) == 1:
            print(i)

#Using List Comphrension
s = ['a','b',1,2,'Skyllx']
s1 = [i for i in s if type(i)==str and len(i) == 1]
print(s1)

#Write a code where u power of 3 for odd if not power of 2
num = [1,2,3,4,5,6,7,8,9,10]
lsteve = []
lstodd = []
for i in num:
    if i % 2 == 0:
        lsteve.append(i**2)
    else:
        lstodd.append(i**3)
print(lsteve)
print(lstodd)

#Using list Comph
num1 = [1,2,3,4,5,6,7,8,9,10]
lsteve = [i**2 for i in num1 if i%2==0]  #[what i want condition from where i want ]
lstodd = [i**3  for i in num1 if i%2 != 0]
print(lsteve)
print(lstodd)

#if-else condition
num2 = [1,2,3,4,5,6,7,8,9,10]
lst = [i**2 if i%2 == 0 else i**3 for i in num2]
print(lst)

# 12-02-2026
# Access and print with index values of each element
a = [ 1 , 2 , 3 , 4 , 5 ]
for i in a:
    print(i , a.index(i))
# 1) Using range()
a = [ 1 , 2 , 3 , 4 , 5 ]
for i in range (len(a)):
    print(i , a[i])

#2) Using enumnerate function 
a = [ 1 , 2 , 3 , 4 , 5 ]
for i , j in enumerate(a):
    print(i , j)

#Access nested list
A = [[1,2] , [3,4] , [5,6]]
for i,j in A:
    print(i)
    print(j)
#OR
A = [[1,2] , [3,4] , [5,6]]
for i in A:
    for j in i:
        print(j)

#Comparision of lists
a = [10 , 20 , 30 , 40 , 50]
b = [10 , 20 , 30 , 40 , 50]
print(a==b)
print(a<b)
print(a>b)

a = [10 , 20 , 30 , 40 ]
b = [10 , 20 , 30 , 40 , 50]
print(a>b)

#Reversing of List using slicing
li = [1,2,3,4,5,6,7,8]
rev = []
for i in li:
    rev = li[::-1]
print(rev)
#OR
li = [1,2,3,4,5,6,7,8]
li2 = li[::-1]
print(li2)

#Sorting of list
numl = [10,20,70,30,80,50,100]
res = sorted(numl)
print('Ascending order :', res)
res1 = sorted(numl , reverse=True)
print('Descending order :' , res1)

#Sorting of list using loops
a = [1,20,56,78,99,32,50,29,5,14]
for i in range(len(a)):
    for j in range(len(a) - i -1):
        if a[j] > a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j]
print(a)

#Membership Check
li = [10,20,30,40,50]
print(20 in li)
print(100 in li)
