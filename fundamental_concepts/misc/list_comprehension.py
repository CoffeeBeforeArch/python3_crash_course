# This program shows off the basics of list comprehension in Python3
# By: Nick from CoffeeBeforeArch

# Sometimes we want a concise was to create lists
# For example, let's create a list of numbers from 1-10
# but squared
simple_list = []

for i in range(10):
    simple_list.append(i ** 2)

# Display the list
print("simple_list: ", simple_list)

# We can also filter the list in a similar way
# Let's make a new list of just the even numbers
simple_even_list = []

for number in simple_list:
    if number % 2 == 0:
        simple_even_list.append(number)

# Display the even list
print("Evens of simple_list: ", simple_even_list)

# Both of these operations (creation and filtering) can be done in a
# single line!
# For example, let's create the same list
list_comp = [i ** 2 for i in range(10)]

# Display our new list list
print("list_comp: ", list_comp)

# Do the filtering in a similar fashion
list_comp_even = [i for i in list_comp if i % 2 == 0]

# Display our new list of even numbers
print("evens of list_comp: ", list_comp_even)

# We can even have nested loops in our list comprehension
nested_loop = [x + y for x in [10, 20, 30] for y in [20, 40, 60]]

# Display our nested loop list
print("nested_loop example: ", nested_loop)

