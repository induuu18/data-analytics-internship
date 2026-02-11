# #Write lines of code to do cube of each element in a list
# lst = [1,2,3,4,5]
# clst = []
# for i in lst:
#     clst.append(i**3)
# print(clst)

# #Another way of doing the above program
# lst1 = [1,2,3,4,5]
# cubelst2 = [i**3 for i in lst]
# print(cubelst2)

# #Printing only even numbers from the list
# lst1 = [1,2,3,4,5,6,7,8,9,10]
# evelst= [i for i in lst1 if i % 2 == 0 ]
# print(evelst)

# #Print only single character from the list 
# s = ['a','b',1,2,'Skyllx']
# for i in s:
#     if type(i) == str:
#         if len(i) == 1:
#             print(i)

# #Using List Comphrension
# s = ['a','b',1,2,'Skyllx']
# s1 = [i for i in s if type(i)==str and len(i) == 1]
# print(s1)

#Write a code where u power of 3 for odd if not power of 2
# num = [1,2,3,4,5,6,7,8,9,10]
# lsteve = []
# lstodd = []
# for i in num:
#     if i % 2 == 0:
#         lsteve.append(i**2)
#     else:
#         lstodd.append(i**3)
# print(lsteve)
# print(lstodd)

#Using list Comph
# num1 = [1,2,3,4,5,6,7,8,9,10]
# lsteve = [i**2 for i in num1 if i%2==0]  #[what i want condition from where i want ]
# lstodd = [i**3  for i in num1 if i%2 != 0]
# print(lsteve)
# print(lstodd)

#if-else condition
# num2 = [1,2,3,4,5,6,7,8,9,10]
# lst = [i**2 if i%2 == 0 else i**3 for i in num2]
# print(lst)