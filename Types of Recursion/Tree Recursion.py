#IncresingDecreasing
#Outline:
#Take an niput ‘n’ from the user and print Increasing - Decreasing sequence (n n-1 n-2 . . . . 1 1 2 3 . . . .n) using recursion.

def OnetoN(n,x):
    if (n<1 or n > x):
        return     
    print(n)
    OnetoN(n-1,x)
    print(n)

x=int(input("Enter the last number: "))
OnetoN(x,x)
