def in_asc_order(arr):
    if len(arr) <= 1:
        return True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
