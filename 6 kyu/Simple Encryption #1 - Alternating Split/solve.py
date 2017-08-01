def decrypt(text, n):
    if not text:
        return text

    mid = len(text) // 2

    for i in range(n):
        a = text[:mid]
        b = text[mid:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(mid + 1))
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
