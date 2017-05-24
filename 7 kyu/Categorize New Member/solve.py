def openOrSenior(data):
    return ['Senior' if age >= 55 and handicap >= 8 else 'Open' for (age, handicap) in data]
