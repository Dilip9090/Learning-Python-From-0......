class Student:
    collage_name = "Other Collage"

    def __init__(self , name , markes):
        self.name = name
        self.marks = markes

    def welcome(self):
        print("Welcome students ,", self.name)
    
    def get_marks(self):
        return self.marks
    

s1 = Student("Raju" ,98)
s1.welcome()
print(s1.get_marks())