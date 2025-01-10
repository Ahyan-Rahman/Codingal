#Take an input ‘n’ from the user and print n-1 using tail recursion.
def OnetoN(n,x):
    if n > x:
        return
    print(n)
    OnetoN(n+1,x)

x=int(input("Enter the last number: "))
OnetoN(1,x)