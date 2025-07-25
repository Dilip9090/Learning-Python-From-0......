class Car:
    colour = "white"
    @staticmethod
    def start():
        print("Car Started......")

    @staticmethod
    def stop():
        print("Car Stoped.....")



class ToyotaCar(Car):
    def __init__(self , brand):
        self.brand = brand


car1 = ToyotaCar("fourtuner")
car2 = ToyotaCar("Prius")


print(car1.name)
print(car2.name)

print(car1.start())

print(car1.colour)