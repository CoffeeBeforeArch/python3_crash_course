# This program shows the fundamentals of for-loops in Python3
# By: Nick from CoffeeBeforeArch

# For loops are incredibly useful for lists!
grocery_list = ["apple", "banana", "chicken", "salt", "chocolate"]

# Two useful functions are range() and len()
# Range gives us another list of variables that count up from 0
# (Can set different start, end, and stride for range(...))
print(f"Range of 5 = {range(5)}")

# Len gives us the length of a list
print(f"Length of our original list is {len(grocery_list)}")

# In a for loop, we can first generate an array containing all
# valid elements in the list, in order (range(len(grocery_lost)))
# "for i in" says go over each element in the list in order
for i in range(len(grocery_list)):
    print(f"Index {i}, Item {grocery_list[i]}")

# Alternatively, if we don't care about the index, we can just go
# over the original list, and set "item" to be the list value
for item in grocery_list:
    print(f"Item {item}")

# We can also cleanly combine these two techniques using enumerate
# Enumerate gives us both the indices and items
for i, item in enumerate(grocery_list):
    print(f"Index {i}, Item {item}")
