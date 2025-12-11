-- 1) All intake records with patient details
SELECT
    i.intake_id,
    i.intake_date,
    i.insurance_provider,
    i.policy_number,
    p.first_name,
    p.last_name
FROM intake i
JOIN patients p
    ON i.patient_id = p.patient_id;

    -- 2) Count how many intake records are missing insurance info
SELECT
    COUNT(*) AS missing_insurance_count
FROM intake
WHERE insurance_provider IS NULL
   OR policy_number IS NULL;

   -- 3) Number of intake records by insurance provider
SELECT
    insurance_provider,
    COUNT(*) AS intake_count
FROM intake
GROUP BY insurance_provider;

-- 4) Patients with more than one intake event
SELECT
    p.patient_id,
    p.first_name,
    p.last_name,
    COUNT(i.intake_id) AS total_intakes
FROM patients p
JOIN intake i
    ON p.patient_id = i.patient_id
GROUP BY
    p.patient_id,
    p.first_name,
    p.last_name
HAVING COUNT(i.intake_id) > 1;

-- 5) Intake notes that mention prior authorization
SELECT
    i.intake_id,
    i.intake_date,
    i.note_text,
    p.first_name,
    p.last_name
FROM intake i
JOIN patients p
    ON i.patient_id = p.patient_id
WHERE i.note_text LIKE '%auth%'
   OR i.note_text LIKE '%authorization%';

