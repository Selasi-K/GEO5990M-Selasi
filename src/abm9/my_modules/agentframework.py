#import packages
import random
import my_modules.geometry as geometry
    
class Agent:
    def __init__(self, agents, i, environment, n_rows, n_cols, x = None, y = None):
        """
        The constructor method.
        
        Parameters
        ----------
        i : Integer
            To be unique to each instance.
        environment : List
            A reference to a shared environment
        n_rows : Integer
            The number of rows in environment.
        n_cols : Integer
            The number of columns in environment.
        x : Integer
            For initialising the x coordinate of the agent.
        y : Integer
            For initialising the y coordinate of the agent.
        
        Returns
        -------
        None.
        
        """
        self.agents = agents
        self.i = i
        self.environment = environment
        if x == None:
            tnc = int(n_cols / 3)
            self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        else:
            self.x = x
        if y == None:
            tnr = int(n_rows / 3)
            self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        else:
            self.y = y
        self.store = random.randint(0, 99)
        self.store_shares = 0
    
    def __str__(self):
        """
        Return the instance in a string format.
    
        Returns:
            A string as 'Class(x=value, y=value, i=value)' where:
            - 'Class' is the class name.
            - 'x', 'y', and 'i' are attributes of the instance.
            - 'value' is the string format of the atrribute.
            """
        return self.__class__.__name__ + "(x=" + str(self.x) \
        + ", y=" + str(self.y) + ", i=" + str(self.i) + ")"
        
    def __repr__(self):
        """
        Return the instance in a string format and enhances printing results.
    
        Returns:
            A string as 'Class(x=value, y=value, i=value)' where:
         
            """
        return str(self)
    
    def move(self, x_min, y_min, x_max, y_max):
        """
   Move the agents to a new location but ensures they are within set bounds.

   Args:
       x_min (int): The minimum x coordinate within the set boundary.
       y_min (int): The minimum y coordinate within the set boundary.
       x_max (int): The maximum x coordinate within the set boundary.
       y_max (int): The maximum y coordinate within the set boundary.

   The method randomly creates a new location for the instance by adding or
   deducting 1 from its current x and y coordinates dependent on value of rn while ensuring
   locations fall within the set boundary

   """
        rn =random.random()
        if rn < 0.5:
            self.x = self.x + 1
        else:
            self.x = self.x - 1
        #y-coordinate
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            self.y = self.y  + 1
        else:
            self.y  = self.y  - 1
            
         # Apply movement constraints.
        if self.x < x_min:
         self.x = x_min
        if self.y  < y_min:
         self.y  = y_min
        if self.x > x_max:
         self.x = x_max
        if self.y  > y_max:
         self.y  = y_max
         
    def eat(self):
        """
      This method takes units from the environment of an agent and stores them.
      
      If the environment has 10 or more units, 10 is taken and added to the store, 
      else everything is added to the store and environment is reset to 0
      
      Adds an extra condition stating that if store value is greater than 99, 
      half of the value is taken and added to the environment

  Args:
      self (object): An instance of the agent class.

  Returns:
      None
   
    """ 
       
        if self.environment[self.y][self.x] >= 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        
    #if store is greater than 99
        if self.store > 99:
           self.store = self.store/2 
           self.environment[self.y][self.x] += self.store
         
       
          
       
    def share(self, neighbourhood):
        """
  Shares a portion of one agent's resources with its neighbors within a given radius.
  The amount of resources to be shared is divided by the number of neighbouring agents 
  `geometry.get_distance` is used to calculate the distance between agents.

  Parameters
  ----------
  neighbourhood :
      The radius of the circular neighborhood around the agent measured as distance.

  Returns
  -------
  None

   """
    # Create a list of agents in neighbourhood
        neighbours = []
        #print(self.agents[self.i])
        for a in self.agents:
            distance = geometry.get_distance(a.x, a.y, self.x, self.y)
            if distance < neighbourhood:
                neighbours.append(a.i)
        # Calculate amount to share
        n_neighbours = len(neighbours)
        #print("n_neighbours", n_neighbours)
        shares = self.store / n_neighbours
        #print("shares", shares)
        # Add shares to store_shares
        for i in neighbours:
            self.agents[i].store_shares += shares
            
            
    
            