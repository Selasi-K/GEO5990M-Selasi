# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:48:42 2023

@author: Selasi
"""

import csv

# Read input data
def read_data():
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
        