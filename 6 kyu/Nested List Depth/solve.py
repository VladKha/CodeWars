def list_depth(l, depth=1):
    max_depth = depth
    for e in l:
        if type(e) is list:
            max_depth = max(max_depth, list_depth(e, depth+1))
    return max_depth
