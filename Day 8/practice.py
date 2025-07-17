i = 1
while i <= 100:
    print(i)
    i += 1


w = 100
while w >= 1:
    print(w)
    w -= 1



i = 1
while i<=10:
    print(5*i)
    i += 1




numbers = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(numbers):
    print(numbers[idx])
    idx += 1



all = (1,4,9,16,25,36,49,64,81,100)

x = print(int(input("Enter Value Which Want To Find : ")))
d = 0
while d < len(all):
    if (all[d] == all):
        print("Found", d)
    else:
        print("Not Found" , d)
    d += 1