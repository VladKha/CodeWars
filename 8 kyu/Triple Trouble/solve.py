def triple_trouble(one, two, three):
    return ''.join(x+y+z for x,y,z in zip(one,two,three))
