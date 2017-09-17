def createDict(keys, values):
    return dict(zip(keys, values + [None] * (len(keys) - len(values))))
