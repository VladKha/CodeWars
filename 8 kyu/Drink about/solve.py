def people_with_age_drink(age):
    result = 'drink '
    if age <= 13:
        result += 'toddy'
    elif age < 18:
        result += 'coke'
    elif age < 21:
        result += 'beer'
    else:
        result += 'whisky'
    return result
