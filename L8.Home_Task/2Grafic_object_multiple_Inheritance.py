'''
Grafic Figures
exploring multiple inheritance
создать классы:
 графичекий объект
 прямоугольник
 кнопка для обработки нажатия мыши
Создать объект кнопки и вызвать метод нажатия на кнопку
'''

class Figure:
    color = 'White'

    def __init__(self, color="White"):
        self.color = color

    def show_color(self):
        return self.color

    def changecolor(self, ch):
        self.color = ch

class FigureClick(Figure):

    def click(self):
        self.changecolor('Blue')

class Square():
    sides = 4
    def __init__(self, w=20, h=10):
        self.widht = w
        self.height = h

    def show_sides(self):
       return self.sides


class Button(Square, FigureClick):

    def __init__(self, name_button):
        self.widht = 10
        self.height = int(len(name_button)) + 2
        self.name = name_button

print('test Button class')
b1 = Button('OK')
b2 = Button('No')
print('Sides: ', b1.show_sides())
print(Button.__mro__)
print()

print('button "b1" - before click: ', b1.color)
b1.click()
print('button "b1" - after click: ', b1.color)
print('button "b2" - no click: ', b2.color)