# This is a sample module containing a print, a variable, a function, and a class.

#! Normal Print
print("My name is Raj.")

#! Storing a name in a variable
name = "Raj"

#! Printing name by function
def greet(name):
    return f"Hello, {name}!"

#! Class
#* Approach 1: Instance Method with `self`
class Car:
    def __init__(self, model, color):
        # Instance attributes unique to each object
        self.model = model
        self.color = color

    # Instance method using `self` to access instance attributes
    def display_info(self):
        return f"Car Model: {self.model}, Color: {self.color}"
    
#* Approach 2: Static Method without `self`
class Bike:
    @staticmethod
    def display_info(model, color):
        # No `self`, the method takes parameters directly
        return f"Bike Model: {model}, Color: {color}"