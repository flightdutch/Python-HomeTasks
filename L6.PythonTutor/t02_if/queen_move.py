# Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
# Даны две различные клетки шахматной доски,
# определите, может ли ферзь попасть с первой клетки на вторую одним ходом.


while True:
    x1 = int(input('x1: '))
    y1 = int(input('y1: '))
    x2 = int(input('x2: '))
    y2 = int(input('y2: '))

    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        print("YES")
    else:
        print("NO")

    if input('anykey - continue; 0 - stop:' ) == '0':
        break
