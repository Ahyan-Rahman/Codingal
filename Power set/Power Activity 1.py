def powerset(set,setsize):
    PowerSetSize=2**setsize
    for i in range(PowerSetSize):
        for j in range(setsize):
            if (i & (1<<j))>0:
                print(set[j], end=" ")
        print()

size = int(input("Enter the set-size: "))
set=[]
for i in range(size):
    A=int(input('Enter your element'))
    set.append(A)
powerset(set,size)