CREATE TABLE IF NOT EXISTS visits (
    visit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER, 
    visit_date TEXT,
    reason TEXT, provider TEXT,     
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);
