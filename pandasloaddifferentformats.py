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

#create a dataframe from excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

print(df)

#create a dataframe from database
import pandas as pd
import sqlite3

conn = sqlite3.connect('database.db')

query = 'SELECT * FROM people'
df = pd.read_sql(query, conn)

conn.close()

print(df)

