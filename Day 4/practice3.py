num1 = int(input("Enter The First Number :"))
num2 = int(input("Enter The Second Number :"))
num3 = int(input("Enter The Third Number :"))

if(num1 >= num2 and num1 >= num3):
    print("The" , num1 , "Is Gratest Number")
elif(num2 >=num3 ):
    print("The" , num2 , "Is Gratest Number")
else:
    print("The" , num3 , "Is Gratest Number")