def to_query_string(data):
    parameters = []
    for name, value in sorted(data.items(), key=lambda pair: pair[0]):
        if type(value) == list:
            for e in value:
                parameters.append('{}={}'.format(name, e))
        else:
            parameters.append('{}={}'.format(name, value))
    return '&'.join(parameters)
