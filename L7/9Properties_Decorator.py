# иллюстрация механизма свойст класса
"""
Инкапсуляция
Методы
Свойства
Скрытые поля
"""

class A:
    __value = 4

    @property
    def value(self):
        print('get value')
        return self.__value 

    @value.setter
    def value(self, new_value):
        print('set value')
        self.__value = new_value


a = A()

print(a.value)  # получить доступ к полю - через метод
a.value = 10    # изменить поле - через метод

print(a.value)