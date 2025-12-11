-- 1) Count of records per routing queue
SELECT
    routing_queue,
    COUNT(*) AS count_per_queue
FROM intake_routed
GROUP BY routing_queue;

-- 2) How many records require follow-up based on validation
SELECT
    COUNT(*) AS total_rows,
    SUM(CASE WHEN needs_followup = 1 THEN 1 ELSE 0 END) AS followup_rows,
    ROUND(
        (SUM(CASE WHEN needs_followup = 1 THEN 1 ELSE 0 END) * 1.0 / COUNT(*)) * 100,
        2
    ) AS followup_percentage
FROM intake_routed;

-- 3) Routing queue counts grouped by insurance provider
SELECT
    insurance_provider_clean,
    routing_queue,
    COUNT(*) AS count_per_group
FROM intake_routed
GROUP BY insurance_provider_clean, routing_queue
ORDER BY insurance_provider_clean, routing_queue;


-- 4) Patients who repeatedly need follow-up
SELECT
    patient_id_clean AS patient_id,
    COUNT(*) AS followup_events
FROM intake_routed
WHERE needs_followup = 1
GROUP BY patient_id_clean
HAVING COUNT(*) > 1;

-- 5) Compare clinical_review vs insurance_followup volumes
SELECT
    routing_queue,
    COUNT(*) AS count_per_queue
FROM intake_routed
WHERE routing_queue IN ('clinical_review', 'insurance_followup')
GROUP BY routing_queue;


