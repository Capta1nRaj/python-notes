import os
os.system('cls')

# 1. If else based on weather condition
weatherCondition = 'Cold'
if(weatherCondition == 'Raining'):
    print("Dont' go outisde")
elif(weatherCondition == 'Sunny'):
    print("Go outside & play")
elif(weatherCondition == 'Cold'):
    print("Wear jacket before going outside!")
else:
    print("Error in fetching the data!")

# 2. Looping through a list
fruits = ["apple", "banana", "cherry"]

# 2.1. Looping all data using for loop
for fruit in fruits:
    print(fruit)

# 2.2. Looping all data using for loop but till a specific range
for fruit in range(2):
    print(fruits[fruit])

# 2.3 Loop through keys and values
person = {"name": "John", "age": 30, "city": "New York"}

for key, value in person.items():
    print(f"{key}: {value}")
