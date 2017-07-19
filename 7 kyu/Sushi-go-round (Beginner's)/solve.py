def total_bill(s):
    plates = s.count('r')
    return (plates - plates // 5) * 2
