def is_palindrome(s):
    s = str(s).lower()
    return s == s[::-1]
