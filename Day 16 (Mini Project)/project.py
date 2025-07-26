import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess The Number or Enter Quit For Quit The Game : ")
    if (userChoice == "Quit"):
        break
    userChoice = int(userChoice)
    if (userChoice == target):
        print("Sucess : Currect Guess!!")
        break
    elif (userChoice < target):
        print("You Enter Too Small Number Guess Bigger Number.....")
    else:
        print("You Enter Too Big Number Guess Smaller Number.....")  



print("----GAME OVER----")