CREATE TABLE HRDW.Bronze_WebJobs (
    JobTitle NVARCHAR(200),
    Company NVARCHAR(200),
    Location NVARCHAR(100),
    City NVARCHAR(100),
    Summary NVARCHAR(MAX),
    Link NVARCHAR(500),
    LoadTimestamp DATETIME DEFAULT GETDATE()
);