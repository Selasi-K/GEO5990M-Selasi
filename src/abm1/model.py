#abm1 practical session
#Importing random package
import random
import math

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Initialise variable x0
x0 = 0
print("x0", x0)

# Initialise variable y0
y0 = 0
print("y0", y0)

# Change x0 and y0 randomly
rn = random.random()
print(rn)
#adding the conditional if statement
#Simplifying the code
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)

#Duplicating the code to change value of y
if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print("y0", y0)

#Initialise variable x1 to randomly change values
x1 = random.randint(0, 99)
print("x1", x1)

#Initialise variable y1 to randomly change values
y1 = random.randint(0, 99)
print("y1", y1)

# Change x1 and y1 randomly
rn = random.random()
print(rn)
if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print("x1", x1)

if rn < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print("y1", y1)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
#Setting variables of coordinates
x0 = 0
y0 = 0
x1 = 3
y1 = 4
# Calculate the difference in the x coordinates.
diff_x = x0 - x1
print("diff_x", diff_x)
# Calculate the difference in the y coordinates.
diff_y = y0 - y1
print("diff_y", diff_y)
# Square the differences and add the squares
add_squaresxy = (diff_x * diff_x) + (diff_y * diff_y)
print("add_squarexy", add_squaresxy)
# Calculate the square root
distance = math.sqrt(add_squaresxy)
print("distance", distance)





 