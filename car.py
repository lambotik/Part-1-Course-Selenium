class Car():
    """Create class car"""
    def __init__(self, model, year, engine_volume, price, mileage):
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def car(self):
        """Create car"""
        print('Car name: ' + self.model + '\nYear of issue:' + str(self.year) + '\nEngine volume: ' + str(
            self.engine_volume) + '\nPrice: ' + str(self.price) + '$' + '\nMileage: ' + str(
            self.mileage) + 'km' + '\nWheels: ' + str(self.wheels))

class Truck(Car):
    """Get attribute of parent class"""
    def __init__(self, model, year, engine_volume, price, mileage):
        super().__init__(model, year, engine_volume, price, mileage)
        self.wheels = 8
    def truck_description(self):
        description = 'Car name: ' + self.model + '\nYear of issue:' + str(self.year) + '\nEngine volume: ' + str(
            self.engine_volume) + '\nPrice: ' + str(self.price) + '$' + '\nMileage: ' + str(
            self.mileage) + 'km' + '\nWheels: ' + str(self.wheels)
        print('Truck ' + description)



# volvo = Car('Volvo', 2022, 5.0, 50000, 12000)
# volvo.car()
mac = Truck('Mac', 2000, 5.5, 70000, 600000)
mac.truck_description()