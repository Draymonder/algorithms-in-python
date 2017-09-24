def search(arr, key, low=0, upper=None):
    if upper is None:
        upper = len(arr)-1
    if upper == low:
        assert key == arr[upper]
        return upper
    else:
        mid = (low + upper)//2
        if arr[mid] > key:
            return search(arr, key, low, mid)
        else:
<<<<<<< Updated upstream:search_right.py
            return search(arr, key, mid+1, upper)


if __name__ == '__main__':
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(search(seq, 3))
=======
            return search(arr, key, mid, upper)
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(search(seq, 3))
>>>>>>> Stashed changes:search.py
