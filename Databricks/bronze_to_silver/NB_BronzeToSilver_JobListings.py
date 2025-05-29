# Databricks notebook source
# ✅ Updated JDBC Connection for SQL Authentication

jdbc_url = "jdbc:sqlserver://localhost:1433;databaseName=JobMarketDW"

connection_properties = {
    "user": "admin",                      # Use your SQL login, e.g., 'sa'
    "password": "password", # Replace with your actual SQL login password
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}


# COMMAND ----------

# Web job listings from Bronze
df_web = spark.read.jdbc(
    url=jdbc_url,
    table="HRDW.Bronze_WebJobs",
    properties=connection_properties
)

# Internal job openings from SQL Server
df_sql = spark.read.jdbc(
    url=jdbc_url,
    table="HRDW.FactJobOpening",
    properties=connection_properties
)


# COMMAND ----------

from pyspark.sql.functions import lit

# Add source flag
df_web = df_web.withColumn("Source", lit("Web"))
df_sql = df_sql.withColumn("Source", lit("Internal"))

# Align columns
df_sql_renamed = df_sql.selectExpr(
    "Title as JobTitle",
    "NULL as Company",
    "NULL as Summary",
    "NULL as Link",
    "RequiredSkills",
    "LocationID as City",
    "OpeningDate as LoadTimestamp",
    "Status",
    "Source"
)

df_combined = df_web.select(
    "JobTitle", "Company", "Summary", "Link", lit(None).alias("RequiredSkills"),
    "City", "LoadTimestamp", lit("Open").alias("Status"), "Source"
).unionByName(df_sql_renamed)


# COMMAND ----------

df_combined.write.jdbc(
    url=jdbc_url,
    table="HRDW.Silver_CombinedJobs",
    mode="overwrite",  # or append
    properties=connection_properties
)
