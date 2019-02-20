# This program shows off f-strings in Python 
# By: Nick from CoffeeBeforeArch

# Save a normal string to a variable
normal_string = "hello there!"
# Save and f-string to a variable
f_string = f"Look how I can automatically say, {normal_string}"

# Print both the normal and f-string
print(normal_string)
print(f_string)

# Save an f-string with a variable decided upon later
empty_f_string = "Is this a valid f-string? {}"

# Print the empty f-string and specify the missing variable
print(empty_f_string.format(True))

# Combining two strings is simple. Just use the + operator
first_half = "We can combine the first half of the string "
second_half = "with a second half!"

# Print concatenated strings
print(first_half + second_half)
