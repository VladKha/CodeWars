import re


def validPhoneNumber(phone_number):
    return re.fullmatch(r'^\(\d{3}\) \d{3}-\d{4}$', phone_number) is not None
