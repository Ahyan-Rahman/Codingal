#Take an input ‘n’ from the user and print 1-n using head recursion
def OnetoN(n,x):
    if n > x:
        return
    OnetoN(n+1,x)
    print(n)

x=int(input("Enter the last number: "))
OnetoN(1,x)
    