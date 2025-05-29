

INSERT INTO HRDW.DimDepartment VALUES 
(1, 'Data Engineering'),
(2, 'Data Science'),
(3, 'Analytics'),
(4, 'IT Support');



INSERT INTO HRDW.DimLocation VALUES 
(1, 'Perth'),
(2, 'Sydney'),
(3, 'Melbourne');




INSERT INTO HRDW.FactJobOpening VALUES
(1001, 'Data Engineer', 1, 1, 'SQL, Python, Azure', '2024-11-01', 'Open'),
(1002, 'Data Scientist', 2, 2, 'Python, ML, Azure ML', '2024-12-01', 'Open'),
(1003, 'BI Analyst', 3, 3, 'Power BI, SQL, DAX', '2025-01-15', 'Closed'),
(1004, 'Support Engineer', 4, 1, 'Windows, Helpdesk', '2025-02-01', 'Open');




INSERT INTO HRDW.IngestionControl VALUES
('SQLServer_HR', 'SQL', 1, 'Bronze_HRJobs', NULL, NULL),
('Web_Seek_PSM', 'WEB', 1, 'Bronze_WebJobs', NULL, 
 '{"cities":["Perth","Sydney","Melbourne"],"keyword":"data"}');
