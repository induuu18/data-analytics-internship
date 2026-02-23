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