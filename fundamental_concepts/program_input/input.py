# This program shows off the input() function of Python
# By: Nick from CoffeeBeforeArch

# Ask the user for a number, and use the input() function to get it
print("Pick your favorite number: ")
number = input()
print(f"Your favorite number is {number}")

# Have the input on the same line as the question
print("Pick your second favorite number:", end = ' ')
number = input()
print(f"Your second favorite number is {number}")

# Get rid of print altogether
number = input("What is your third favorite number? ")
print(f"Your third favorite number is {number}")

# Print out the type of the input
print(type(number))
