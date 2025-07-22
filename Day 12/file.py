f = open("demo.txt" , "rt")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("demo.txt" , "rt")
data = f.read(5)
print(data)
print(type(data))
f.close()


f = open("demo.txt" , "rt")
line1 = f.readline()
print(line1)
print(type(line1))
f.close()


#this i create for use the deleting command
f = open("demo4.txt" , "w")
delta = f.read()
print(delta)
f.close()