import pandas as pd 
//Program to check for different Conversions. All the Utility Functions to use in the whole project.

# Sample DataFrame with different date format
data = {'date_string': ['21-09-2023', '22-09-2023', '23-09-2023']}
df = pd.DataFrame(data)

# Convert the 'date_string' column with a specified format
df['date'] = pd.to_datetime(df['date_string'], format='%d-%m-%Y')

# Print the DataFrame to see the result
print(df)

'''
date_string       date
0  21-09-2023 2023-09-21
1  22-09-2023 2023-09-22
2  23-09-2023 2023-09-23
> 
'''
