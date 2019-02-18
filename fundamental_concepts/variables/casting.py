# This program shows how to convert data types in python
# By: Nick from CoffeeBeforeArch

# Declare and initialize some floats
a = 4.5
b = 5.3

# Print them as integers (casting rounds down)
print(int(a), int(b))

# Another division example
c = 10
d = 4

# Division of integers returns only the quotient
print(c / d)

# Cast as a float to get the result as a decimal
# float(c / d) doesn't work because it only casts the result 
# (the quotient) as a floating point number
print(float(c) / float(d))
