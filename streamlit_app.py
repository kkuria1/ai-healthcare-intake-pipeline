import streamlit as st
import pandas as pd
import sqlite3

DB_PATH = "healthcare_ops.db"
TABLE = "intake_routed_ai_v2"

@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(f"SELECT * FROM {TABLE}", conn)
    conn.close()
    return df

st.set_page_config(page_title="Intake Triage Dashboard", layout="wide")

st.title("🏥 Intake Triage Dashboard (AI + Rules)")
st.caption("Filters + case-level review powered by SQLite + Python + Llama 3 (Ollama) outputs.")

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("Filters")

queue_options = ["All"] + sorted(df["routing_queue_v2"].dropna().unique().tolist())
risk_options = ["All"] + sorted(df["risk_level"].dropna().unique().tolist())
issue_type_options = ["All"] + sorted(df["insurance_issue_type"].dropna().unique().tolist())

queue = st.sidebar.selectbox("Routing Queue (v2)", queue_options)
risk = st.sidebar.selectbox("Risk Level", risk_options)
issue_type = st.sidebar.selectbox("Insurance Issue Type", issue_type_options)

search = st.sidebar.text_input("Search notes / summaries", "")

filtered = df.copy()

if queue != "All":
    filtered = filtered[filtered["routing_queue_v2"] == queue]
if risk != "All":
    filtered = filtered[filtered["risk_level"] == risk]
if issue_type != "All":
    filtered = filtered[filtered["insurance_issue_type"] == issue_type]

if search.strip():
    s = search.strip().lower()
    note_col = "note_text_clean" if "note_text_clean" in filtered.columns else None
    summary_col = "llm_summary" if "llm_summary" in filtered.columns else None

    mask = False
    if note_col:
        mask = mask | filtered[note_col].fillna("").str.lower().str.contains(s)
    if summary_col:
        mask = mask | filtered[summary_col].fillna("").str.lower().str.contains(s)

    filtered = filtered[mask]

# --- Top metrics ---
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total records", len(df))
c2.metric("Filtered", len(filtered))
c3.metric("High risk (filtered)", int((filtered.get("risk_level", "") == "High").sum()))
c4.metric("Insurance issues (filtered)", int((filtered.get("insurance_issue_detected", "") == "Yes").sum()))

st.divider()

# --- Table view ---
st.subheader("Worklist")
show_cols = [c for c in [
    "intake_id",
    "routing_queue_v2",
    "risk_level",
    "insurance_provider_clean",
    "insurance_issue_detected",
    "insurance_issue_type",
] if c in filtered.columns]

st.dataframe(filtered[show_cols].sort_values(by=["risk_level", "routing_queue_v2"], ascending=[False, True]),
             use_container_width=True,
             hide_index=True)

st.divider()

# --- Detail viewer ---
st.subheader("Case Viewer")

id_col = "intake_id"
ids = filtered[id_col].dropna().astype(int).tolist() if id_col in filtered.columns else []
if not ids:
    st.info("No records match your filters.")
else:
    selected_id = st.selectbox("Select intake_id", ids)
    row = filtered[filtered[id_col] == selected_id].iloc[0]

    left, right = st.columns(2)

    with left:
        st.markdown("### Intake Note")
        st.write(row.get("note_text_clean", ""))

        st.markdown("### AI Summary")
        st.write(row.get("llm_summary", ""))

    with right:
        st.markdown("### Routing & Flags")
        st.write({
            "routing_queue_v2": row.get("routing_queue_v2", ""),
            "risk_level": row.get("risk_level", ""),
            "needs_followup": row.get("needs_followup", ""),
            "insurance_issue_detected": row.get("insurance_issue_detected", ""),
            "insurance_issue_type": row.get("insurance_issue_type", ""),
            "insurance_issue_reason": row.get("insurance_issue_reason", ""),
        })

        st.markdown("### Insurance Fields")
        st.write({
            "insurance_provider_clean": row.get("insurance_provider_clean", ""),
            "policy_number_clean": row.get("policy_number_clean", ""),
        })
        