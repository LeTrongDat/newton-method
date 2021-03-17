from models.nequation import NonlinearEquation
from solvers.equsolver import EquationSolver
from solvers.syssolver import SystemSolver
from invokers.invoker import Invoker
import numpy as np
from models.argument import Argument
from models.sysnequation import SystemNonlinearEquation
from strategies.newton import NewtonStrategy

if __name__ == '__main__':
    np.seterr(all='raise')
    equations = [
        NonlinearEquation(lambda x: x ** 3 - 2 * x ** 2 + 1, lambda x: (2 * x ** 2 - 1) ** (1. / 3.),
                          "x^3 - 2x^2 + 1 = y"),
        NonlinearEquation(lambda x: x - 1 - 0.5 * np.sin(x), lambda x: 1 + 0.5 * np.sin(x),
                          "x - 1 - 0.5 * sin(x) = y"),
        NonlinearEquation(lambda x: np.log(x) + x ** 3 - x, lambda x: (x - np.log(x)) ** (1. / 3.),
                          "ln(x) + x^3 - x = y"),
        NonlinearEquation(),
        NonlinearEquation(),
        NonlinearEquation(),
        NonlinearEquation(),
        NonlinearEquation(),
        NonlinearEquation()
    ]
    arguments = [
        Argument(lambda x: 3 * x ** 2 - 5, "3 * x^2 - 5"),
        Argument(lambda x: 2 * x ** 2, "2 * y^2"),
        Argument(lambda x: 8 * x ** 2 - 14, "8 * x^2 - 14"),
        Argument(lambda x: 6 * x ** 2, "6 * y^2"),
        Argument(lambda x: x ** 2 + x - 11, "x^2 + x - 11"),
        Argument(lambda x: x ** 2, "y^2"),
        Argument(lambda x: 3 * x ** 2, "3 * x^2"),
        Argument(lambda x: np.tan(x) - 2, "tan(y) - 2"),
        Argument(lambda x: 7 * x ** 3 - 2, "7 * x^3 - 2"),
        Argument(lambda x: -6 * x ** 2 + x, "-6 * y^2 + y"),
        Argument(lambda x: x ** 4 - 5, "x^4 - 5"),
        Argument(lambda x: x ** 3, "y^3")
    ]

    equations[3].set_args(arguments[0:2])
    equations[4].set_args(arguments[2:4])
    equations[5].set_args(arguments[4:6])
    equations[6].set_args(arguments[6:8])
    equations[7].set_args(arguments[8:10])
    equations[8].set_args(arguments[10:12])

    system_non_equations = [
        SystemNonlinearEquation(equations[3:5]),
        SystemNonlinearEquation(equations[5:7]),
        SystemNonlinearEquation(equations[7:9])
    ]

    equation_solver = EquationSolver(equations)
    system_solver = SystemSolver(system_non_equations)
    system_solver.set_strategy(NewtonStrategy())

    invoker = Invoker(equation_solver, system_solver)
    invoker.invoke()
