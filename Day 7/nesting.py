student = {
    "name" : "pankaj bhai" , 
    "subjects" :{
        "hindi" : "75" ,
        "gujrati" :"89" ,
        "english" : "67"
    } 
}

print(student["subjects"]["gujrati"])

print(student.keys())
print(len(student))

print(student.values())

print(student.items())

print(student.get("name"))

new_dict = {"rollno" : "21"}
student.update(new_dict)

print(new_dict["rollno"])