def list_animals(animals):
    return ''.join('{}. {}\n'.format(i, x) for (i, x) in enumerate(animals, 1))
