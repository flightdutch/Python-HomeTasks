
class Car:
    # name = 'NoName'
    # color = 'Black'
    # year = '1900'
    # price = '$1'

    def __init__(self, new_model, new_color='Black', new_year='1900', new_price='$1'):
        self.model = new_model
        self.color = new_color
        self.year = new_year
        self.price = new_price

    def __str__(self):
        return (self.model + ' ' + self.color + ' ' + self.year +' ' + self.price)

car1 = Car('Colt', 'Red', '2008', '$16000')
car2 = Car('Audi', 'Red', '1999', '$12000')
car3 = Car('Cherry')

print(str(car1))
print(str(car2))
#print(car3.str())
