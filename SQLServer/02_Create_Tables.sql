CREATE TABLE HRDW.DimDepartment (
    DepartmentID INT PRIMARY KEY,
    DepartmentName NVARCHAR(100)
);

CREATE TABLE HRDW.DimLocation (
    LocationID INT PRIMARY KEY,
    LocationName NVARCHAR(100)
);

CREATE TABLE HRDW.FactJobOpening (
    JobID INT PRIMARY KEY,
    Title NVARCHAR(150),
    DepartmentID INT,
    LocationID INT,
    RequiredSkills NVARCHAR(MAX),
    OpeningDate DATE,
    Status NVARCHAR(50), -- Open, Closed
    FOREIGN KEY (DepartmentID) REFERENCES HRDW.DimDepartment(DepartmentID),
    FOREIGN KEY (LocationID) REFERENCES HRDW.DimLocation(LocationID)
);

CREATE TABLE HRDW.IngestionControl (
    SourceName NVARCHAR(100),           -- e.g., 'SQLServer_HR', 'Web_Seek'
    SourceType NVARCHAR(50),            -- e.g., 'SQL', 'WEB'
    IsActive BIT,                       -- Control flag for orchestration
    TargetTable NVARCHAR(100),          -- Table to load into (e.g., Bronze layer)
    LastIngested DATETIME NULL,         -- Optional: last run timestamp
    Parameters NVARCHAR(MAX) NULL       -- For JSON-style parameters if needed
);