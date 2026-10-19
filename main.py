
import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("FirstSparkApp") \
    .master("local[*]") \
    .getOrCreate()

# Reduce the log noise
spark.sparkContext.setLogLevel("ERROR")

# Create some sample data
data = [
    ("Amit", 25, "Kanpur"),
    ("Priya", 30, "Delhi"),
    ("Rahul", 22, "Lucknow"),
    ("Sneha", 28, "Delhi"),
]
columns = ["name", "age", "city"]

df = spark.createDataFrame(data, columns)

# Show the whole table
df.show()

# Show the structure (column names and types)
df.printSchema()


# 1. Select specific columns
print("Names and cities:")
df.select("name", "city").show()

# 2. Filter rows (people older than 24)
print("Age greater than 24:")
df.filter(df.age > 24).show()

# 3. Filter on text (people in Delhi)
print("People in Delhi:")
df.filter(df.city == "Delhi").show()

spark.stop()