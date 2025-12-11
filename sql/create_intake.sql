CREATE TABLE IF NOT EXISTS intake (
    intake_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    intake_date TEXT,
    insurance_provider TEXT,
    policy_number TEXT,
    note_text TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
