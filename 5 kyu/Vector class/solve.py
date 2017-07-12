class Vector:
    def __init__(self, values):
        self.v = list(values)

    @staticmethod
    def __check_dims__(v1, v2):
        if len(v1) != len(v2):
            raise Exception('Bad dimensions')

    def add(self, other):
        Vector.__check_dims__(self, other)
        return Vector([self.v[i] + other.v[i] for i in range(len(self))])

    def subtract(self, other):
        Vector.__check_dims__(self, other)
        return Vector([self.v[i] - other.v[i] for i in range(len(self))])

    def dot(self, other):
        Vector.__check_dims__(self, other)
        return sum([x * y for x,y in zip(self.v, other.v)])

    def norm(self):
        return sum(x ** 2 for x in self.v) ** 0.5

    def __str__(self):
        return '(' + ','.join(str(x) for x in self.v) + ')'

    def equals(self, other):
        return self.v == other.v

    def __len__(self):
        return len(self.v)
