n = int(input('Enter a number'))
def CheckIfPower(n):
    if(n<=0):
        return False
    if(n==1):
        return True
    if(n%2==0):
        return(n/2)
    return False

if(CheckIfPower(n)):
    print("Power of 4")
else:
    print("not power of 4")