#Positional Arguements
def power_of(num,pow):
    print(num**pow)
power_of(5,2)
power_of(2,5)

#Keyword Arguements
def power_of(num,pow):
    print(num**pow)
power_of(pow = 2 , num = 5)
power_of(pow = 5 , num = 2)

#Default Arguments
def power_of(num,pow):
    print(num**pow)
#power_of(5) error
power_of(5,3)

#Variable length
def sub_de(*args):
    print(*args)
sub_de('Manisha',22,'Indu',21)

#Variable length keyword arguement
