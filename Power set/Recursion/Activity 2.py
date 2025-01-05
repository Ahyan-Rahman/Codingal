def factorial(a):
    if a==0:
        return 1
    return a*factorial(a-1)






a=int(input('Enter a number to calculate its factorial: '))
print(factorial(a))