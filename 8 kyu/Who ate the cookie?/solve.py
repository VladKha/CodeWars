def cookie(x):
    name = {str: 'Zach', float or int: 'Monica', int: 'Monica'}.get(type(x), 'the dog')
    return "Who ate the last cookie? It was {}!".format(name)
