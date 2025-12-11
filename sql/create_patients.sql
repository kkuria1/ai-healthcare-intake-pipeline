CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    dob TEXT,
    gender TEXT,
    primary_insurance TEXT,
    policy_number TEXT
);
