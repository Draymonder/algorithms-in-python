def search(arr, key, lower=0, upper=None):
    if upper is None:
        upper = len(arr)-1
    if upper == lower:
        assert key == arr[upper]
        return upper
    else:
        mid = (lower + upper) // 2
        if arr[mid] > key:
            return search(arr, key, lower, mid-1)
        else:
            return search(arr, key, mid, upper)


if __name__ == '__main__':
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(search(seq, 3))