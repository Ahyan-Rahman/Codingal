def pof2(x):
    if x==0:
        return False
    if (x & (~(x - 1)) == x):
        return True
        
    return False

a = int(input("Enter a number to be checked for power of 2"))  
if (pof2(a)):
    print(a,"is a power of 2")
else:
    print(a,"is not a power of 2")

"""" 
x=8
x-1=7
~(x-1)=-8=11111000
00001000
1000
"""