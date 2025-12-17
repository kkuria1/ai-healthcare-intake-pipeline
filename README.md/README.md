
⸻
 AI-Driven Healthcare Intake Automation Pipeline

End-to-end data cleaning, validation, routing, and AI summarization using SQLite, Python, and local Llama 3 (Ollama).

⸻

📘 Overview

This project implements a realistic healthcare intake operations pipeline.
It processes intake notes and insurance information through a full data workflow:
	1.	Extract data from SQLite
	2.	Clean inconsistent fields
	3.	Validate insurance information
	4.	Route each intake into operational queues
	5.	Enrich notes with AI summaries using a local LLM (Llama 3 via Ollama)
	6.	Persist enriched data back into the database
	7.	Analyze operational metrics and generate case-study samples

## ⭐ Project Highlights (What this demonstrates)

- Built an end-to-end healthcare intake pipeline: cleaning → validation → routing → AI enrichment → writeback → analytics
- Integrated a local LLM (Llama 3 via Ollama) to generate summaries and structured extractions (risk + insurance issues)
- Implemented hybrid routing logic (rules + AI signals) with persisted v2 outputs in SQLite
- Added human-in-the-loop evaluation:
  - labeled ground truth set
  - confusion table scoring
  - severity-weighted scoring to reflect healthcare risk
- Delivered a Streamlit triage dashboard for filtering by queue, risk, and insurance issue type

The goal is to demonstrate real-world AI Ops, Product Ops, and Healthcare Data Engineering capability.

⸻

🏗️ Architecture

SQLite → Python ETL → Cleaning → Validation → Routing → AI Summaries → Writeback → Analytics

	•	SQLite stores source tables (patients, visits, incidents, claims, intake)
	•	Python ETL modules load, clean, validate, and route intake data
	•	Ollama (Llama 3) generates concise AI summaries for intake notes
	•	Analytics + case study scripts output operational insights and examples

⸻

📂 Project Structure

ai-ops-roadmap/
│
├── SQL/
│   ├── create_*.sql           # schema creation
│   ├── insert_*.sql           # sample data loaders
│   └── *_queries.sql          # analytics queries
│
├── python/
│   ├── data_loader.py         # load any SQL table into Pandas
│   ├── clean_intake.py        # normalize intake fields
│   ├── validate_intake.py     # detect missing/bad insurance, bad formats
│   ├── intake_pipeline.py     # full clean + validate pipeline
│   ├── router.py              # rule-based intake routing engine
│   ├── writeback_intake.py    # write routed results to SQLite + CSV
│   ├── ai_summarizer.py       # Llama 3 summarization via Ollama
│   ├── writeback_intake_ai.py # write LLM summaries to DB
│   ├── analytics_intake.py    # operational KPIs
│   └── case_study_intake_ai.py# narrative examples per routing queue
│
├── data/
│   └── intake_routed_ai.csv   # exported AI-enriched data
│
└── healthcare_ops.db          # SQLite database


⸻

🔄 Workflow Overview

1. Intake Cleaning
	•	Standardizes insurance provider names
	•	Strips policy numbers
	•	Normalizes note text

2. Validation Layer

Flags:
	•	missing insurance provider
	•	missing policy number
	•	invalid policy number (too short or malformed)
	•	suspicious characters (?, -, etc.)

3. Rule-Based Routing Engine

Routes each intake into:

Queue	Reason
insurance_followup	Missing/invalid insurance info
prior_auth_team	Mentions “auth”, “authorization”
clinical_review	Contains clinical risk terms (falls, confusion, wound, behavior)
general_intake	Everything else

4. AI Summaries (Llama 3 via Ollama)

Each intake note is condensed into a 1–2 sentence summary highlighting:
	•	clinical risk
	•	insurance issues
	•	operational follow-up needs

5. Writeback Layer

AI-enriched output is stored in:

intake_routed_ai

and exported to:

data/intake_routed_ai.csv

6. Analytics & Case Study Views

Python scripts analyze:
	•	queue distribution
	•	follow-up rates
	•	payer-specific routing patterns
	•	clinical workload distribution
	•	AI-enhanced case samples

⸻

📊 Example Output (Case Study)

=== Queue: clinical_review (3 samples) ===

Intake ID: 14
Insurance Provider: Blue Cross
Needs Follow-up: No

Original Note:
  Behavioral changes observed, family concerned about mood.

AI Summary:
  Patient showing behavioral changes and mood concerns; may require evaluation by clinical team.

------------------------------------------------------------
⸻

🧠 Why This Project Matters

Healthcare operations deal with:
	•	messy text
	•	inconsistent insurance data
	•	high-risk patient notes
	•	prior authorization complexity
	•	heavy manual review

This project demonstrates the ability to:
	•	Design ETL pipelines
	•	Implement validation & routing systems
	•	Integrate local LLMs
	•	Persist enriched operational data
	•	Produce meaningful analytics

It aligns strongly with roles in:
	•	AI Ops
	•	Healthcare Product Operations
	•	Clinical Operations Engineering
	•	Data Engineering / ETL
	•	AI Workflow Automation

⸻

🛠 Installation & Usage

1. Start Ollama

ollama serve
ollama pull llama3

2. Run the pipeline

python3 python/writeback_intake.py

3. Generate AI summaries

python3 python/writeback_intake_ai.py

4. Operational analytics

python3 python/analytics_intake.py

5. Case-study samples

python3 python/case_study_intake_ai.py

## Quickstart (Local)

### 1) Install dependencies
```bash
pip install -r requirements.txt


## 📸 Demo Screenshots

### Worklist View
![Worklist](screenshots/dashboard_worklist.png)

### Case Viewer
![Case Viewer](screenshots/dashboard_case_view.png)

⸻

## 🔧 What I’d improve next (Production hardening)

- Add automated tests for routing rules + extraction parsing
- Add batch processing + concurrency controls for LLM calls
- Add monitoring metrics (drift, cache hit rate, latency)
- Add role-based access and audit logging for clinical workflows
- Deploy as a service (FastAPI) with a hosted dashboard


⸻

📄 License

MIT License.

⸻
