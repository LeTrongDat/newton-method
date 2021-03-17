from strategies.strategy import Strategy
import random

class IterationStrategy(Strategy):
    def __init__(self, nonlinear_equation):
        self.__nonlinear_equation = nonlinear_equation

    def execute(self):
        return self.find_root()

    def find_root(self):
        print("> Please enter your interval [a, b]: ", end = "")
        a, b = map(float, input().split())
        print("> Please enter your epsilon: ", end = "")
        self.EPS = float(input())
        x1 = random.random() * (b - a) + a
        prv_val = -1e9
        converge = [x1]
        for iter in range(int(1e6)):
            if abs(self.__nonlinear_equation.f(x1)) < self.EPS and abs(prv_val - x1) < self.EPS:
                return [x1, converge]
            if (x1 < a or x1 > b): return "There is no solution!!"
            x1 = self.__nonlinear_equation.f_equiv(x1)
            converge.append(x1)

        return [x1, converge] if abs(self.__nonlinear_equation.f(x1)) < self.EPS else "There is no solution!!"



