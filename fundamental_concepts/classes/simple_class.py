# This program shows off the basics of classes in Python3
# By: Nick from CoffeeBeforeArch

# Encapsulate the coordinates of a point in a single class
class Coordinate():
    # An __init__ method is called to create an instance
    # of this class
    # 'self' points to this particular instance
    def __init__(self, x, y):
        # 'x' and 'y' are are data attributed
        # Data attributes of an instance are also called instance
        # variables
        self.x = x
        self.y = y
    
    # We can also define our own methods
    # We'll use 'self' to refer to this instance, and 'other', another
    def distance(self, other):
        # Simple Pythag. Thm.
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5
    
    # __str__(self) is used when we try and print an object
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    # Other things we can override
    # __add__, __sub__, __eq__, __lt__, __len__, ...

# Create two instances of coordinates
c1 = Coordinate(3, 4)
origin = Coordinate(0, 0)

# Print out coordinates
print(f"Coordinate c1: x={c1.x}, y={c1.y}")
print(f"Coordinate origin: x={origin.x}, y={origin.y}")

# Print out the distance using explicit and implicit parameters
print(f"Distance with explicit parameters {Coordinate.distance(c1, origin)}")
print(f"Distance with implicit parameters {c1.distance(origin)}")

# Use out custom string when print is called
print(c1)
