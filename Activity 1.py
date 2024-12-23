def totalSetBits(n):
    # Count variable set as 0 
    
    ones=0
    zeros=0
    # Right shift the number till we find first set bit
    while (n):
        if(n&1==1):
            ones+=1
        else:
            zeros+=1
        n >>= 1 

    print('The number of Zeros',zeros)
    print('The number of ones',ones)      

number= int(input("Enter a number here: "))
totalSetBits(number)