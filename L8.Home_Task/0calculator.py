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
            a = int(input('a: '))
            b = int(input('b: '))
        except:
            print('error value: a or b')
            return None

        op = input('what do you want: +,-,*,/: ')

        print(operators[op](a,b))

        if (input('stop - 0; continue - anykey')) == '0':
            break

if __name__ == "__main__":
    main()