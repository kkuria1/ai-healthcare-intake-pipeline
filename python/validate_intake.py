import pandas as pd
from data_loader import load_table

def validate_intake_data():
    """Validate insurance and policy fields in the intake table."""
    df = load_table("intake")

    # Rule 1: Missing insurance provider or policy number
    df["missing_insurance_provider"] = df["insurance_provider"].isnull()
    df["missing_policy_number"] = df["policy_number"].isnull()

    # Rule 2: Policy number should be at least 5 characters if not null
    df["invalid_policy_length"] = df["policy_number"].apply(
        lambda x: True if pd.notnull(x) and len(str(x)) < 5 else False
    )

    # Rule 3: Detect suspicious characters in policy numbers
    df["suspicious_policy_chars"] = df["policy_number"].astype(str).str.contains(r"[^A-Za-z0-9]")

    # Rule 4: Overall validation flag
    df["needs_followup"] = (
        df["missing_insurance_provider"]
        | df["missing_policy_number"]
        | df["invalid_policy_length"]
        | df["suspicious_policy_chars"]
    )

    return df

if __name__ == "__main__":
    validated_df = validate_intake_data()
    print(validated_df.head())

    