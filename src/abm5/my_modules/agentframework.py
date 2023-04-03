#Import package
import random
    
class Agent:
    def __init__(self, i, environment, n_rows, n_cols):
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
        
        Returns
        -------
        None.
        
        """
        self.i = i
        self.environment = environment
        tnc = int(n_cols / 3)
        self.x = random.randint(tnc - 1, (2 * tnc) - 1)
        tnr = int(n_rows / 3)
        self.y = random.randint(tnr - 1, (2 * tnr) - 1)
        self.store = 0
        
    #string method    
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
        
        
    #repair method
    def __repr__(self):
        """
        Return the instance in a string format and enhances printing results.
    
        Returns:
            A string as 'Class(x=value, y=value, i=value)' where:
            
            """
        return str(self)
    
    
    
    
    #move method
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
   locations fall within the set boundary.

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
         
         
         
         
    #defining eat method to gather 
    def eat(self):
        """
        This method takes units from the environment and stores them.
        
        If the location contains 10 or more, 10 units are taken and stored, 
        otherwise everything is deposited in the store.

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
            self.environment[self.y][self.x]= 0

