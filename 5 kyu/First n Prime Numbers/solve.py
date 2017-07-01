def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


class Primes:
    d = dict()

    @staticmethod
    def first(n):
        result = []
        i = 2
        while len(result) < n:
            if i in Primes.d:
                prime = Primes.d[i]
            else:
                prime = is_prime(i)
                Primes.d[i] = prime
            if prime:
                result.append(i)
            i += 1
        return result
