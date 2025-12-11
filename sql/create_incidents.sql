CREATE TABLE IF NOT EXISTS incidents (
    incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    incident_date TEXT,
    type TEXT,
    severity TEXT,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
