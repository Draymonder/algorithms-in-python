def search(arr, key, low=0, upper=None):
    if upper is None: upper = len(arr)-1
    while low < upper:
        mid = (low+upper)//2
        if(arr[mid] > key): upper=mid-1
        elif(arr[mid] < key): low = mid+1
        else: return mid

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(search(seq, 3))