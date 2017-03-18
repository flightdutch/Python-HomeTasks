
class A:
    __value = 5         # Hidden field - only for Python-core
    _val = 10       # доступное но предназанченно для использования только методами класса. извне - лучше не трогать
    # __value__ - only system value/method. don't use

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        self.__value = new_value

a = A()
# print(a.__value) # doesn't work
print(a._A__value)      # __value rename to _A__value
print()
print(a.get_value())
print()
a.set_value(34523)
print(a.get_value())
