class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello ")

    def Welcome(self):
        self.__hello

p1 = Person()

print(p1.Welcome())