# Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
# По данному натуральному n вычислите значение n!. 
# Пользоваться математической библиотекой math в этой задаче запрещено. 

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n

print(factorial(10))

def factorial2(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
        print(fact)
    return fact

print(factorial2(10))