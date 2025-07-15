list1 = [1,2,3,2,1]
list2 = [1,2,3,4,5]
print(type(list1))
print(type(list2))
copy_list1 = list1.copy()
copy_list1.reverse()
copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list1 == list1):
    print("The List Is Palindrome")
else:
    print("The List Is Not Palindrome")


if(copy_list2 == list2):
    print("The List Is Palindrome")
else:
    print("The List Is Not Palindrome")



#next

marks = ("C","D","A","A","B","B","A")
print(marks.count("A"))

#next
marks = ["C","D","A","A","B","B","A"]
print(type(marks))
marks.sort()
print(marks)
