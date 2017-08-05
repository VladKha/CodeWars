def prefill(n, v='undefined'):
    try:
        return [v] * int(n)
    except:
        raise TypeError('{} is invalid'.format(n))
