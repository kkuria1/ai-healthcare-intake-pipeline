import pandas as pd
from intake_pipeline import intake_pipeline

def assign_queue(row):
    """
    Simple rule-based routing for intake rows.
    Returns a queue name based on validation flags and note_text.
    """

    note = str(row.get("note_text_clean", "")).lower()

    # 1) If validation shows insurance issues → send to insurance follow-up
    if row.get("needs_followup", False):
        return "insurance_followup"

    # 2) If note suggests prior authorization → route to prior auth team
    if "prior auth" in note or "authorization" in note or "auth" in note:
        return "prior_auth_team"

    # 3) If note mentions fall, confusion, or high-risk signals → route to clinical review
    high_risk_keywords = ["fall", "confusion", "aggressive", "infection", "wound", "hip pain"]
    if any(keyword in note for keyword in high_risk_keywords):
        return "clinical_review"

    # 4) Default queue
    return "general_intake"


def route_intake():
    """
    Run the full intake pipeline and assign a routing_queue to each row.
    """
    df = intake_pipeline()

    # We assume note_text and validation flags are present in the merged dataframe.
    df["routing_queue"] = df.apply(assign_queue, axis=1)

    return df

if __name__ == "__main__":
    routed_df = route_intake()

    print("Routing queue distribution:")
    print(routed_df["routing_queue"].value_counts())

    print("\nSample routed rows:")
    print(
        routed_df[
            ["intake_id", "note_text_clean", "needs_followup", "routing_queue"]
        ].head()
    )
    






