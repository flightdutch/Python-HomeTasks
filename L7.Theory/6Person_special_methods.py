"""
Person Class with methods
"""
import time

class Person:
    def __init__(self, name, age ):     # встроенная функция для инициализации экземпляра класса
        self.name = name
        self.age = age
        self.b_time = time.time()

    def __len__(self):
        return self.age

    # def __repr__(self):
    #     return 'class is - test repr'

    def print_info(self):
        print(self.name, self.age)

alex = Person(name='Alex', age=17)
kate = Person(name='Kate', age=16)

print('Kate', kate) # работает repr - возращает предаствление объекта
print(alex)
# если удалить - закоментить метод __repr__
# будет стандартное поведение print(alex) - возращет ссылку на экземпляр класса

print()
alex.print_info()
kate.print_info()
print(alex.b_time)
print(alex)
print(len(alex))        # аналог функции len для объектов list/string
print(len(kate))
