INSERT INTO intake (patient_id, intake_date, insurance_provider, policy_number, note_text)
VALUES
(1, '2024-01-02', 'Aetna', 'AT12345', 'New admission, reports dizziness and recent fall at home.'),
(1, '2024-02-08', 'Aetna', NULL, 'Follow-up intake, family unsure of updated policy number.'),
(2, '2024-01-10', 'Blue Cross', 'BC98765', 'Transfer from hospital, recent abdominal surgery.'),
(2, '2024-02-18', NULL, 'BC-?7789', 'Insurance form incomplete, policy number handwritten and unclear.'),
(3, '2024-01-09', 'UnitedHealthcare', 'UH55667', 'Complains of chronic knee pain, uses walker.'),
(3, '2024-02-27', 'UnitedHealthcare', NULL, 'Requesting medication refill authorization, pharmacy on hold.'),
(4, '2024-01-20', 'Kaiser', 'KAI44556', 'New admission, memory issues reported by family.'),
(4, '2024-03-01', 'Kaiser', 'KAI44556', 'Intake before neurology follow-up, needs transportation coordination.'),
(5, '2024-01-29', 'Medicare', 'MED77889', 'New resident, history of falls, uses cane.'),
(5, '2024-03-05', 'Medicare', NULL, 'Prior authorization may be required for new pain med.'),
(6, '2024-02-10', 'Aetna', 'AT99887', 'Short-term rehab after hip surgery, limited mobility.'),
(6, '2024-03-02', 'Aetna', 'AT99887', 'Intake for home health evaluation after discharge.'),
(7, '2024-01-28', 'Blue Cross', 'BC22334', 'Behavioral changes observed, family concerned about mood.'),
(7, '2024-03-04', NULL, NULL, 'Insurance card not present at intake, to be provided by family later.'),
(8, '2024-02-01', 'Aetna', 'AT65432', 'Chronic wound care patient, frequent dressing changes.'),
(8, '2024-03-11', 'Aetna', NULL, 'Possible prior auth needed for new wound vac equipment.'),
(9, '2024-01-08', 'UnitedHealthcare', 'UH33445', 'New intake, increased confusion per family report.'),
(9, '2024-03-14', 'UnitedHealthcare', NULL, 'Follow-up intake, family switching insurance plan soon.'),
(10, '2024-02-06', 'Medicare', 'MED44566', 'Admitted for weakness and falls, PT/OT eval ordered.'),
(10, '2024-03-18', 'Medicare', NULL, 'Insurance details being updated due to spouse retirement.');

