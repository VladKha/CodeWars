def pick_peaks(arr):
    result = {'pos': [], 'peaks': []}
    pos = 0
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[pos]:
            pos = i
        if pos and arr[pos - 1] < arr[pos] > arr[i + 1]:
            result['pos'].append(pos)
            result['peaks'].append(arr[pos])
    return result
