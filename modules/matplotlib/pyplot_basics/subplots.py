# This program shows of sub-plots in Python3 using matplotlib
# By: Nick from CoffeeBeforeArch

import matplotlib.pyplot as plt

# Create a new figure
# Reference it using "1"
# 3 inches tall, by 9 inches wide
plt.figure(1, figsize=(9,3))

# Make some fake data
values = [1, 10, 100]

# Make some fake labels
labels = ["A", "B", "C"]

# Make a bar graph
plt.subplot(131)
plt.bar(labels, values)

# Make a scatter plot
plt.subplot(132)
plt.scatter(labels, values)

# Make a line plot like we've seen before
plt.subplot(133)
plt.plot(labels, values)

# Add a title to the figure
plt.suptitle("Three different plots on the same figure")

# Show the figure
plt.show()

