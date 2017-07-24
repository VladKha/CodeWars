def sort_list(sort_key, l):
    return sorted(l, key=lambda d: d[sort_key], reverse=True)
