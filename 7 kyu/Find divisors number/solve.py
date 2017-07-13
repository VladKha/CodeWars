def divisors(n):
    return sum(n % i == 0 for i in range(1,n + 1))
