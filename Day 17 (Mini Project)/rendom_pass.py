import random
import string
pas = 12
print(string.ascii_letters)
print(string.punctuation)
print(string.digits)
val = string.ascii_letters + string.punctuation + string.digits


password ="\n"
for i in range(pas):
    password += random.choice(val)

print("Your random Password is : " , password)


with open("save.txt" , "a") as f:
    f.write(password)
