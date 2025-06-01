# Classes and Objects in Python
class buisness:
    def employee(x):
        x.name = input("Enter the name of the employee: ")
        x.age = int(input("Enter the age of the employee: "))
        x.salary = int(input("Enter the salary of the employee: "))


buisness = buisness()
print(buisness.employee())
print("Name of the employee: ", buisness.name)

# Constructor in Python
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name  # Initialize attributes
        self.age = age

# Creating an object
p1 = Person("Alice", 25)

print(p1.name)  # Output: Alice
print(p1.age)   # Output: 25

# Decorators in Python

def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function call
# Hello!
# After the function call

# Access Modifiers in Python
class Example:
    public_var = "Public"
    _protected_var = "Protected"
    __private_var = "Private"

e = Example()
print(e.public_var)      # Accessible
print(e._protected_var)  # Accessible but should not be used outside the class
# print(e.__private_var) # Error: Attribute not accessible



        
