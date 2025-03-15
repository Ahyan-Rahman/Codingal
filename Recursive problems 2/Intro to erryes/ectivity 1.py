def arrymean(arr, arr_size):
    total_sum = 0
    for i in range(0, arr_size):
        total_sum += arr[i]

    return float(total_sum/arr_size)

def arrymedian(arr, arr_size):
    sorted(arr)

    if arr_size%2 != 0:
        return float(arr[int(arr_size/2)])
    return float((arr[int((arr_size-1)/2)] + arr[int(arr_size/2)])/2.0) 
arr = [3,5,7,9,1,2,6,8]
arr_size = len(arr)

print("mean= ", arrymean(arr, arr_size))