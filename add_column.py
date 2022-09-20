# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

""" 
The code is loading .csv file and adding an extra column.
Column contains the length of the segment.
"""

#Import the csv file, read it in, and allow for editing
import csv 
with open('brca_cnvs_tcga-1.csv', 'r') as csvinput :
    with open('new.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput)
       
#Recognize that first row contains categories and append a new one to it
#Define length as subtracted value of the segment start from the segment end
#Append the length as the new item in the row
#This is done for every row in the input file
    
        for row in csv.reader(csvinput):
            if row[0] == "ID":
                writer.writerow(row+["Length"])
            else:
                length = int(row[3]) - int(row[2])
                writer.writerow(row+[length])
                
            
            
    
            
    
            
        
    
