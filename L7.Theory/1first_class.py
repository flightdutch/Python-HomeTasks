class CustomClass:
    pass

print()
print('CustomClass: ',CustomClass)
print()
obj = CustomClass()
print('obj: ', type(obj))
print()

MyClass = CustomClass
print('MyClass: ',MyClass)
obj2 = MyClass()
print('obj2',type(obj2))
print()

# isinstance() - принадлежит нечто указанному объекут/классу
print('1,int: ',isinstance(1,int))
print('obj: ', obj)
print('obj is MyClass: ', isinstance(obj, MyClass))
print('obj is CustomClass: ', isinstance(obj, CustomClass))
print()