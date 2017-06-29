def fake_bin(x):
    return ''.join('0' if int(c) < 5 else '1' for c in x)
