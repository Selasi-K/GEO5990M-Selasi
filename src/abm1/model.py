#abm1 
#Importing random package
import random
import math #Importing math pazckage

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Initialise variable x0
x0 = 0
print("x0", x0) #prints out results

# Initialise variable y0
y0 = 0
print("y0", y0)

# Change x0 and y0 randomly
rn = random.random()
print(rn)

#adding the conditional if statement
#If random value is less than 0.5, 1 is added else 1 is subtracted
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

# Calculating the Euclidean distance between (x0, y0) and (x1, y1)
#Setting variables of coordinates
x0 = 0
y0 = 0
x1 = 3
y1 = 4

# Calculating the difference in the x coordinates.
diff_x = x0 - x1
print("difference in x", diff_x)

# Calculating the difference in the y coordinates.
diff_y = y0 - y1
print("difference in y", diff_y)

# Squaring the differences and add the squares
add_squaresxy = (diff_x * diff_x) + (diff_y * diff_y)
print("add_squarexy", add_squaresxy)

# Calculating the square root to find final result
distance = math.sqrt(add_squaresxy)
print("distance", distance)





 