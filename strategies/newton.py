from strategies.strategy import Strategy

class NewtonStrategy(Strategy):
    size = 0
    SCALE = 6
    def execute(self):
        equations = self.system.get_equations()
        for equa in equations:
            self.size = max(self.size, equa.get_number_of_args())
        print("> Please enter an initial value of {} arguments: ".format(self.size))
        print("> ", end = "")

        values = list(map(float, input().split()))

        for i in range(int(1e5)):
            matrix = []
            for order, equation in enumerate(equations):
                row = []
                for j in range(equation.get_number_of_args()):
                    row.append(equation.f_deri(j, values))
                row.append(-equation.f_args(values))
                matrix.append(row)
            deltas = self.gauss(matrix)
            for index, delta in enumerate(deltas): values[index] += delta

        print("The solution of this system of nonlinear equations is: ", end = "")
        for value in values: print(round(value, self.SCALE), end = " ")
        return values

    def gauss(self, matrix):
        n = len(matrix)
        pivot_col, pivot_row = 0, 0
        while pivot_col < n and pivot_row < n:
            i = pivot_row
            for i in range(pivot_row, n, 1):
                if matrix[i][pivot_col]: break
            if not matrix[i][pivot_col]:
                pivot_col += 1
                continue
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
            for i in range(pivot_row + 1, n, 1):
                rate = matrix[i][pivot_col] / matrix[pivot_row][pivot_col]
                for j in range(pivot_col, n + 1, 1):
                    matrix[i][j] -= matrix[pivot_row][j] * rate

            pivot_row += 1
            pivot_col += 1
        values = []
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                matrix[i][n] -= values[n-1-j] * matrix[i][j]
            values.append(matrix[i][n] / matrix[i][i])
        return reversed(values)

    def set_system(self, system):
        self.system = system
