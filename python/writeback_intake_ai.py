import sqlite3
import os

from ai_summarizer import generate_llm_summaries

DB_PATH = "../healthcare_ops.db"
CSV_OUTPUT_PATH = "../data/intake_routed_ai.csv"


def write_intake_routed_ai():
    """
    Run the LLM summarization over intake_routed and
    write the result to a new SQLite table: intake_routed_ai.
    Also exports the result to a CSV file in the data/ folder.
    """
    # 1) Get the AI-enriched DataFrame
    enriched_df = generate_llm_summaries()

    # 2) Write to SQLite as a new table
    connection = sqlite3.connect(DB_PATH)
    enriched_df.to_sql("intake_routed_ai", connection, if_exists="replace", index=False)
    connection.close()

    print(f"✅ Wrote {len(enriched_df)} rows to the 'intake_routed_ai' table in {DB_PATH}")

    # 3) Ensure data folder exists
    os.makedirs(os.path.dirname(CSV_OUTPUT_PATH), exist_ok=True)

    # 4) Export to CSV
    enriched_df.to_csv(CSV_OUTPUT_PATH, index=False)
    print(f"✅ Exported AI-enriched intake data to CSV at: {CSV_OUTPUT_PATH}")


if __name__ == "__main__":
    print("Running AI write-back for intake_routed_ai...\n")
    write_intake_routed_ai()

