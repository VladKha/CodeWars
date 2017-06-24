def to_weird_case(s):
    def f(w):
        return ''.join(w[i] if i % 2 != 0 else w[i].upper() for i in range(len(w)))
    words = s.split()
    return ' '.join(map(f, words))
