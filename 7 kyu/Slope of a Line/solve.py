def getSlope(p1, p2):
    """ Return the slope of the line through p1 and p2"""
    return None if p1[0] == p2[0] else (p2[1] - p1[1]) / (p2[0] - p1[0])
