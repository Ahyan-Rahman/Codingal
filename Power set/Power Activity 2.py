def totalflips(num1, num2):
    flips= 0
    while num1>0 or num2>0:
        lastb1=(num1&1)
        lastb2=(num2&1)
        if lastb1 != lastb2:
            flips=flips+1 
        num1=num1>>1
        num2=num2>>1
    return flips

A=int(input('Enter a number:'))
B=int(input('Enter another number:'))
print(f"Bit Differnece between {A} and {B} is ",totalflips(A,B))
