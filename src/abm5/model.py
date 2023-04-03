#Importing packages
import random
import math
from matplotlib import pyplot as plt
import operator
import my_modules.agentframework as af
import my_modules.io as io

#Calling the io
environment, n_rows, n_cols = io.read_data()

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
x_max = n_cols - 1
# The maximum y coordinate.
y_max = n_rows - 1

#Create and append agents
agents = []
for i in range(n_agents):
# Create an agent
    agents.append(af.Agent(i,environment,n_rows,n_cols))
    print(agents[i])
print(agents)


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
#print(get_distance(x0, y0, x1, y1))

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


def sumEnv():
    """
    Calculate the sum of all values in the list of lists.
    
    In an iterative way the function takes values in the environment and adds
    them together till it obtains the sum of the values.

    Args:
        environment : A list of lists with numeric values.

    Returns:
        The sum of all numeric values in `environment`.
    """
    sumEnv=0
    for row in environment:
        for v in row:
            sumEnv += v
        #sumEnv += sum(row)
    return sumEnv
    
print('Sum of values in environment', sumEnv())

#Create a function to find the sum of store values
def sumAS():
    """
    Calculate the total amount of units stored.
    
    The function in an iterative way goes through the agents and adds up the stores 
    till it obtains the total number of units stored across all agents.

   Args:
      agents : A list of agent objects.

  Returns:
       The total stored across all agents.
  """
    Sumstore=0
    for agent in agents:
        Sumstore += agent.store
    return  Sumstore

print('Sum of stores', sumAS())

#define a funtion to write environment 

        

# Move agents
n_iterations = 100
for n_iterations in range(n_iterations):
    for i in range(n_agents):
        #Change agents(i) coordinates randomly
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
        
#Calling write_data function
n_cols = io.write_data(environment)
    

#Printing out results after moves
print('Sum of values in environment', sumEnv())
print('Sum of stores', sumAS())
    
# Plot
plt.imshow(environment)

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
 #Limiting the plot axis
plt.ylim(y_max / 3, y_max * 2 / 3)
plt.xlim(x_max / 3, x_max * 2 / 3)      
plt.show()

