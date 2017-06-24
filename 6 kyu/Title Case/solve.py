def title_case(title, minor_words=''):
    words = title.capitalize().split()
    exceptions = minor_words.lower().split()
    return ' '.join([word if word in exceptions else word.capitalize() for word in words])
