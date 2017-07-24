import re


def autocorrect(message):
    return re.sub(r'\b(u|you+)\b', 'your sister', message, flags=re.IGNORECASE)
