class Argument:
    def __init__(self, fx, str):
        self.fx = fx
        self.str = str

    def f(self, x):
        return self.fx(x)

    def to_str(self):
        return self.str

