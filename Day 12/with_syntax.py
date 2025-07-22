# with open("demo.txt" , "r") as f:
#     deta = f.read()

# print(deta)



# with open("demo.txt" , "w") as f:
#     deta = f.write("new deta")

# print(deta)


# # import os
# # os.remove("demo4.txt")



# #practice time creating file 
# f = open("practice.txt" , "w")
# read = f.write("Hi Everyone\nWe Are Learning File I/O\nusing Java\nI like programming in Java")
# f.close()


# with open("practice.txt" , "r") as f:
#     demo = f.read()

# new_data = demo.replace("Java" , "Pythone")

# print(new_data)


# with open("practice.txt" , "w") as f:
#     f.write(new_data)


# word = "Learning"
# with open("practice.txt" , "r") as f:
#     dop = f.read()
#     if(dop.find(word) != -1):
#         print("found")
#     else:
#         print("not found")



# def check_for_line():
#     word = "Learning"
#     deta = True
#     line_no = 1
#     with open("practice.txt" , "r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#                 line_no += 1


# print(check_for_line)



count = 1
with open("practice.txt" , "w") as f:
    deta = f.write("1,2,3,76,84,90,101")
    print(deta)

with open("practice.txt" , "r") as f:
    delta = f.read()
    print(delta)


nums = delta.split(",")
for val in nums:
    if (int(val) %2 == 0):
        count += 1

print(count)