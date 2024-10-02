import os
import math
os.system('cls')

#^ Slide 1 & 2

#! 1. What are Python Modules?
# It is simply a file that contains Python code.
# It acts like a toolbox containing tools (such as functions, classes, variables, etc.) that you can reuse in your program.
# This approach is also called code refactoring.

#! 2. The Indian Kitchen Analogy for Python Modules.
# Think of a module like a spice box (masala dabba) in an Indian kitchen.

#^ Slide 7

#! 3. How to Use a Module?

#* 3.1 Let's start with in-built math module
import math
# Using the sqrt() function from the math module
sqrtResult = math.sqrt(16)
print(sqrtResult)

# Using the fsum() function from the math module
sumResult = math.fsum({80,20})
print(sumResult)

# Using the sin() function from the math module
sinResult = math.sin(90)
print(sinResult)

#^ Slide 8

# Using datetime time
import datetime
# Get the current date and time
current_time = datetime.datetime.now()
print(current_time)

#^ Slide 9

# Using os module
import os
# Get the current working directory
current_directory = os.getcwd()
print(current_directory)

#^ Slide 10

# Using sys module
import sys
# Get the list of command-line arguments
arguments = sys.argv
print(arguments)
print("Python Version:", sys.version_info)
sys.exit(0)

#* 3.2 Let's create our own module
# File create a file, write some code, & import it, will also print if written inside it without being used
import myNamePrintModule

# Using the variable
print(myNamePrintModule.name)

# Using the function
print(myNamePrintModule.greet("Cena"))

# Using the class
# Create an instance of the `Car` class defined in `myNamePrintModule`
my_car = myNamePrintModule.Car("BMW", "Black")
# Call the `display_info` instance method
print(my_car.display_info())  # Output: Car Model: BMW, Color: Black

# Call the static method directly from the `Bike` class defined in the module
print(myNamePrintModule.Bike.display_info("BMW", "Black"))  # Output: Bike Model: BMW, Color: Black

#^ Slide 4

#! 4. What is a Python Library?
# A collection of modules that provide tools and functions to perform specific tasks, simplifying development and reducing code duplication.

#! 5. Indian Railway System Analogy for Python Library.
# Imagine the Indian railway system.
# Each train station is like a module with specific functions. It serves a specific purpose and has its own set of functions (like boarding, ticketing, etc.)
# The entire railway system, connecting all stations, is like a library.
# It’s a collection of stations (modules) that work together to help you travel across the states/countries.
#* Similarly, a Python library is a collection of modules that work together to help you perform a specific task.

#! 6. Popular python libraries.
#* 6.1 NumPy
# - Library used for numerical computations.
# - Provides support for arrays, matrices, and mathematical functions.

#* 6.2 Pandas
# - Library used for data manipulation and analysis.
# - Provides data structures like DataFrames for handling tabular data.

#* 6.3 Matplotlib
# - Library used for creating visualizations like graphs and charts.
# - Commonly used in data science to visualize data.

#* 6.4 Requests
# - Library used for making HTTP requests.
# - Useful for interacting with web APIs and fetching data from the internet.

#^ Slide 11

#! 7. Let's get our hands on with Pandas Library.
# 7.1 First we will install "pandas"
#! pip install pandas

#* 7.2 Now we will import Pandas
import pandas as pd

#* 7.3 Let's create a DataFrame
data = {
    'Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}

#* 7.4 Create a DataFrame from the dictionary
df = pd.DataFrame(data)