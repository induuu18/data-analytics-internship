#Recursive function
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
res = fact(5)
print(res)
#Factorial Function is callin itself again and again is called as resursive function