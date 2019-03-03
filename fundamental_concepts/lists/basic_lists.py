# This program shows off the basics of lists in Python3
# By: Nick from CoffeeBeforeArch

# Make a list variable
example_list = []

# Add three different data types to the list
example_list.append("Hello")
example_list.append(1)
example_list.append(True)

# Print out the list
print(f"Contents of list {example_list}")

# Print out the list length and individual elements
print(f"Size of list {len(example_list)}")
print(example_list[0])
print(example_list[1])
print(example_list[2])

# Clear the list and print out the size again
example_list.clear()
print(f"New size of list {len(example_list)}")

# Create a new list of only integers
example_list = [4, 2, 21, 19, 45, 5]

# Sort the list
example_list.sort()

# Print the sorted list
print(f"Sorted list {example_list}")

# Reverse the newly sorted list
example_list.reverse()

# Reverse the list
print(f"Reversed list {example_list}")

# Remove the last element of the list
example_list.pop()
print(f"Removed last element {example_list}")

# Insert into a specific location of the list
example_list.insert(1, 10)
example_list.insert(3, 10)
example_list.insert(5, 10)
print(f"Insert 3 elements of 10 {example_list}")

# Check how many times 10 is in the list
print(f"There are {example_list.count(10)} 10s in the list")

# Remove the first 10 found each time
print(f"Removing 10 from position {example_list.index(10)}")
example_list.remove(10)
print(example_list)
print(f"Removing 10 from position {example_list.index(10)}")
example_list.remove(10)
print(example_list)
print(f"Removing 10 from position {example_list.index(10)}")
example_list.remove(10)
print(example_list)
