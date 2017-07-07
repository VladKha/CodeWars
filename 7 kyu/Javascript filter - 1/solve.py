def search_names(logins):
    return filter(lambda pair: pair[0].endswith('_'), logins)
