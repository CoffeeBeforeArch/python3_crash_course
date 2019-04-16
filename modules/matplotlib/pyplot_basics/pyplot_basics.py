# This program shows off how to create basic plots using matplotlib
# By: Nick from CoffeeBeforeArch

# Import numpy for some convenience
import numpy as np

# Import pyplot from matplotlib (this is where the plotting stuff is)
import matplotlib.pyplot as plt

# Create some data
# This just gives us a numpy array of points between 0 and 2
x = np.linspace(0, 2, 100)
print(x)

# Create a figure
# Is blank until we add to it
fig = plt.figure()

# Plot a linear, quadratic, and cubic function
plt.plot(x, x, label="Linear")
plt.plot(x, x**2, label="Quadratic")
plt.plot(x, x**3, label="Cubic")

# Add a title to the plot
plt.title("Simple Plot")

# Show the legend of the plot
plt.legend()

# Print out the final plot
plt.show()

