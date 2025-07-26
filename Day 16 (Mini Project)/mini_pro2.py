# #check if number is even/odd , positive/nagative
num = int(input("Enter The Number : "))
print(num)


if (num >= 0):
    print("The" , num , "Is Positive Number")
if(num % 2 == 0):
    print("This Number Is Even Number")
elif(num % 2 != 0):
    print("The Number Is Odd")
else:
    print("The" , num , "Is Nagative Number")






# #print 1 to 50 reverse string

str = ("1,2,3,4,5,6,7,8,9,10")

reversed= str[::-1]
print(reversed)


# read from other file and write to other file
f = open("write.txt" , "r")
f.seek(0)
f.read()
content = f.read()
f.seek(0)
print(content)
f = open("write.txt" , "w")
f.write(content)

f.close()


#don't Forget To Save The txt File After Writing Something
with open('read.txt' , 'r') as f:
    f.seek(0)
    write = f.read()
    print(write)

with open("writing.txt" , "w") as file:
    file.write(write)
    # print(save)
    file.seek(0)
