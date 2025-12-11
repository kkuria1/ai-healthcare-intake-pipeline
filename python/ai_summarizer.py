import subprocess
from data_loader import load_table

def ollama_generate(prompt: str, model: str = "llama3") -> str:
    """
    Call a local Ollama model and return the text response as a string.
    """
    # `ollama run <model>` reads the prompt from stdin and prints the response to stdout
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        text=True,
        capture_output=True
    )
    if result.returncode != 0:
        # Basic error handling – return a fallback string
        return f"[LLM ERROR] {result.stderr.strip()}"
    return result.stdout.strip()


def summarize_note_text(note_text: str) -> str:
    """
    Summarize an intake note in 1–2 sentences,
    focusing on clinical risk and insurance / follow-up needs.
    """
    note_text = "" if note_text is None else str(note_text)

    prompt = f"""
You are an assistant helping with healthcare intake operations.

Summarize the following intake note in 1–2 short sentences.
Focus on:
- clinical risk (falls, confusion, infection, pain, behavior)
- insurance or prior auth issues
- any follow-up that staff should be aware of.

Return ONLY the summary text, no bullet points, no labels.

Intake note:
\"\"\"{note_text}\"\"\"
"""
    return ollama_generate(prompt)


def generate_llm_summaries():
    """
    Load routed intake data from the 'intake_routed' table
    and generate an LLM summary for each row's note_text_clean.
    """
    df = load_table("intake_routed")

    # Make sure the column exists
    if "note_text_clean" not in df.columns:
        raise ValueError("Column 'note_text_clean' not found in intake_routed table.")

    df["llm_summary"] = df["note_text_clean"].apply(summarize_note_text)

    return df


if __name__ == "__main__":
    print("Generating LLM summaries with Ollama (model: llama3)...\n")
    enhanced_df = generate_llm_summaries()
    # Show a small sample
    print(
        enhanced_df[
            ["intake_id", "note_text_clean", "llm_summary"]
        ].head()
    )
    
