import random

#Creates a Agent class for different methods    
class Agent:
    def __init__(self, i):
        """
       Initialize a new class instance with  unique id and random x and y-coordunates.

       Args:
           i (int): A unique id

       Attributes:
           i (int): Unique id assigned to the instance.
           x (int): A random x coordinate of the instance (integer between 0 and 99)
           y (int): A random  y coordinate of the instance (integer between 0 and 99)

       This constructor method initializes a new instance
       of the class with a unique identifier `i` and random `x` and `y` coordinates.
       The `i` attribute can be used to identify the instance, while the `x` and `y`
       attributes represent its location. The `random.randint()` function from the
       Python standard library is used to generate the random coordinates.
       """
        self.i = i
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        pass

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
            A string as 'Class(x=value, y=value, i=value)' 
            
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

   The method randomly creates a new location for the instance by adding or deducting 1 from its current x and y coordinates while making sure the new locations fall within the set boundary.

   """
        rn =random.random()
        if rn < 0.5:
            self.x = self.x + 1
        else:
            self.x = self.x - 0
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

