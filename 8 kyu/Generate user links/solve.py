try:
    from urllib.parse import quote
except:
    from urllib import quote


def generate_link(user):
    return 'http://www.codewars.com/users/' + quote(user)
