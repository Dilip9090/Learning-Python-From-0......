def len_of_list(a):
    print(len(a))


d = [1,2,3,4,5,6,7,8,9]

len_of_list(d)
print(type(d))



def print_list(lists):
    for item in lists:
        print(item, end=" ")


g = [4,5,7,7,9,0,2,3,4,6]
h = [67,8,9,9,7,6,5,4,4]

print_list(g)
print_list(h)



def calculate_fac(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)


calculate_fac(5)



def conveter (usd_value):
    inr_val = usd_value * 83
    print(usd_value, "USD = " ,inr_val, "inr")


   
   
pop = conveter(10)
print(pop)