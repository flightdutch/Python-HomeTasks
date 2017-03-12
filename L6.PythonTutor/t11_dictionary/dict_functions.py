func = {
    'print': print,
    'input': input,
}

func['print'](1,2,3,4,5,6,7)
func['print']('qwerty')

# Calculator
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b != 0:
        return a / b

# Create dictionary
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

# print(operations['+'](2,5))
# print(operations['-'](2,5))
# print(operations['*'](2,5))
# print(operations['/'](2,5))

# Видоизменяем - в зав от ключа введенного юзером
while True:
    a = int(input('a: '))
    b = int(input('b: '))
    op = input('operation +-*/: ')

    if op in operations.keys():         # проверка наличия ключа
        print(operations[op](a,b))
    else:
        print('No such operation')

    if input('anykey - continue; 0 - stop:') == '0':
        break