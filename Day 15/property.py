class Student:
    def __init__(self , phy , chem , math):
        self.phy = phy
        self.chem = chem
        self.math = math

        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"



stu1 = Student(89 , 70 , 90)

print(stu1.chem)
print(stu1.math)
print(stu1.phy)
print(stu1.percentage)