# This program shows off dictionaries in python
# By: Nick from CoffeeBeforeArch

# Storing data in two lists is inconvenient. Take the case of students
# and their grades
students = ["Andy", "Michelle", "Bob", "Kyle", "Mollie"]
grades = ["C", "B", "B", "D", "A"]

# Replace with a dictionary that uses key-value pairs
# Lists are a subset of dictionaries that use integers as the key
my_dict = {}
my_dict["Andy"] = "C"
my_dict["Michelle"] = "B"
my_dict["Bob"] = "B"
my_dict["Kyle"] = "D"
my_dict["Mollie"] = "A"

print(my_dict["Bob"])
print(my_dict["Mollie"])

# We can test if a value is in a dictionary
print("Kyle" in my_dict)

# And we can remove an entry
del(my_dict["Kyle"])

# Make a new dictionary and fill it in one line
cars = {"Bill":"Chevrolet", "Nancy":"Toyota", "Chris":"BMW"}

# We can get all keys/value from a dictionary as well
# This is not guaranteed to be ordered!
print(cars.keys())
print(cars.values())
