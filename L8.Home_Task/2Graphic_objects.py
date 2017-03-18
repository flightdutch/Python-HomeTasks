class Figure:
    def __init__(self, color="white"):
        self.color = color

    def changecolor(self, ch):
        self.color = ch


class FigureClick(Figure):

    def click(self):
        self.changecolor('Blue')


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

class Button(FigureClick):

    def __init__(self, name_button):
        self.color = 'Grey'
        self.widht = 10
        self.height = int(len(name_button)) + 2
        self.name = name_button


print('test Square class')
s = Square(8,8)
s.howsides(4)
s.outsides()
s.changecolor("grey")
print(s.color, s.widht, s.height)
print()

print('test Button class')
b1 = Button('OK')
b2 = Button('No')
print('button before click: ', b1.color)
b1.click()
print('button after click: ', b1.color)