def checksort(a):
    b=len(a)
    if b==0 or b==1:
        return True
    return a[0]<=a[1] and checksort(a[1:])


a=[100,101,109,103,104]
if checksort(a):
    print('This is sorted')
else: 
    print('This is not sorted')
