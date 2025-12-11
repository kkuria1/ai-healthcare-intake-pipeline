-- 1) All incidents with patient details
SELECT
    i.incident_id,
    i.incident_date,
    i.type,
    i.severity,
    p.first_name,
    p.last_name,
    p.primary_insurance
FROM incidents i
JOIN patients p
    ON i.patient_id = p.patient_id;

    -- 2) Number of incidents per patient
SELECT
    p.patient_id,
    p.first_name,
    p.last_name,
    COUNT(i.incident_id) AS total_incidents
FROM patients p
LEFT JOIN incidents i
    ON p.patient_id = i.patient_id
GROUP BY
    p.patient_id,
    p.first_name,
    p.last_name;

    -- 3) Number of incidents by severity level
SELECT
    severity,
    COUNT(*) AS count_by_severity
FROM incidents
GROUP BY severity;

-- 4) Total incidents grouped by insurance provider
SELECT
    p.primary_insurance,
    COUNT(i.incident_id) AS incident_count
FROM incidents i
JOIN patients p
    ON i.patient_id = p.patient_id
GROUP BY p.primary_insurance;

-- 5) All HIGH severity incidents with patient names
SELECT
    i.incident_id,
    i.incident_date,
    i.type,
    p.first_name,
    p.last_name,
    p.primary_insurance
FROM incidents i
JOIN patients p
    ON i.patient_id = p.patient_id
WHERE i.severity = 'High';

