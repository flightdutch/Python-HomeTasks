# Classes. Классы. Наследование в ООП.
# Напишите программу, где класс «геометрические фигуры» (figure)
# содержит свойство color с изначальным значением white и метод для изменения цвета фигуры,
# а его подклассы «овал» (oval) и «квадрат» (square) содержат методы __init__
# для задания начальных размеров объектов при их создании.

class Figure:
    def __init__(self, w="white"):
        self.color = w

    def changecolor(self, ch):
        self.chcolor = ch


class Oval(Figure):
    def __init__(self, r, x, y):
        self.radius = r
        self.ox = x
        self.oy = y

    def out(self):
        print(self.radius, self.ox, self.oy)


class Square(Figure):
    def __init__(self, w, h):
        self.widht = w
        self.height = h

    def howsides(self, n):
        if not n == 4:
            print("It is not a sguare")
        else:
            self.sides = n

    def outsides(self):
        print(self.sides)


x = Figure("red")
print(x.color)

o = Oval(5, 0, 0)
o.out()
o.changecolor("black")
print('Oval: ', o.chcolor, o.radius)

s = Square(8, 8)
s.howsides(4)
s.outsides()
s.changecolor("grey")
print('Square: ',s.chcolor, s.widht, s.height)