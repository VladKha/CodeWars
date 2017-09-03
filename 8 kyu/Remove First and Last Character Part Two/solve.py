def array(s):
    parts = s.split(',')[1:-1]
    return ' '.join(parts) if parts else None
