-- 1) All visits with patient name and provider
SELECT
    v.visit_id,
    v.visit_date,
    v.reason,
    v.provider,
    p.first_name,
    p.last_name,
    p.primary_insurance
FROM visits v
JOIN patients p
    ON v.patient_id = p.patient_id;

    -- 2) Number of visits per patient
SELECT
    p.patient_id,
    p.first_name,
    p.last_name,
    COUNT(v.visit_id) AS total_visits
FROM patients p
LEFT JOIN visits v
    ON p.patient_id = v.patient_id
GROUP BY
    p.patient_id,
    p.first_name,
    p.last_name;

    -- 3) Total visits grouped by primary insurance
SELECT
    p.primary_insurance,
    COUNT(v.visit_id) AS total_visits
FROM patients p
JOIN visits v
    ON p.patient_id = v.patient_id
GROUP BY
    p.primary_insurance;

  -- 5) All visits seen by 'Dr. Lee' after 2024-02-01
SELECT
    v.visit_id,
    v.visit_date,
    v.reason,
    p.first_name,
    p.last_name
FROM visits v
JOIN patients p
    ON v.patient_id = p.patient_id
WHERE
    v.provider = 'Dr. Lee'
    AND v.visit_date > '2024-02-01';  
    