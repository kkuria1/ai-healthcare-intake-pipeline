# AI-Driven Healthcare Intake Automation — Case Study

## Problem
Healthcare intake workflows rely heavily on manual review of unstructured notes and inconsistent insurance data. This leads to:
- delayed triage of high-risk cases
- insurance follow-up backlogs
- inconsistent routing decisions
- limited visibility into operational workload

## Objective
Design a system that:
- cleans and validates intake data
- routes intakes into operational queues
- uses AI to extract actionable signals from free-text notes
- supports evaluation, explainability, and human review

## Solution
I built an end-to-end intake automation pipeline using Python, SQLite, and a local LLM (Llama 3 via Ollama).

The system:
- normalizes intake and insurance fields
- flags missing/invalid insurance data
- routes records using hybrid rules + AI signals
- generates concise AI summaries
- extracts structured risk and insurance issue labels
- writes enriched outputs back to SQLite
- exposes results through analytics and a Streamlit dashboard

## Architecture
SQLite → Python ETL → Validation → AI Enrichment → Hybrid Routing → Writeback → Analytics & Dashboard

## AI & Logic
- LLM summaries (Llama 3) for intake notes
- Risk classification: Low / Moderate / High
- Insurance issue extraction:
  - Missing policy
  - Coverage unclear
  - Prior authorization
  - Eligibility
- Hybrid routing logic combining:
  - deterministic validation rules
  - AI-extracted signals
  - safety overrides for high-risk cases

## Evaluation
Implemented human-in-the-loop evaluation:
- Labeled ground truth set (20 samples)
- Accuracy + confusion table
- Severity-weighted scoring (high-risk misroutes penalized more)
- High-risk safety metric (% routed to clinical review)

## Outcomes
- Improved prioritization of high-risk cases
- More precise routing for prior authorization issues
- Reduced ambiguity in insurance follow-up workflows
- Clear, explainable AI outputs suitable for ops teams

## Tools
Python, Pandas, SQLite, SQL, Streamlit, Llama 3 (Ollama), AI workflow orchestration

## What I’d Improve Next
- Automated tests for routing rules
- Monitoring for model drift and extraction accuracy
- FastAPI deployment for real-time intake processing
- Role-based access controls for clinical workflows

