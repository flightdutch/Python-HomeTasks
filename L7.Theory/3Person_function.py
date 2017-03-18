"""
Person Class with function - method
"""
def print_info(person):
    print(person.name,person.age)

class Person:
    #def __init__(self):
    pass

# функцию делаем методом
# на этапе выполнения
Person.print_info = print_info

# Создает объект alex - екземпляр класса Person
alex = Person()
# Созадем атрибуты объекта (переменные)
alex.name = 'Alex'
alex.age = 17

# class работает по принципу словаря:
#  - если чего то нет - добавить
# - если это уже есть - изменить
kate = Person()
kate.name = 'Kate'
kate.age = 16

print('Kate', kate)
print_info(kate)
print_info(alex)
print()

alex.print_info()   # метод занет что вызывается на Alex

# print(kate.name, 'is: ', kate.age, 'max: ', kate.max_age)
# print(alex.name, 'is: ', alex.age, 'max: ', alex.max_age)

