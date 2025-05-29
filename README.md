# 📊 Job Market Analytics Platform

A hybrid data engineering project combining internal structured data from **SQL Server** and external web scraping (e.g., job ads from SEEK) using a **Metadata-Driven Architecture** in **Azure Data Factory**, processed in **Databricks**, and visualized in **Power BI**.

---

## 📌 Project Overview

This project demonstrates an end-to-end **Modern Data Platform** to analyze job market trends across major Australian cities (Perth, Sydney, Melbourne) by integrating internal HR data with external job postings scraped from the web.

---

## 🧱 Architecture Overview

![Architecture Diagram](Architecture/job-market-architecture.png)

---

## 🛠️ Technologies Used

| Layer                  | Tools / Services                           |
|------------------------|--------------------------------------------|
| **Data Source**        | SQL Server (On-Prem), Web Scraping (Python)|
| **Orchestration**      | Azure Data Factory (ADF)                   |
| **Transformation**     | Azure Databricks (Bronze → Silver → Gold)  |
| **Storage**            | Delta Lake on Azure Data Lake              |
| **Visualization**      | Power BI                                   |
| **Control**            | Metadata-Driven Ingestion Table (SQL)      |
| **Version Control**    | GitHub                                      |

---

## 🗃️ Folder Structure

```bash
📁 job-market-analytics/
├── 📂 data-ingestion/
│   ├── ingestion_control.sql
│   └── dim_fact_tables.sql
├── 📂 adf-pipelines/
│   └── metadata-driven-adf.json
├── 📂 databricks/
│   ├── bronze_to_silver_notebook.py
│   ├── silver_to_gold_notebook.py
│   └── web_scrape_seek.py
├── 📂 powerbi/
│   └── job-market-dashboard.pbix
├── 📂 images/
│   └── architecture-diagram.png
└── README.md

---

## 📅 Use Case Description
Analyze internal job openings across departments and locations.

Scrape and analyze external job listings (from SEEK) by city, title, and summary.

Combine and enrich both datasets for comparative market insights.

Enable metadata-driven automation for scalable ingestion pipelines.

---

## 🧩 SQL Server Data Warehouse
Schemas & Tables
HRDW.DimDepartment

HRDW.DimLocation

HRDW.FactJobOpening

HRDW.IngestionControl

HRDW.Bronze_WebJobs

✅ Data is pre-populated with sample job roles, departments, cities.

---

## 🧪 Azure Data Factory (ADF)
Uses Lookup activity to fetch ingestion metadata.

ForEach activity iterates over sources.

Switch handles SourceType logic (SQL or WEB).

Triggers:

PL_Copy_WebJobs_To_SQL: Executes Python web scraper.

Uses parameters from control table.

---

## 🔁 Web Scraping (Python + Seek)
Script: web_scrape_seek.py

Inputs: JSON config (cities, keywords) from IngestionControl.

Output: Bronze_WebJobs SQL table.

Parsed fields:

JobTitle, Company, Location, City, Summary, Link

---

## 🔁 Databricks (Bronze → Silver → Gold)
Bronze Layer: Raw ingestion tables (SQL + Web)

Silver Layer: Cleaned, transformed job postings

Gold Layer: Joined data for reporting

---

## 📊 Power BI Dashboard
Key Visuals:

Open vs Closed Positions by City

Market Job Postings vs Internal Postings

Skills Frequency in External Jobs

Time-Series of Job Openings

🔗 Connects directly to Gold Layer in Databricks via SQL Analytics endpoint or Delta Share.

---

## ⚙️ Metadata Control Table

CREATE TABLE HRDW.IngestionControl (
    SourceName NVARCHAR(100),
    SourceType NVARCHAR(50),
    IsActive BIT,
    TargetTable NVARCHAR(100),
    LastIngested DATETIME,
    Parameters NVARCHAR(MAX)
);
✅ Controls all ingestion jobs.
📦 Makes the pipeline scalable, modular, and automated.

---

## 💡 Key Learnings
Hybrid integration of internal SQL and external data

Metadata-driven orchestration with ADF

Bronze-Silver-Gold modeling using Delta Lake

End-to-end GitHub portfolio-ready project

---

## 🚀 Getting Started
Prerequisites
Azure Subscription

SQL Server (Local or Azure SQL DB)

Databricks Workspace

Power BI Desktop

Python (with requests, beautifulsoup4)

Steps
Clone the repo:

git clone https://github.com/your-username/job-market-analytics.git
cd job-market-analytics
Run SQL scripts from data-ingestion folder to create schema and tables.

Set up ADF pipeline using metadata-driven-adf.json.

Configure Databricks and execute notebooks under databricks/.

Open Power BI file and update dataset connection.

---

## 📬 Contact
Author: Mohsin Mukhtiar
📍 Perth, WA | 💼 BI Developer | 📧 mohsin@example.com
