# This program takes a file input and prints its content
# By: Nick from CoffeeBeforeArch

#import argv from the sys module
from sys import argv

# Assign the program name and command line inpuit name to variables
program_name, file_name = argv

# Open the input file, and assign "text" the file object
text = open(file_name)

# Print contents of the file
print(text.read())

# Close the file object
text.close()
