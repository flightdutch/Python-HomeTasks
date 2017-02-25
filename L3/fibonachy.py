# функция рекурсивного нахождения n-го числа фиббоначи

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n

def main():
    n = int(input('Enter your Number - from 1 to 100: '))
    f = factorial(n)
    print('Factorial number {} = {} '.format(n, f))

#if __name__ == '__name__':
main()
