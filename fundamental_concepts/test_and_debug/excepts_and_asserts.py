# This program showcases how to handle exceptions in Python3
# By: Nick from CoffeeBeforeArch

# We use try-except blocks if we want to manage exceptions

# For out-of-bounds indexing
# Code we want to test goes in "try"
try:
    array = [1, 2, 3, 4]
    # Out of bounds!
    print(array[5])
# Each "except" block executes if that exception is thrown
except IndexError:
    print("Index 5 does not exist!")
# Default exception handling
except:
    print("All other exceptions go here!")
# "else" executes if there is no exception
else:
    print("No indexing problems!")
# "finally" executes always, and can be used for cleanup
finally:
    print("This will print in any case!")

# For accessing variables that don't exist
try:
    print(arrat)
except NameError:
    print("That variable doesn't exist!")

# For mixing incompatible types
try:
    print(7/"20")
except TypeError:
    print("You can't divide an integer by a string!")

# Opening a file that does not exist
try:
    bad_file = open("does_not_exist.txt", "r")
except IOError:
   print("Can not find that file!") 

# If we try and use something that doesn't exists
try:
    array = [1, 2, 3]
    array.appenf(4)
except AttributeError:
    print("We meant to use .append()")

# If we try a bad conversion
try:
    print(int("This can't be an int!"))
except ValueError:
    print("Casting a string to an integer doesn't work!")


# For the fairly common divide by zero error
try:
    print(10/0)
except:
    print("Raise our own exception with a message")
    raise ZeroDivisionError("We can't divide 10 by 0!")

# We don't just have to wait for an error! We can do defensive
# programming using assertions!

# Don't wait for an exception, find it ahead of time!
# Check inputs to functions or outputs
# If a function/code region takes a long time, we don't want to
# execute it wastefully if we know ahead of time it will be wrong!

grades = []
assert len(grades) != 0, "List of grades is empty!"
average = sum(grades) / len(grades)
