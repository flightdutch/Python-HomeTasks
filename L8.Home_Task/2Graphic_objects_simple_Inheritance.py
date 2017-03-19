'''
Grafic Figures
exploring simple inheritance
'''

class Figure:
    def __init__(self, color="white"):
        self.color = color

    def changecolor(self, ch):
        self.color = ch

class Square(Figure):
    sides = 4
    def __init__(self, w=20, h=10):
        super().__init__()
        self.widht = w
        self.height = h

    def show_sides(self):
        return self.sides

print('test Square class')
s = Square(8,8)
print(Square.__mro__)
print('sides of Square: ',s.show_sides())
print('Default Parameters: ',s.color, s.widht, s.height)
s.changecolor("grey")
print('Change Parameters of object Square: ',s.color, s.widht, s.height)
print()

