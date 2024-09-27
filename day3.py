import os
os.system('cls')

# 1. What is a Function?
# 2. Indian Analogy: Auto Chapati Maker machine
# 3. How to define a function, it's syntax/indentation, & call/run it
# 4. Let's make a greet function in multiple ways

# 5. Greet function with arg
def greet1():
    print('hello')
print(greet1())

# 6. Passing arguments in functions
# 7. Greet fun with arguments
def greet2(name):
    print(f"Hello {name}, how are you?")
print(greet2("Raj"))

# 8. Passing default parameters in function
# 9. Function with default arguments
def greet3(name="Guest"):
    if(name=="Guest"):
        print("Hello, {name}, please login!")
    else:
        print(f"Hello {name}, how you doing mate?")
print(greet3())
print(greet3("Raj"))

# 10. Function with return values
def add(a,b):
    return a+b
print(add(5, 3))

# 11. Function with multiple returns
def add_sub(a, b):
    return a+b, a-b
print(add_sub(5, 3))

# 11. Scope of variables
# Global vs Local variables
x=10
def scope_demo():
    x = 20
    print(x)
print(x)

# 12. Lambda function
add = lambda a, b: a + b
print(add(5, 3))

# 13. Recursive function
def recursive_function(n):
    if n == 1:
        return 1 
    else:
        return n * recursive_function(n-1)
num = int(input('enter num '))
print(recursive_function(num))

# 14. Function overloading
# Python does not support function overloading directly.
# Python does not support function overloading in the traditional sense because it does not differentiate function signatures based on their arguments alone.
# Instead, Python can achieve a similar functionality using default arguments or by using *args and **kwargs to handle varying numbers of positional or keyword arguments.

def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

# Using default arguments
greet("Alice")               # Output: Hello, Alice!
greet("Bob", "Good morning") # Output: Good morning, Bob!

# 14.1 Using *args to handle multiple arguments dynamically
def add(*args):
    return sum(args)

print(add(1, 2, 3))       # Output: 6
print(add(1, 2, 3, 4, 5)) # Output: 15

# Using **kwargs to handle keyword arguments dynamically
def print_book_details(**kwargs):
    print("Book Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with different keyword arguments
print_book_details(title="1984", author="George Orwell")
print_book_details(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925)

# 15. Higher order function
# Higher-order functions are functions that can take other
# functions as arguments or return them. They are a key part of functional programming.

# 15.1 map(): Applies a function to all items in an input list.
# 15.2 filter(): Filters a list according to a condition.
# 15.3 reduce(): Aggregates elements in a list based on a function.

# 15.1 map
def square(x):
    return x * x
numbers = [1, 2, 3, 4]
# Applies square() to each element
squared_numbers = map(square, numbers)
# Convert map object to a list
squared_list = list(squared_numbers)
print(squared_list)

# 15.2 filter
def is_even(x):
    return x % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
# Filters only even numbers
even_numbers = filter(is_even, numbers)
# Convert filter object to a list
even_list = list(even_numbers)
print(even_list)

# 15.3 reduce
from functools import reduce
def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4]
# Multiplies all elements together
result = reduce(multiply, numbers)
print(result)

# 16. Function decoder
# A decorator wraps a function and allows you to modify or extend its
# behavior without changing its actual code. It usually defines a function that takes another function as input.
def my_decorator(func):
    def wrapper():
        print("Authenticating user....")
        print("User authenticated!")
        func()
    return wrapper

@my_decorator
def say_hello():
    print("Hello User!")
say_hello()

# 17. Function Scope and Closures
# Functions that are defined inside other functions are called nested functions.
# This means you can create a function inside another function.
# The purpose of doing this is to organize code and keep certain logic hidden or separated from the rest of the program.
# This helps keep things neat and only makes the inner function available where it's needed.

os.system('cls')
def outer_function(msg):
    def inner_function():
        print(msg)  # msg is retained in the closure
    return inner_function

my_closure = outer_function("Hello!")
my_closure()  # Outputs: Hello!
exit(0)

# Sample real life user
# def authenticate(user):
#     def check_password():
#         # Password check logic
#         return user.password == 'secure_password'
    
#     if check_password():
#         print("Access granted")
#     else:
#         print("Access denied")