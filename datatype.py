name = "Aryan"
age = 15
is_student = True
weight = 38.5 #Float

#How to find data type in python
print("Data Type of Name is", type(name))
print("Data Type of of weight is", type(weight))
print("The age is :", age)


print("before typecasting")
print("Data Type of age is", type(age))
print()

print("after typecasting")
newage = int(age)
print("Data Type of age is" , type(newage))