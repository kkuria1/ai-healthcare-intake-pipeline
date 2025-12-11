import sqlite3
import pandas as pd

# Connect to the SQLite database
connection = sqlite3.connect("../healthcare_ops.db")

# Simple query to test the connection
df = pd.read_sql_query("SELECT * FROM patients LIMIT 5;", connection)

print("Connection successful. Sample data:")
print(df)

connection.close()
