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