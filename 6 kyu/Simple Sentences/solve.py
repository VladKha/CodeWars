def make_sentences(parts):
    result = ''
    for i in range(len(parts) - 1):
        result += parts[i]
        if parts[i + 1] not in '.,':
            result += ' '
    result += parts[-1]
    return result.rstrip('.') + '.'
