def well(x):
    n = x.count('good')
    return 'Fail!' if n == 0 else 'Publish!' if n in [1,2] else 'I smell a series!'
