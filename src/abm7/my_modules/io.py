import csv

# Read input data
def read_data():
    """
    Read a CSV file  and presents it as a list of list
    
    The fumction opens the text file from '../../data/input/in.txt' directory
    and reads it in using the csv module. Each row is collected as list of lists

   Returns:
       List: A list of lists with data read from the input file.
   """
    f = open('../../data/input/in.txt', newline='')
    data = []
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
            #print(value)
        data.append(row)
    f.close()
    print(data)
    
  

#Checking that each row of data contains the same number of values, and returning the num of rows and columns
  #Checking number of rows and columns
    n_rows = len(data)
    #print('n_rows',n_rows)
    n_cols0 = len(data[0])
   # print('n_cols',n_cols0)
   #Checking if there equal number of rows and columns and printing the num 
    for row in range(1,n_rows):
        n_cols = len(data[row])
        if n_cols != n_cols0:
            print("Warning")
        #print data
        return data, n_rows, n_cols
        f.close()
        print(data)

def write_data(filename,environment):
    """
    Write a list of lists with data produced to a CSV file.

    This function takes the list of lists produced, opens 
    '../../data/output/out.txt' directory and writes the environment contents
    to it using the csv module. Lists within
    lists are treated as rows written as comma-separated values.
    
    Args:
        environment: A list of lists containing numeric 
        data to be written to the output file.

    Returns:
        None
    """
    with open('../../data/output/out.txt','w', newline='') as f:
        writer=csv.writer(f, delimiter=',')
        for row in environment:
            writer.writerow(row)
    f.close()
        
