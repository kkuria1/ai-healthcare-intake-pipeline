-- 1) All claims with patient names & payer
SELECT
    c.claim_id,
    c.service_date,
    c.amount,
    c.status,
    c.payer,
    p.first_name,
    p.last_name
FROM claims c
JOIN patients p
    ON c.patient_id = p.patient_id;

    -- 2) Denial rate by payer
SELECT
    payer,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN status = 'Denied' THEN 1 ELSE 0 END) AS denied_claims,
    ROUND(
        (SUM(CASE WHEN status = 'Denied' THEN 1 ELSE 0 END) * 1.0 / COUNT(*)) * 100,
        2
    ) AS denial_rate_percent
FROM claims
GROUP BY payer;

-- 3) Total dollar amount by payer
SELECT
    payer,
    SUM(amount) AS total_amount
FROM claims
GROUP BY payer;

-- 4) Average claim amount by status
SELECT
    status,
    AVG(amount) AS avg_amount
FROM claims
GROUP BY status;

-- 5) Patients with more than one denied claim (risk signal)
SELECT
    p.patient_id,
    p.first_name,
    p.last_name,
    COUNT(c.claim_id) AS denied_claims
FROM patients p
JOIN claims c
    ON p.patient_id = c.patient_id
WHERE c.status = 'Denied'
GROUP BY
    p.patient_id,
    p.first_name,
    p.last_name
HAVING COUNT(c.claim_id) > 1;

