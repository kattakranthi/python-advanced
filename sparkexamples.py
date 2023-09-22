//spark load csv files and save in parquet.
//spark load txt files and save in orc format. 
//orc vs parquet
//spark use joins of 2 dataframes, map employee and department tables
//aggregrate functions 
//Add total - of department salary, show the data by department salary, show the employee count by Organization.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder.appName("Employee CSV to Parquet").getOrCreate()

# Load the CSV file into a DataFrame
csv_file_path = "employees.csv"
df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

# Add one more column to the DataFrame
df_with_salary_multiplier = df.withColumn("SalaryMultiplier", col("Salary") * 2)  # You can adjust the multiplier as needed

# Save the DataFrame as a Parquet file
parquet_file_path = "output/"
df_with_salary_multiplier.write.parquet(parquet_file_path)

#save the dataframe as a orc format
df_with_salary_multiplier.write.orc(output_path)

# Stop the SparkSession
spark.stop()

