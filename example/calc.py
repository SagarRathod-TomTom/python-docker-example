import numpy as np
from fire import Fire
from functools import reduce


class Calculator:

    def add(self, *values):
        return sum(values)

    def mult(self, *values):
        return reduce(lambda accm, value: accm * value, values)

    def sub(self, num1, num2):
        return num1 - num2

    def mean(self, *values):
        return np.mean(values)

    def var(self, *values):
        return np.var(values)

    def std_dev(self, *values):
        return np.std(values)


if __name__ == "__main__":
    Fire(Calculator)