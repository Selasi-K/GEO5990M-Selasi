#PROJECT TITLE

AGENT BASED MODEL

##DESCRIPTION 

The Agent Based Model is a simulation software which is usually used to study behaviour in complex systems.
In this model, agents are created and taken through some steps in an iterative manner which in the long
run alters their characteristics and environment. Some of these steps include randomly moving, eating, sharing resources, and measuring
distances between agents.
Output of the model will be saved in a set file directory while final output will be presented as a GUI.


##GETTING STARTED

License - Apache 2.0. Read the licence file for more information. Additional, you can visit this link for more details: https://www.apache.org/licenses/LICENSE-2.0

##FILE DIRECTORY

data - input - contains in.txt file which contains coordinates data read by the program

	 - output - contains out.gif,out.txt,out7.gif,out7.txt and Images folder. (All are outputs of the program)

src- abm1 - model.py

	 abm2 - model.py

	 abm3 - model.py
			timing.py

	 abm4 -	agentframework.py
			model.py
	
	 abm5 -	my_modules - agentframework.py
						 io.py
		  -	model.py	  
	 
	 abm6 - my_modules - agentframework.py
						 geometry.py
						 io.py			 
		  -	model.py
		  
	 abm7 -  my_modules - agentframework.py
						 geometry.py
						 io.py				 
		  -	model.py
		  
	 abm8 -  my_modules - agentframework.py
						 geometry.py
						 io.py			 
		  -	model.py
		  
	 abm9 - my_modules - agentframework.py
						 geometry.py
						 io.py			 
		  -	model.py

licence

README.md
		  
##PREREQUISITES

This program runs preferably best on the Scientific Python Development Environment (Spyder) IDE,one of the programs in the Anaconda package on a computer.
However it will also work on any python compatible software. Spyder is a free open source 
Python system which has a good interface and tools helpful in visualing outputs, debugging, and
interactivity. To download and install python click this link and follow the instructions:
https://www.spyder-ide.org/
Additionally, watch the video on getting started to learn about the basics of the program.

##USAGE

Once the Spyder program is installed succefully,launch the program.
You should see three windows, The Editor where most of the coding will be done on the left, Help viewer
on top right where tools like variable explorer, help and plots can be be accessed, and ipython console where some outputs 
are printed and additionally coding can be done (Watch video in the above link for more details). Also see figure 1 in the word document.

#RUNNING THE PROGRAM

From the tool bar at the top of your screen, click open file or hit Ctrl + O on your keyboard.
Navigate to where you have saved the files and select your desired file. For instance, select Abm9 to see final simulation output.
Note: All files in your prefered Abm folder should be opened for optimum run of the program.

After selecting and opening the files, by hovering on each option in the tool bar find 'run file'. Ensure 'model.py'
tab is active and click run. (See figure 1 in word document for help)

Once run is clicked, a series of steps are followed to produce the final simulation:
- txt. data is read in using the csv module (read function) or from the web if running abm9.
- This data is collected and represented as a list of lists in the program (string,repair function).
-This coordinates are plotted to visualize them.
- The coordinates are moved randomly from one point to another within the defined boundaries (move function).
- Resources are taken and stored or released to the environment based on the parameters set.
- A neigbourhood radius is created using the distance from each agent to assess neighbours resources will be shared with and shares them(share function).
- This processes alter the position of the agents and changes the environment iteratively.
-The process goes on till the set stopping condition is reached.
-At this point the final output is written to a txt file (write function)
-It can additionally be displayed on a canvas as a GUI.
-The GUI model can be run by clicking 'model' and then 'run' from the drop down menu (See figures 2,3 and 4 in attached word document).

#Brief about ABM files

ABM1 - Basic steps in initializing random variables and calculating Euclidean distance between them.
ABM2 - Creating lists to store agents using loops and plotting these agents to visualize them.
ABM3 - Creating functions to calculate maximum, minimum and average distances between coordinates 
		and adding a timing code to assess time taken to execute command. Movement constraints are also introduced.
ABM4 - Introducing classes and how to use them to hold different methods.
ABM5 - Reading  in and writing data using the csv module and introducing interactions between the agents and the environment.
ABM6 - Assessing neigbourhood of neighbours and adding conditions for sharing resources. The if __name__ == '__main__': is 
introduced to better organize the code. Outputs are produced as gif files.
ABM7- Introducing exceptions and more on displaying outputs as animations
ABM8- Introducing GUI
ABM9 -Reading in data from web sources.


Note: In case of any errors, use the debugging tool to detect the problem. ipython console is also 
particularly helpful in doing this.

Also, tests showed that errors can be caused when file path in the python manager(see figure 5 in document) does not match files opened.
To fix, this add appropriate file path and try running code again.

