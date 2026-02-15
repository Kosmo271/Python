mytuple = ()
print (mytuple)
#tuple is non-changing after it's set

mytuple = (10, 11, 13, "Hello")
print (mytuple)

mytuple=("number", [1,7,5], (10,2,3))
#nested tuple     #list       #tuple

mytuple=("A","R","Y","A","N")
print("What is the first letter:", mytuple[0])

n_tuple=("number", [1,7,5], (10,2,3))
print(n_tuple [0][5])
print(n_tuple [2][1])

print("Slice:", mytuple[1:3])

for letter in (mytuple):
    print("Hello", letter)