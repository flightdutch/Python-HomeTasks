# simple calculator

def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def div(a,b):
    return a/b

def min(a,b):
    return a - b

operators = {
    '+': add,
    '-': min,
    '*': mul,
    '/': div,
}

def main():
    while True:
        try:
            a = float(input('a: '))
            b = float(input('b: '))
            op = input('what do you want: +,-,*,/: ')
            print(operators[op](a, b))
        except ValueError:
            print('value error for: a or b')
        except KeyError:
            print('type error for option - only: +, -, *, / ')
        except ZeroDivisionError:
            print('Attempt to divide by Zero')
        except ArithmeticError:
            print('Arithmetic error that occur for numeric calculation')

        if (input('stop - 0; continue - anykey')) == '0':
            break

if __name__ == "__main__":
    main()
