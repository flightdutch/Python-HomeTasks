"""
Person Class with methods
"""

class Person:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def __len__(self):
        return self.age
    """
    "машинное" представление объекта
    __repr__ should return a printable representation of the object,
    most likely one of the ways possible to create this object.
    See official documentation: https://docs.python.org/3/library/functions.html#repr
    __repr__ is more for developers while __str__ is for end users.
    """
    def __repr__(self):
        return 'Person(name="{}", age={})'.format(self.name, self.age)

    def __str__(self):
        """
        строковое представление объекта
        Работает при:
         - print(alex)
         - str(alex)
        :return:
        """
        return self.name + ' is ' + str(self.age)

    # еще один пример спец.метода
    # bool(alex)
    # if alex: print('hello')
    def __bool__(self):
        return True

    def print_info(self):
        print(self.name, self.age)

alex = Person(name='Alex', age=17)
kate = Person(name='Kate', age=16)

print('Kate', kate)
print()
alex.print_info()           # вызываем метод. метод знает что вызывается на Alex-экземпляре класса Person
                            # в self автоматически подставляется объект на котором вызывается метод
kate.print_info()
print()
print(kate)         # use new method __repr__
print(alex)
