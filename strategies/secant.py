from .strategy import Strategy
import random


class SecantStrategy(Strategy):

    def __init__(self, nonlinear_equation):
        self.nonlinear_equation = nonlinear_equation

    def execute(self):
        return self.find_root()

    def find_root(self):
        print("> Please enter your interval [a, b]: ", end = "")
        a, b = map(float, input().split())
        print("> Please enter your epsilon: ", end = "")
        self.EPS = float(input())
        converge = [a]
        prv_val = -1e9
        for i in range(int(1e6)):
            fa = self.nonlinear_equation.f(a)

            if abs(fa) < self.EPS and abs(prv_val - a) < self.EPS:
                return [a, converge]
            fb = self.nonlinear_equation.f(b)
            if (fa == fb):
                return "There is no solution!!"
            rev_diff_fx = (b - a) / (fb - fa)
            a = a - fa * rev_diff_fx
            converge.append(a)
        return [a, converge] if abs(self.nonlinear_equation.f(a)) < self.EPS else "There is no solution!!"
