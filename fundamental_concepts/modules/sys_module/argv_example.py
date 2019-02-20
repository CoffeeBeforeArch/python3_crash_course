# This example imports argv from the sys module to take command line 
# inputs
# By: Nick from CoffeeBeforeArch

# From the sys module import argv
from sys import argv

# Unpack the arguments into unique variables
one, two, three = argv

print(argv)
print("Arguement one is: ", one)
print("Arguement two is: ", two)
print("Arguement three is: ", three)
