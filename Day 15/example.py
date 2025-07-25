class A:
    varA = "Welcome To Class A"

class B:
    varB = "Welcome To Class B"

class C(A , B):
    varC = "Welcome To Class C"


c1 = C()


print(c1.varC)
print(c1.varB)
print(c1.varA)





#Example 2

class Car:
    def __init__(self , type):
        self.type = type

    colour = "white"
    @staticmethod
    def start():
        print("Car Started......")

    @staticmethod
    def stop():
        print("Car Stoped.....")



class ToyotaCar(Car):
    def __init__(self , name , type):
        self.name = name
        self.type = type
        super().__init__(type)
        super().start



car1 = ToyotaCar("fortuner" , "Electric")
print(car1.type)
print(Car.start())
