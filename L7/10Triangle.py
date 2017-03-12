"""
Figures
"""

class Triangle:
    __symb = '*'
    def __init__(self, size):
        self.size = size

    def print_figure(self):

        for i in range(self.size + 1):
            print(self.__symb * i)

    def change_symb(self, new_s):
        self.__symb = new_s

t1 = Triangle(5)
t1.change_symb('^')
t2 = Triangle(10)

t1.print_figure()
print()

t2.print_figure()
