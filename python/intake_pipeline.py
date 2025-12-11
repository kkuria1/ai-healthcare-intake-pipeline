import pandas as pd
from data_loader import load_table
from clean_intake import clean_intake_data
from validate_intake import validate_intake_data

def intake_pipeline():
    """Run the full intake pipeline: clean + validate."""

    # Step 1: Load raw data
    raw_df = load_table("intake")

    # Step 2: Clean data
    cleaned_df = clean_intake_data()

    # Step 3: Validate data
    validated_df = validate_intake_data()

    # Step 4: Merge cleaning + validation outputs
    # (Left join on intake_id ensures we keep all rows)
    final_df = cleaned_df.merge(
        validated_df,
        on="intake_id",
        suffixes=("_clean", "_validated")
    )

    return final_df


if __name__ == "__main__":
    output = intake_pipeline()
    print("Pipeline output sample:")
    print(output.head())

