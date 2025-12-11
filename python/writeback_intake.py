import sqlite3
import os
from router import route_intake

DB_PATH = "../healthcare_ops.db"
CSV_OUTPUT_PATH = "../data/intake_routed.csv"

def write_routed_intake_to_db():
    """
    Run the routing pipeline and write the result to a new SQLite table: intake_routed.
    Also exports the result to a CSV file in the data/ folder.
    """
    # 1) Run the routing pipeline to get the final DataFrame
    routed_df = route_intake()

    # 2) Write to SQLite as a new table
    connection = sqlite3.connect(DB_PATH)
    routed_df.to_sql("intake_routed", connection, if_exists="replace", index=False)
    connection.close()

    print(f"✅ Wrote {len(routed_df)} rows to the 'intake_routed' table in {DB_PATH}")

    # 3) Ensure data folder exists
    os.makedirs(os.path.dirname(CSV_OUTPUT_PATH), exist_ok=True)

    # 4) Export to CSV
    routed_df.to_csv(CSV_OUTPUT_PATH, index=False)
    print(f"✅ Exported routed intake data to CSV at: {CSV_OUTPUT_PATH}")


if __name__ == "__main__":
    write_routed_intake_to_db()

