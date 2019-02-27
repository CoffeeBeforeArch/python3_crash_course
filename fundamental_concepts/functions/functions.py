# This program shows off functions in Python3
# By: Nick from CoffeeBeforeArch

# Print with no arguments
def print_none():
    print("No arguments")

# Print 1 argument
def print_one(arg1):
    print(arg1)

# Prints 2 arguments
def print_two(arg1, arg2):
    print(arg1, arg2)

# Prints any number of arguments
def print_any(*args):
    # Print out the array of inputs
    print(args)
    arg1, arg2, arg3 = args
    print(arg1, arg2, arg3)

# Call a function with no arguments
print_none()

# Call a function with 1 argument
print_one("This is a single argument print")

# Call a function with 2 arguments
print_two("Arguement 1", "Argument 2")

# Call a function with a variable number of arguments
print_any("Arg1", "Arg2", "Arg3")
