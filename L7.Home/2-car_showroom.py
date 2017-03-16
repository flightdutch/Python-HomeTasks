class Car:

    def __init__(self, new_model, new_color='Black', new_year='1900', new_price='$1'):
        self.model = new_model
        self.color = new_color
        self.year = new_year
        self.price = new_price

    def __str__(self):
        return (self.model + ' ' + self.color + ' ' + self.year +' ' + self.price)

    def __list__(self):
        return (self.model + ' ' + self.color + ' ' + self.year + ' ' + self.price)

class ShowRoom(Car):

    def __init__(self, new_address, new_name):
        self.addr = new_address
        self.name_showroom = new_name
        self.list_car = []

    def __str__(self):
        return ('ShowRoom: ' + self.name_showroom + ' ' + self.addr + ': ' + str(len(self.list_car)) + ' cars'  )


    def add_car(self, car):
        self.list_car.append(car)

    def show_cars(self):
        for item in self.list_car:
            print(item)

    def sell_car(self, car):
        i = self.list_car.index(car)
        sold_car = self.list_car.pop(i)
        print('Sold car: ',sold_car)


car1 = Car('Colt', 'Red', '2008', '$16000')
car2 = Car('Audi', 'Red', '1999', '$12000')
car3 = Car('Cherry')
car4 = Car('VW', 'Black')

shroom1 = ShowRoom('street 2', 'Room1')
shroom1.add_car((car1))
shroom1.add_car((car2))
shroom1.add_car((car3))
shroom1.add_car((car4))

print(str(shroom1))
print('исходное состояние склада')
shroom1.show_cars()
print()
shroom1.sell_car(car1)
print()
print('остаток после продажи')
shroom1.show_cars()

