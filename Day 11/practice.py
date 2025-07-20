# def cal_sum(n):
#     if (n == 0):
#         return 0
#     return cal_sum(n-1) + n



# sum = cal_sum(5)

# print(sum)



def print_list(list , idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list , idx+1)


fruits = ["mango","banana","apple","kiwi"]
print_list(fruits)