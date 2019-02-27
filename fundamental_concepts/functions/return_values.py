# This program shows off return values in Python3
# By: Nick from CoffeeBeforeArch

# Compute addition and return the sum
def add(a, b):
    return a + b

# Compute subtraction and return the difference
def sub(a, b):
    return a - b

# Compute multiplication and return the product
def mul(a, b):
    return a * b

# Compute division and return the quotient (and remainder)
def div(a, b):
    return a / b

# Call add(...) and print result
print(f"5 + 3 = {add(5, 3)}")

# Call sub(...) and print result
print(f"10 - 5 = {sub(10, 5)}")

# Call mul(...) and print result
print(f"5 * 5 = {mul(5, 5)}")

# Call div(...) and print result
print(f"10 / 20 = {div(10, 20)}")
