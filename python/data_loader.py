import sqlite3
import pandas as pd

DB_PATH = "../healthcare_ops.db"

def load_table(table_name):
    """Load any table from the SQLite database into a pandas DataFrame."""
    connection = sqlite3.connect(DB_PATH)
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df

if __name__ == "__main__":
    # Test: Load the patients table
    patients_df = load_table("patients")
    print(patients_df.head())

