# This program shows off conditionals and while-loops in Python3
# By: Nick from CoffeeBeforeArch

# How do we alter control flow (what our program does)
a = 5
b = 3

# Only 1 conditional in a chain will be evaluated
# It will always be the first one that is true, in-order
# else blocks don't require a condition, they cove all other cases
if(a == 3):
    print("a == 3")
elif(b == 5):
    print("b == 5")
else:
    print("All other cases!")

# While loops check if a condition is true each iteration
# Must be careful to not make this infinite! (Unless we want that)
i = 0
while(i != 10):
    # Increment every ieration
    i += 1

    # Print something special on the third iteration
    if i == 3:
        print(f"Only prints on third iteration ({i})")
        # Continue immediately starts the next iterations
        continue
    # Print something every other iteration
    print(f"Prints on every other iteration ({i})")

    # Exit the loop early on the seventh iteration   
    if i == 7:
        # Immediately leave the loop
        break

print(f"Exited the loop when i == {i}")
