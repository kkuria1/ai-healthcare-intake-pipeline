import pandas as pd
from data_loader import load_table

def analyze_intake_routed():
    """Compute operational metrics from the intake_routed table."""
    
    df = load_table("intake_routed")

    metrics = {}

    # 1. Total records
    metrics["total_records"] = len(df)

    # 2. Queue distribution
    metrics["queue_distribution"] = df["routing_queue"].value_counts().to_dict()

    # 3. Follow-up percentage
    followup_count = df["needs_followup"].sum()
    metrics["needs_followup"] = {
        "count": int(followup_count),
        "percentage": round((followup_count / len(df)) * 100, 2)
    }

    # 4. Payer-level routing counts
    if "insurance_provider_clean" in df.columns:
        payer_distribution = (
            df.groupby("insurance_provider_clean")["routing_queue"]
              .value_counts()
              .unstack(fill_value=0)
              .to_dict()
        )
        metrics["payer_routing"] = payer_distribution

    # 5. High-risk clinical routing count
    metrics["clinical_review_count"] = int((df["routing_queue"] == "clinical_review").sum())

    return metrics


if __name__ == "__main__":
    results = analyze_intake_routed()

    print("\n=== INTAKE ROUTED ANALYTICS ===\n")

    print(f"Total intake records: {results['total_records']}")
    print("\nQueue distribution:")
    for queue, count in results["queue_distribution"].items():
        print(f"  {queue}: {count}")

    print("\nRecords needing follow-up:")
    print(f"  Count: {results['needs_followup']['count']}")
    print(f"  Percent: {results['needs_followup']['percentage']}%")

    print("\nClinical review workload:")
    print(f"  {results['clinical_review_count']} records routed to clinical review")

    if "payer_routing" in results:
        print("\nRouting by payer:")
        for payer, routes in results["payer_routing"].items():
            print(f"  {payer}: {routes}")

        