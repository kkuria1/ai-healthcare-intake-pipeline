CREATE TABLE IF NOT EXISTS claims (
    claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    service_date TEXT,
    amount REAL,
    status TEXT,
    payer TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
