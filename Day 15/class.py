class Person:
    name = "other"


    def changeName(self,name):
        Person.name = name


p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)

