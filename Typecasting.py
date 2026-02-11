#Typecast a = 'skyllx' to i) int ii) str iii) bool iv) complex v)float
a = "skyllx"
b = int(a)
print(b,type(b))
c = str(a)
print(c,type(c))
d = bool(a)
print(d,type(d))
e = complex(a)
print(e,type(e))
f = float(a)
print(f,type(f))
#The error ValueError: invalid literal for int() with base 10: 'skyllx' occurs because you are attempting 
# to convert the string 'skyllx' to an integer. The int() function requires the input string to be a valid representation of a whole number 
# (e.g., "123", "-5"). Since 'skyllx' contains alphabetic characters, it cannot be interpreted as an integer, thus raising this ValueError. 
# This conversion is not possible with the given string.