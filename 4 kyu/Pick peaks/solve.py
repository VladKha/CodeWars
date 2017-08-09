def pick_peaks(arr):
    result = {'pos': [], 'peaks': []}
    pos = 0
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[pos]:
            pos = i
        if arr[pos - 1] < arr[pos] and arr[i + 1] < arr[pos] and pos != 0:
            result['pos'].append(pos)
            result['peaks'].append(arr[pos])
    return result
