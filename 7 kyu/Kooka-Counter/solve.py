import re


def kooka_counter(laughing):
    return len(re.findall(r'(Ha)+|(ha)+', laughing))
