def alias_gen(f_name, l_name):
    a = FIRST_NAME.get(f_name[0].upper())
    b = SURNAME.get(l_name[0].upper())
    return '{} {}'.format(a,b) if (a and b) else 'Your name must start with a letter from A - Z.'
