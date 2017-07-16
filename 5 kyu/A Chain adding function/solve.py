class add(int):
    def __call__(self, n):
        return add(self + n)
