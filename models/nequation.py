from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
class NonlinearEquation:
    EPS = 1e-6

    def __init__(self, fx = None, fequiv = None, to_str = None):
        self.__fx = fx
        self.__fequiv = fequiv
        self.__to_str = to_str

    def f(self, x):
        return self.__fx(x)

    def f_equiv(self, x):
        return self.__fequiv(x)
    def to_str(self):
        return self.__to_str

    def get_number_of_args(self):
        return len(self.args)
    def set_args(self, args):
        self.args = args
    def f_args(self, values):
        ans = 0
        for i, value in enumerate(values):
            ans += self.args[i].f(value) if i < len(self.args) else 0
        return ans
    def f_deri(self, i, values):
        values[i] += self.EPS
        f1 = self.f_args(values)
        values[i] -= self.EPS
        f0 = self.f_args(values)

        return (f1 - f0) / self.EPS

    def to_str_args(self):
        s = []
        for i, arg in enumerate(self.args): s.append(arg.to_str())
        return " + ".join(s) + " = 0"


