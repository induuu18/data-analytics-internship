A = "Skyllx for a 'Reason'"
B = "'Skyllx for a' Reason"
C = '''''Skyllx for a ' "Reason"'''
print(A)
print(B)
print(C)

A1 = 'a'
print(A1)
print(id(A1))

A2 = 'a'
print(A2)
print(id(A2))

#String Formatting
s1 = "Skyllx"
s2 = "for"
s3 = "Tech"
s4 = "{} {} {}".format(s1,s2,s3)
s4 = "s1 = {} s2 ={} s3 ={}".format(s1,s2,s3)
print(s4)
# or
s4 = f'{s1} {s2} {s3}'
print(s4)

#Binary formatting
a = 45
b = 16
print("a = {:b} b = {:b}".format(a,b))

#Exponential formatting
y = 231.234567
print("{:e}".format(y))

#Float formatting
pi = 3.14537346478
print("{:.2f}".format(pi))

#Percentage formatting
x = 0.56
print("{:.2%}".format(x)) #print("{:%}".format(x)

a = 10.57
print("%d"%(a))

b = 11
print("%f"%(b))

A = 45
print("%x"%(A))
print("%s"%(A))
print("%o"%(A))

# Built in functions in string
St= 'This is a Test String'
print(St.lower())
print(St.upper())
print(St.capitalize())
print(St.title())
print(St.swapcase())
print(St.index('s'))
print(St.split())

table = St.maketrans('aeiou','12345')
print(table)
print(St.translate(table))

#Reverse a string
string = 'Skyllx for tech'
rev = ''
for i in reversed(string):
    print(i)

#using for loop 
rev = ''
for i in string:
    rev = i + rev
print(rev)

#using slicing
print(string[::-1])

#Printing each character in a string
S = 'Hello World'
L =[]
for i in S:
    L.append(i)
print(L) #Method 1 
print(list(S)) #Method 2
print([*S]) #Method 3

# Membership check in string
Si = 'Skyllx for tech'
print(Si.startswith('S'))
print(Si.startswith('Sky'))
print(Si.startswith('X'))
print(Si.endswith('ch'))
print(Si.startswith('ab'))

#Checking if string and id's of entered strings are equal or not
S1 = 'skyllx'
S2 = 'skyllx'
if(S1==S2):
        print("Strings are equal")
else:
    print("Strings are not equal")
if id(S1)==id(S2):
    print("Id's of both the strings are same")
else:
    print("Id's of both the strings are not same")

#Different methods to join two seperate strings
l1 = 'Hello'
l2 = 'World'
l3 = l1+l2
print(l3)
l4 = (''.join([l1,l2]))
print(l4)
l5 = "{} everyone in {}".format(l1,l2)
print(l5)
l6 = f'{l1} {l2}'
print(l6)