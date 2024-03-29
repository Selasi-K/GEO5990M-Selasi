#abm3 practical session
#Importing packages
import random
import math
from matplotlib import pyplot as plt
import operator


# Set the pseudo-random seed for reproducibility
random.seed(0)

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99


#Create a list to store agents
agents = []

# Initialise agents
n_agents = 10
for i in range(n_agents):
    x0 = random.randint(0,99)
    #print("x0", x0)
    y0 = random.randint(0,99)
    #print("y0", y0)
    agents.append([x0,y0])

print(agents)


# Move agents
n_iterations = 1000
#Loop to move agents by number of iterations set#
for n_iterations in range(n_iterations):
    for i in range(n_agents):
        #Change agents(i) coordinates randomly
        #x-coordinate
        rn =random.random()
        #print("rn", rn)
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
        # print("agents[i][0]", agents[i][0])
        # print("agents[i][1]", agents[i][1])
        # Apply movement constraints.
        if agents[i][0] < x_min:
            agents[i][0] = x_min
        if agents[i][1] < y_min:
            agents[i][1] = y_min
        if agents[i][0] > x_max:
            agents[i][0] = x_max
        if agents[i][1] > y_max:
            agents[i][1] = y_max
        # print("agents[i][0]", agents[i][0])
        # print("agents[i][1]", agents[i][1])
    
# Calculate the Euclidean distance between (x0, y0) and (x1, y1) using functions
#Setting variables of coordinates
x0 = 0
y0 = 0
x1 = 3
y1 = 4

def get_distance(x0, y0, x1, y1):
    """
    Calculate the Euclidean distance between (x0, y0) and (x1, y1).

    Parameters
    ----------
    x0 : Number
        The x-coordinate of the first coordinate pair.
    y0 : Number
        The y-coordinate of the first coordinate pair.
    x1 : Number
        The x-coordinate of the second coordinate pair.
    y1 : Number
        The y-coordinate of the second coordinate pair.

    Returns
    -------
    distance : Number
        The Euclidean distance between (x0, y0) and (x1, y1).
    """
    # Calculate the difference in the x coordinates.
    diff_x = x0 - x1
    # Calculate the difference in the y coordinates.
    diff_y = y0 - y1
    # Square the differences and add the squares
    add_squaresxy = (diff_x * diff_x) + (diff_y * diff_y)
    # Calculate the square root
    distance = math.sqrt(add_squaresxy)
    return distance
print(get_distance(x0, y0, x1, y1))



def get_min_and_max_distance():
    """
    Calculate and return the maximum and minimum distance between all the agents
    Also calculates the average of these distances

    Returns
    -------
    max_distance : Number
        The maximum distance between all the agents.
        
    min_distance : Number
        The minimum distance between all the agents.
    
    average distance: float
        The averahe distance between all the agents
    
    
       """
    max_distance = 0 #Initialize max distance
    min_distance = math.inf #Initialize min distance
    total_distances = 0 #Initialize total distance
    n = 0
    print("len(agents)", len(agents))
    for i in range(len(agents)):
        a = agents[i]      
        for j in range(i+1, len(agents), 1):
                #print(i, j) 
                b = agents[j]
                distance = get_distance(a[0], a[1], b[0], b[1])
                #print("distance between", a, b, distance)
                min_distance = min(min_distance, distance)
                max_distance = max(max_distance, distance)
                total_distances = total_distances + distance
                n = n + 1
                #print("min_distance", min_distance)
                #print("i", i, "j", j)
    return min_distance, max_distance, total_distances / n

min_distance, max_distance, average = get_min_and_max_distance()
print("Maximum distance between all the agents", max_distance)
print("Minimum distance between all the agents", min_distance)
print("Average distance between all the agents", average)

print(agents)
# Plot the agents
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
    # Get the coordinates with the largest x-coordinate
    maxx = (max(agents, key=operator.itemgetter(0)))
    plt.scatter(maxx[0], maxx[1], color='red')
    # Get the coordinates with the smallest x-coordinate
    minx = (min(agents, key=operator.itemgetter(0)))
    plt.scatter(minx[0], minx[1], color='blue')
    #Get coordinate with the largest y-coordinate#
    maxy = (max(agents, key=operator.itemgetter(1)))
    #Plot coordinate with largest y-coordinate yellow#
    plt.scatter(maxy[0], maxy[1], color='yellow')
    #Get coordinates with smallest y-coordinate
    miny = (min(agents, key=operator.itemgetter(1)))
    #Plot coordinates with smallest y green#
    plt.scatter(miny[0], miny[1], color='green')
plt.show()
    



 