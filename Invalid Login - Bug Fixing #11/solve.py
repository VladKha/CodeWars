def validate(username, password):
    if any(s in password for s in ['||', '//']):
        return 'Wrong username or password!'

    validator = Validator()
    return validator.login(username, password)
