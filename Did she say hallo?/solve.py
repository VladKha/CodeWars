import re


def validate_hello(greetings):
    pattern = re.compile(r'hello|ciao|salut|hallo|hola|ahoj|czesc', flags=re.IGNORECASE)
    return re.search(pattern, greetings) is not None
