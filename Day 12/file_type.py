f = open("demo.txt" , "w")

f.write("Now We Change The File Data")

f.close()


f = open("demo2.txt" , "a")

f.write("i am adding data in old file")

f.close()


f = open("demo3.txt" , "a")

f.write("i am adding data in new file")

f.close()


f = open("demo.txt" , "w+")
print(f.read())
f.write("abc")


f.close



