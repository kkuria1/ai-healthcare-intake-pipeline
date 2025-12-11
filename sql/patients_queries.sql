SELECT * FROM patients;
SELECT COUNT(*) AS total_patients FROM patients;
SELECT primary_insurance, COUNT(*) AS count_per_insurance
FROM patients
GROUP BY primary_insurance;
SELECT first_name, last_name, dob
FROM patients
WHERE dob < '1985-01-01';
SELECT first_name, last_name, primary_insurance
FROM patients 
order BY last_name ASC;