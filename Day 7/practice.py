dict1 = {
    "cat" : "a small animal",
    "table" : ["a pice of furniture"  , "list of facts" ]
}

print(dict1)




subjects = {
    "pythone" , "java" , "c++" , "javascripts" , "pythone" , "pythone" , "java"
}

print(len(subjects))


marks = {}

phy = int(input("enter your phy marks : "))
java = int(input("enter your java marks : "))
c = int(input("enter your c marks : "))

print(marks)

marks.update({"phy" : phy})
marks.update({"java" : java})
marks.update({"c" : c})

print(marks)