"""
Person Class with function - method
"""
# def print_info(person):
#     print(person.name,person.age)
# функцию делаем методом на этапе проектирования
class Person:
    #def __init__(self):
    def print_info(self):
        print(self.name, self.age)

# Создаем объект alex - екземпляр класса Person
alex = Person()
# Созадем атрибуты объекта (переменные)
alex.name = 'Alex'
alex.age = 17

# class работает по принципу словаря:
#  - если чего то нет - добавить
# - если это уже есть - изменить

# Создаем екземпляр  kate
kate = Person()
kate.name = 'Kate'      # атрибут
kate.age = 16

print('Kate', kate)
print()
alex.print_info()           # вызываем метод. метод знает что вызывается на Alex-экземпляре класса Person  
                            # в self автоматически подставляется объект на котором вызывается метод
Person.print_info(alex)     # вызываем метод. классу надо указать что запрашиваем объект alex
