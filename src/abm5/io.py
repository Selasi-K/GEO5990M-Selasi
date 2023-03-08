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