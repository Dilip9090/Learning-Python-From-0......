ele = [1,4,9,16,25,36,49,64,81,100]

for ui in ele:
    print(ui)


#2nd question

po = (1,4,9,16,25,36,49,64,81,100)

x = 36
idx = 0
for el in po:
    if (el == x):
        print("Number Found" , idx)
    else:
        print("Not Found" , idx)
    idx += 1

for i in range(1 , 101):
    print(i)


for a in range(100 , 0 , -1):
    print(a)


n = 5 
sum = 0
while i <= n:
    sum += 1

    print(sum)


n = 5

facto = 1

i = 1

while i <= n:
    facto *= i
    i += 1

print(("Factoriam is :") , facto)