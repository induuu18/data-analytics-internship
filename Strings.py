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

s1 = "Skyllx"
s2 = "for"
s3 = "Tech"
# s4 = "{} {} {}".format(s1,s2,s3)
s4 = "s1 = {} s2 ={} s3 ={}".format(s1,s2,s3)
print(s4)
# or
s4 = f'{s1} {s2} {s3}'
print(s4)