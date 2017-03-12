# В Python поля и методы обычно называются общим термином атрибуты.
# Статические атрибуты могут быть перегружены в экземпляре.
# Атрибуты экземпляра определяются не в структуре класса, а в методах (например, конструкторе).
# Атрибуты, доступ к которым управляется отдельными методами, называются свойствами
# (синтаксически доступ к атрибутам и свойствам идентичен):
# атрибуты имена которых начинаются и заканчиваются двумя знаками подчеркивания -
# внутренние атрибуты для Питона и задают особые свойства объекта:
# __doc__ - документационная строка
# __class__ - атрибут в которм хранится класс данного объекта
# Методы со спец.именами - "магические методы" - задают особое поведение объектов
# и позволяют переопределять поведение встроенных функций и оператолров для эекземпляров данного класса
# __init__ - конструктор

class Complex:
    '''
    Комплексное число
    '''

    def __init__(self, real=0.0, imaginary=0.0):
        """
        Конструктор класса
        :param real:
        :param imaginary:
        """

        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        """
        Метод __repr__ возвращает строковое представление объекта, которое,
        если это возможно, должно быть корректным выражением, создающим
        аналогичный объект, иначе содержит его описание;
        собственно - програмное представление объекта: что это за об]ект и как он был создан
        в идеале - метод должен возвращать что-то подо,ное конструктору
        вызывается функцией repr
        :return:
        """
        #return 'Complex(%g, %g)' % (self.real, self.imaginary) - старое форматирование строк
        return 'Complex({}, {})'.format(self.real, self.imaginary)

    def __str__(self):
        """
        Метод __str__ возвращает предназначенное для человека строковое
        представление объекта;
        вызывается функциями: str, print, format
        :return:
        """
        return '%g %c %gi' % (self.real, '+' if self.imaginary >= 0 else '-', abs(self.imaginary))

    # Арифметические операции
    def __add__(self, other):
        """
        Method __add__ определяет операцию сложения
        :param other:
        :return:
        """
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __neg__(self):
        """
        Negation operation
        :return:
        """
        return Complex(-self.real, -self.imaginary)

    def __sub__(self, other):
        """
        Операция вычитания.
        Сложение и отрицание уже определены,
        поэтому - вычитание можно определить через них
        """
        return self +(-other)

    def __abs__(self):
        """
        Модуль числа
        """
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    # Операции сравнения

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        return not (self == other)

def main():
    x = Complex(2, 3.5)
    print(repr(x))
    print('x = ', x)
    print(str(x))
    print()

    y = Complex(5, 7)
    print('y = ', y)
    print()

    print('x + y = ', x + y)
    print('x - y = ', x - y)
    print()

    print('|x| = ', abs(x))
    print('x == y = ', x == y)
    print()

if __name__ == '__main__':
    main()