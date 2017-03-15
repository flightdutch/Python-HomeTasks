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

    def add_car(self, car):
        self.list_car.append(car)

    def show_cars(self):
        for i in self.list_car:
            print(i)

    def sell_car(self, car):
        # i = self.list_car.index(car)
        # print('N: ',i, self.list_car(i))
        pass

car1 = Car('Colt', 'Red', '2008', '$16000')
car2 = Car('Audi', 'Red', '1999', '$12000')
car3 = Car('Cherry')

shroom1 = ShowRoom('street 2', 'Room1')
shroom1.add_car(str(car1))
shroom1.add_car(str(car2))
shroom1.show_cars()

