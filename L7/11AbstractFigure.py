
class AbstractFigure:
    def __init__(self, size):
        self.size = size

    def print(self):
        raise NotImplementedError

class Triangle(AbstractFigure):

    def print(self):
        for _ in range(self.size + 1):
            print('*' * _)

class Square(AbstractFigure):

    def print(self):
        for _ in range(self.size + 1):
            print('*' * self.size)

class Cat:
    def print(self):
        print('MEAW')

t = Triangle(5)
t.print()
print()
s = Square(5)
s.print()

figures =[
    Square(4),
    Triangle(6),
    Square(7),
    Square(3),
    Triangle(3),
    Cat(),
]

for figure in figures:
    figure.print()      # эффект - утиная типизация (если это выглядит как утка, плавает как утка и крякает как утка -> это утка)
                        # работаем с разными типами объектов но имеющих одинаковые наборы свойств/методов
                        # тоесть - мы привязываемся к  интерфейсу/методам/полям разных типов/классов данных
    print()