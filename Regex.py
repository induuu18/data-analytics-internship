#Tab Space
res = "\tSkyllx"
print(res)

#New Line
res1 = "\nSkyllx"
print(res1)

#Raw string
res3 = r"\tSkyllx"
res4 = r"\nSkyllx"
print(res3)
print(res4)

#search function
import re
S = "Skyllx for Tech"
res = re.search(r"Skyllx",S)
print(res)

res1 = re.search(r"Tech",S)
print(res1)

res2 = re.search(r'xyz',S)
print(res2)

print(S[0:6])
print(S[11:15])

#Match function
res3 = re.match("Skyllx",S)
print(res3)

s = '''akash26@gmail.com
    dazedhoney99@gmail.com
    xyzscf@gmail.com
    shaswath56@gmail.com
    linda45@gmail.com
    9876543215'''
print(s)
fi = re.search(r"[a-zA-z0-9\.]+@[a-z]+\.[a-z]+",s)
print(fi)
fi1 = re.findall(r"[a-zA-z0-9\.]+@[a-z]+\.[a-z]+",s)
print(fi1)
fi3 = re.sub( r"([a-zA-Z0-9\.]+)(@[a-z]+\.[a-z]+)", r"Name: \1, Domain: \2", s )
print(fi3)

import re 
#RE for fetching first two letters in each word
S = "Skyllx for tech"
res = re.findall(r"\b\w{2}",S)
print(res)
#RE for fetching the first word in a string
res1 = re.search(r"^\w+",S)
print(res1)
Mu = '''9808111112
        Krishnakant
        02/10/1994
        info@skyllx.com'''
op = re.findall(r"\d{2}/\d{2}/\d{4}",Mu)
print(op)

#RE to fetch only indian pincodes from the multi line string
pincode = ''' 560001
10001
700106
94105
110016
SW1A 1AA
400601
200
751001
75008
V6B 1A1
10115
600045
90210
00100'''
list = re.findall(r"[1-9][0-9]{5}",pincode)
print(list)

import re
ans = input("Enter your Indian Pincode:")
pattern = r"[1-9][0-9]{5}"
if re.search(pattern,ans):
    print("It is a valid Indian Pincode")
else:
    print("It is not a valid Indian Pincode")

# IGBORECASE/I method
S = "Skyllx for tech"
res = re.search(r"[F][O][R]",S,re.IGNORECASE)
print(res)
res1 = re.search(r"[F][O][R]",S,re.I)
print(res1)

# DotAll method
s = "skyllx . \ntech .\nfor"
res = re.search(r".+",s,re.DOTALL)
print(res)