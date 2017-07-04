def get_number_from_string(s):
    return int(''.join(c for c in s if c.isdigit()))
