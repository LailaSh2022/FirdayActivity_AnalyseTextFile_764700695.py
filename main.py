print("My First app using Python")
print("NewZealand")
print(3*"\n")
print("Canada")
print("Australia")
print("Python", end='!' "\n")
a = "Gest"
b = 100
print(a + str(b))

f = 101     # Global variable
print(f)
# Creating function
def firstFunction():
    f = "f inside the function"     # Local variable
    print(f)
firstFunction()
print(f)

f = 99
print(f)
del f           # Delete f
print(f)        # Giving an error because of deleting the variable
