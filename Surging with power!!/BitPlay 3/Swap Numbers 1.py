a=int(input('Enter a number for a'))
b=int(input('Enter a number for b'))
a=a^b
b=a^b
a=a^b
print('After swapping, a & b respectively are:',a,b)

a=int(input('Enter a number for a'))
b=int(input('Enter a number for b'))
a=(a&b)+(a|b)
b=a+(~b)+1
a=a+(~b)+1
print('After swapping, a & b respectively are:',a,b)