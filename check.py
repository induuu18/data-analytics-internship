num = int(input("Enter the number :"))
if (num % 3 == 0 or num % 7 == 0):
    print("This number is divisible by 3 or 7")
    if (num % 3 == 0 ):
        print("This number is divisible by 3")
    if (num % 7  == 0 ):
        print("This number is divisible by 7")
else:
    print("This number is neither divisible by 3 or 7")