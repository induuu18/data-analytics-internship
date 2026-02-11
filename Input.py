print("Enter a number")
a=int(input())
print("Enter another number")
b=int(input())
c=a+b
print(c)

#homework to take input and give display from console
print("Enter number to be displayed")
a=input()
print(a)

#take integer input and check if even or odd
print("Enter an integer")
num=int(input())
if num%2==0:
    print("Even number")
else:
    print("Odd number")

#Take input from console and display
print(input("Enter a string")) #input is taken from user by default is string


#Take a character from console check if it is vowel or consonant
Ch = input('Enter a character:')
Ch.lower()
if Ch in ['a' , 'e' , 'i' , 'o' ,'u']:
    print('It is a vowel')
else:
    print('It is a consonant')

#Take age and check whether he is eligible to vote or not
age = int(input("Enter age :"))
if (age >= 18 ):
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

#Take input from console and say whether the year is a leap year or not
year = int(input("Enter the year:"))
if ( year % 400 == 0 or year % 4 == 0 and year % 100 != 0):
    print("This year is a leap year")
else:
    print("This year is not a leap year")

#Check whether the number is divisible by 3 or 7
num = int(input("Enter the number :"))
if (num % 3 == 0 or num % 7 == 0):
    print("This number is divisible by 3 or 7")
else:
    print("This number is neither divisible by 3 or 7")
