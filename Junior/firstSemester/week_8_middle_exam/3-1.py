class Calc :
    def __init__(self, n):
        self.a = n

    def plus(self, value):
        print(self.a, '+', value, '=', self.a + value)

    def mult(self, value):
        print(self.a, '*', value, '=', self.a * value)


my = Calc(3)
my.plus(7)
my.mult(10)
