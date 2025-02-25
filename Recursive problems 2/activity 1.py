def ways(stairs):

    if stairs<0:
        return 0
    
    if stairs==0:
        return 1
    
    twosteps=0
    onestep=0
    threesteps=0

    if (stairs>=1):
        onestep = ways(stairs-1)

    if (stairs>=2):
        twosteps = ways(stairs-2)

    if (stairs>=3):
        threesteps = ways(stairs-3)

    return onestep + twosteps + threesteps

stairs = int(input('How many stairs are there: '))
print("The number of different ways to climb is :", ways(stairs))

