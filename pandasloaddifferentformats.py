//pandas load csv files and save in parquet.
//pandas load txt files and save in orc format. 
//orc vs parquet
//pandas use joins of 2 dataframes, map employee and department tables
import csv

filename = "data.csv"  # Replace with the path to your CSV file

with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

import pandas as pd

filename = "data.csv"  # Replace with the path to your CSV file
//Read the csv file to a dataframe.
data = pd.read_csv(filename)
print(data)
