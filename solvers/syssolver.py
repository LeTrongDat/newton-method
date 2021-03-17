from solvers.solver import Solver
from models.sysnequation import SystemNonlinearEquation
from matplotlib import pyplot as plt
import numpy as np


class SystemSolver(Solver):
    SCALE = 3

    def __init__(self, systems):
        self.systems = systems

    def execute(self):
        print("> Please choose one of the system of nonlinear equations below:")
        for index, system in enumerate(self.systems):
            print("> {}. System {}".format(index, index))
            system.write()
        print("> Enter your variant: ", end="")
        option = int(input())

        self.strategy.set_system(self.systems[option])

        ans = self.strategy.execute()

        self.draw(option, ans)

    def set_strategy(self, strategy):
        self.strategy = strategy

    def draw(self, option, ans):
        plt.subplot(111)
        plt.title("NEWTON METHOD")
        plt.grid(True)
        if option == 0:
            x = np.arange(-1.2, 1.2, 0.001)
            y = ((5 - 3 * x ** 2) / 2) ** (1 / 2)
            plt.plot(x, y, label="3x^2 - 5 + y^2 = 0")
            y = ((14 - 8 * x ** 2) / 6) ** (1 / 2)
            plt.plot(x, y, label="8x^2 - 14 + 6y^2 = 0")
        elif option == 1:
            x = np.arange(-2, 2, 0.0001)
            y = (11 - x ** 2 - x) ** (1 / 2)
            plt.plot(x, y, label="x^2 + x - 11 + y^2 = 0")
            y = np.arange(2, 4, 0.0001)
            x = ((2 - np.tan(y)) / 3) ** (1 / 2)
            plt.plot(x, y, label="3x^2 + tan(y) - 2 = 0")
        else:
            y = np.arange(-1.7, 1.7, 0.001)
            x = ((6 * y ** 2 - y + 2) / 7) ** (1 / 3)
            plt.plot(x, y, label="7x^3 - 2 - 6y^2 + y = 0")
            x = (-y ** 3 + 5) ** (1 / 4)
            plt.plot(x, y, label="x^4 - 5 + y^3 = 0")
        plt.legend()
        plt.plot([ans[0]], [ans[1]], "bo-")
        plt.annotate("({}, {})".format(round(ans[0], self.SCALE), round(ans[1], self.SCALE)), (ans[0], ans[1]))
        plt.show()
