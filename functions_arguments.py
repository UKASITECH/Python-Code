def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Umang", 14)  # Positional arguments
print("You are now a great person and you are now a Coder.")

greet(age=25, name="Alice")  # Keyword arguments

def greet(name, age=18):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice")  # Uses default value for age
greet("Bob", 30)  # Overrides default value


def add_numbers(*args):
    total = sum(args)
    print(f"The sum is: {total}")

add_numbers(1, 2, 3, 4)  # Pass multiple arguments


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, country="USA")  # Pass multiple keyword arguments
