# This program shows off common string-related operations in Python3
# By: Nick from CoffeeBeforeArch

from sys import argv

name, csv_string = argv

# Make a string variable
s = "Test string"

# Print the first 4 characters using a slice
# T e s t   s t r i n g
# 0 1 2 3 4 5 6 7 8 9 10
print(s[0:4:1])

# Print the remainder of a string
print(s[5:])

# Split the spring into an array of strings
s = s.split(" ")
print(s)

# Combine the stings back together
s = " ".join(s)
print(s)

# This come in handy working with data formatted as CSV
print(csv_string)
csv_string = csv_string.split(",")
print(csv_string)

# Make the entire string uppercase
s = s.upper()
print(s)

# Make the entire string lowercase
s = s.lower()
print(s)
