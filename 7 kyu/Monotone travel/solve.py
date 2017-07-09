def is_monotone(heights):
    for i in range(len(heights) - 1):
        if heights[i] > heights[i+1]:
            return False
    return True
