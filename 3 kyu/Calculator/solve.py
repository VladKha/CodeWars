class Calculator(object):
    def evaluate(self, s):
        return float('{:.4f}'.format(eval(s)))
