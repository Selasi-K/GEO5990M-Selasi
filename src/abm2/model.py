#abm2
#Importing packages
import random
import math
import matplotlib
from matplotlib import pyplot as plt
import operator

# Set the pseudo-random seed for reproducibility
random.seed(0)

#Create an empty list to store agents
agents = []

# Initialise agents
n_agents = 10
#for loop to generate random agents
for i in range(n_agents):
    x0 = random.randint(0,99)
    #print("x0", x0)
    y0 = random.randint(0,99)
    #print("y0", y0)
    agents.append([x0,y0])
    #agents.append([random.randint(0,99), random.randint(0, 99)]) #A different way to do the loop

print(agents)


# Move agents
for i in range(n_agents):
    #Change agents(i) coordinates randomly
    #x-coordinate
    rn = random.random()
    #print("rn", rn)
    #If rn is less than 0.5 1 is added to agent coordinate, else 1 is subtracted
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    #y-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
    
        
# Plot the agents
for i in range(n_agents):
    #Plot coordinates black#
    plt.scatter(agents[i][0], agents[i][1], color='black')
    # Get the coordinates with the largest x-coordinate
    maxx = (max(agents, key=operator.itemgetter(0)))
    #Plot the coordinate with the largest x red#
    plt.scatter(maxx[0], maxx[1], color='red')
    # Get the coordinates with the smallest x-coordinate
    minx = (min(agents, key=operator.itemgetter(0)))
    #Plot the coordinate with the smallest  x blue#
    plt.scatter(minx[0], minx[1], color='blue')
    #Plot the coordinate with the largest y yellow#
    maxy = (max(agents, key=operator.itemgetter(1)))
    plt.scatter(maxy[0], maxy[1], color='yellow')
    #Plot the coordinate with the smallest  y green#
    miny = (min(agents, key=operator.itemgetter(1)))
    plt.scatter(miny[0], miny[1], color='green')
plt.show()



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





 