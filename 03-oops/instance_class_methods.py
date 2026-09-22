# Instance methods use an object; class methods use the class.
class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        return f"Driving a {self.brand}."

    @classmethod
    def info(cls):
        return f"This car class has {cls.wheels} wheels."

car = Car("Toyota")
print(car.drive())
print(Car.info())
