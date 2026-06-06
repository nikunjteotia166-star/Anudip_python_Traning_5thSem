# to create a dictionary to store students data-----
students = {"std101" : "akash" , "std102" : "abhinav" , "std103" : "anil" , "std104" : "rahul"}

# to display the data
print("student details :")
print(students)
print("---------------------------------")
# to update record of students whose roll no is std103
students["std103"] = "rohit"
# to update record of student whose roll no is std105
students["std105"] = "rakesh"
print("student details :")
print(students)
print("-----------------------------------")
for x in students:
    print(x , '->' , students[x])