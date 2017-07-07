def my_first_kata(a,b):
    if type(a) in [int, float, complex] and type(b) in [int, float, complex]:
        return a % b + b % a
    return False
