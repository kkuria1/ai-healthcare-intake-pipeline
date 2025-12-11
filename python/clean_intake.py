import pandas as pd
from data_loader import load_table

def clean_intake_data():
    """Load and clean the intake table."""
    df = load_table("intake")

    # Standardize text columns
    df["insurance_provider"] = df["insurance_provider"].str.strip().str.title()
    df["policy_number"] = df["policy_number"].str.strip() if df["policy_number"].notnull().any() else df["policy_number"]

    # Identify missing insurance info
    df["missing_insurance"] = df["insurance_provider"].isnull() | df["policy_number"].isnull()

    return df

if __name__ == "__main__":
    cleaned_df = clean_intake_data()
    print(cleaned_df.head())

    