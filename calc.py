# Простой калькулятор.

def enter_number():
    return float(input('Enter N: '))

def read_opt():
    return input('Enter operation: + - * /: ')

while True:
    s = 0
    n1 = enter_number()
    n2 = enter_number()
    op = read_opt()
    if op == "+":
        s = n1 + n2
    elif op =="-":
        s = n1 - n2
    elif op == "*":
        s = n1 * n2
    elif op == "/":
        s = n1 / n2
    else:
        print('Enter option as you need: + - * /. After - press enter')
        continue
    print('n1 ' + op + ' n2 = ' + str(s))
    r = int(input('If you want stop - enter 0 : '))
    if r == 0:
        break

