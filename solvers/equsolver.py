from solvers.solver import Solver
from strategies.secant import SecantStrategy
from strategies.iteration import IterationStrategy
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


class EquationSolver(Solver):
    DASH = "-" * 10
    SCALE = 6
    fig, axes = plt.subplots(2)
    fig_num = 0

    def __init__(self, equations):
        self.equations = equations

    def execute(self):
        print("> Please choose one of the equations below")
        for i, equation in enumerate(self.equations):
            if (i < 3): print("> {}. {}".format(i, equation.to_str()))
        print("> Enter your choice: ", end="")
        option = int(input())
        secant_data = self.secant_solver(option)
        iteration_data = self.iteration_sovler(option)

        plt.show()
        self.show_table(secant_data, iteration_data)

    def secant_solver(self, option):
        secant = SecantStrategy(self.equations[option])
        return self.solving(secant, "SECANT METHOD", option)

    def iteration_sovler(self, option):
        iteration = IterationStrategy(self.equations[option])
        return self.solving(iteration, "SIMPLE ITERATION METHOD", option)

    def solving(self, strategy, name, option):
        self.axes[self.fig_num].set_title(name)
        self.axes[self.fig_num].grid(True)
        x = np.arange(-5 if option != 2 else 1, 5 if option != 2 else 10)
        y = self.equations[option].f(x)
        self.axes[self.fig_num].plot(x, y)

        print("> {} {} {}".format(self.DASH, name, self.DASH))
        ans, converge = 0, []
        try:
            ans, converge = strategy.execute()
            ans = round(ans, self.SCALE)
            self.axes[self.fig_num].plot([ans], [self.equations[option].f(ans)], "bo-")
        except:
            ans = "There is no solutions!!"
        self.write_ans(ans, option)
        self.fig_num = self.fig_num + 1

        return converge

    def write_ans(self, ans, option):
        if (isinstance(ans, float)):
            print("> The solution of this equation is: {}".format(ans))
        else:
            print("> {}".format(ans))

    def show_table(self, secant, iteration):
        if not secant or not iteration: return

        sz = max(len(secant), len(iteration))
        secant, iteration = secant + [secant[-1]]* (sz - len(secant)), iteration + [iteration[-1]] * (sz - len(iteration))
        for i in range(sz // 10 + 1):
            data = {"Chord": secant[i * 10:min(i * 10 + 10, sz)],
                    "Iteration": iteration[i * 10:min(i * 10 + 10, sz)]}
            print(pd.DataFrame(data=data))
            if (i == sz // 10):
                print("> End.")
                break
            else:
                print("> Do you want to see more...? (Yes/No)")
                ans = input()
                if (ans == "No"): break
