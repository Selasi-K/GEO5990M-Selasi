#Importing packages
import random
import math
import matplotlib
from matplotlib import pyplot as plt
import operator
import time
import agentframework as af

# Set the pseudo-random seed for reproducibility
random.seed(0)

#Initialize parameters
n_agents = 10

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99

#Create and append agents
agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent(i))
    print(agents[i])
print(agents)


# Calculate the Euclidean distance between (x0, y0) and (x1, y1) using functions
#Setting variables of coordinates
x0 = 0
y0 = 0
x1 = 3
y1 = 4
def get_distance(x0, y0, x1, y1):
    # Calculate the difference in the x coordinates.
    diff_x = x0 - x1
    # Calculate the difference in the y coordinates.
    diff_y = y0 - y1
    # Square the differences and add the squares
    add_squaresxy = (diff_x * diff_x) + (diff_y * diff_y)
    # Calculate the square root
    distance = math.sqrt(add_squaresxy)
    return distance
#print(get_distance(x0, y0, x1, y1))

#Calculating the maximum distance using defined functions
max_distance = 0 # Initialise max_distance
for a in agents:
    for b in agents:
            #distance = get_distance(a[0], a[1], b[0], b[1])
            distance = get_distance(a.x, a.y, b.x, b.y)
            #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
            #print("max_distance", max_distance)


def get_max_distance():
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        #for j in range(len(agents)):
        for j in range(i+1, len(agents), 1):
                #if i != j:
                #if i < j:
                #print(i, j) 
                b = agents[j]
                distance = get_distance(a.x, a.y, b.x, b.y)
                #print("distance between", a, b, distance)
                max_distance = max(max_distance, distance)
                #print("max_distance", max_distance)
                #print("i", i, "j", j)
    return max_distance

def get_min_distance():
    min_distance = math.inf
    for i in range(len(agents)):
        a = agents[i]
        #for j in range(len(agents)):
        for j in range(i+1, len(agents), 1):
                #if i != j:
                #if i < j:
                #print(i, j) 
                b = agents[j]
                distance = get_distance(a.x, a.y, b.x, b.y)
                #print("distance between", a, b, distance)
                min_distance = min(min_distance, distance)
                #print("min_distance", min_distance)
                #print("i", i, "j", j)
    return min_distance

def get_min_and_max_distance():
    max_distance = 0
    min_distance = math.inf
    total_distances = 0
    n = 0
    for i in range(len(agents)):
        a = agents[i]
        #for j in range(len(agents)):
        for j in range(i+1, len(agents), 1):
                #if i != j:
                #if i < j:
                #print(i, j) 
                b = agents[j]
                distance = get_distance(a.x, a.y, b.x, b.y)
                #print("distance between", a, b, distance)
                min_distance = min(min_distance, distance)
                max_distance = max(max_distance, distance)
                total_distances = total_distances + distance
                n = n + 1
                #print("min_distance", min_distance)
                #print("i", i, "j", j)
    return min_distance, max_distance, total_distances / n


# Move agents
n_iterations = 10
for n_iterations in range(n_iterations):
    for i in range(n_agents):
        #Change agents(i) coordinates randomly
        agents[i].move(x_min, y_min, x_max, y_max)
# Plot
for i in range(n_agents):
    plt.scatter(agents[i].x, agents[i].y, color='black')
# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')
       
plt.show()

