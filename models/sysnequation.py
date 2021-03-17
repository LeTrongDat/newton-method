from models.nequation import NonlinearEquation
class SystemNonlinearEquation:
    DASH = "-" * 10
    def __init__(self, nonlinear_equations):
        self.__nonlinear_equations = nonlinear_equations
        self.__size = len(nonlinear_equations)

    def get_equations(self):
        return self.__nonlinear_equations
    def write(self):
        for i, eq in enumerate(self.__nonlinear_equations):
            print("    {}".format(eq.to_str_args()))
