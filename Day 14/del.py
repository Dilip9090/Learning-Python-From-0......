class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age



s1 = Student("Deep" , 16)
print(s1.name)
print(s1.age)

# del s1.name
# print(s1.name)








class Account:
    def __init__(self , account_no , acc_pas):
        self.account_no = account_no
        self.__acc_pas = acc_pas


acc1 = Account("12345" , "abcde")
print(acc1.account_no)
print(acc1.__acc_pas)