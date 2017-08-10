def compose(s1, s2):
    s1 = s1.split()
    s2 = s2.split()
    n = len(s1)
    return '\n'.join(s1[i][:i+1] + s2[n-i-1][:n-i] for i in range(n))
