def averages(arr):
    if arr is None:
        return []
    return [(arr[i]+arr[i+1])/2 for i in range(len(arr)-1)]
