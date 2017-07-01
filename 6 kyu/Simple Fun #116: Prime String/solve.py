def prime_string(s):
    return (s + s).find(s, 1) == len(s)
