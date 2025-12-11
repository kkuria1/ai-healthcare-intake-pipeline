import pandas as pd
from data_loader import load_table

def load_ai_routed_intake():
    """Load the AI-enriched intake_routed_ai table."""
    df = load_table("intake_routed_ai")
    return df

def print_case_study_samples(df, queue_name, n=3):
    """
    Print n sample rows for a given routing queue
    showing original note, flags, and AI summary.
    """
    subset = df[df["routing_queue"] == queue_name].head(n)

    if subset.empty:
        print(f"\n--- No records found for queue: {queue_name} ---")
        return

    print(f"\n=== Queue: {queue_name} (showing up to {n} samples) ===\n")

    for _, row in subset.iterrows():
        intake_id = row.get("intake_id")
        note = row.get("note_text_clean", "")
        summary = row.get("llm_summary", "")
        needs_followup = row.get("needs_followup", 0)
        insurance = row.get("insurance_provider_clean", row.get("insurance_provider_validated", "Unknown"))

        print(f"Intake ID: {intake_id}")
        print(f"Insurance Provider: {insurance}")
        print(f"Needs Follow-up: {'Yes' if needs_followup == 1 else 'No'}")
        print("\nOriginal Note:")
        print(f"  {note}")
        print("\nAI Summary:")
        print(f"  {summary}")
        print("\n" + "-" * 60 + "\n")


def main():
    df = load_ai_routed_intake()

    print("\n=== HIGH-LEVEL OVERVIEW ===\n")
    print(f"Total records: {len(df)}")

    print("\nRouting queue distribution:")
    print(df["routing_queue"].value_counts())

    print("\nFollow-up rate:")
    followup_count = df["needs_followup"].sum()
    followup_pct = round((followup_count / len(df)) * 100, 2)
    print(f"  Count: {followup_count}")
    print(f"  Percent: {followup_pct}%")

    # Print case-study style slices per queue
    for queue in ["insurance_followup", "prior_auth_team", "clinical_review", "general_intake"]:
        if queue in df["routing_queue"].unique():
            print_case_study_samples(df, queue, n=3)


if __name__ == "__main__":
    main()
    