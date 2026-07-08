# MySQL Syllabus for a Complete Data Analysis Course

## Course Context

This MySQL syllabus is designed as one major module inside a complete data-analysis program that also includes **Python, NumPy, pandas, Matplotlib, Seaborn, Excel, and Power BI**. The purpose of this module is not only to teach SQL syntax, but to make students capable of extracting, cleaning, transforming, validating, modeling, analyzing, and serving data from relational databases for real business analytics.

Recommended teaching version: **MySQL 8.4 LTS**
Recommended tools: **MySQL Server, MySQL Workbench, MySQL Shell or CLI, Python, pandas, SQLAlchemy or MySQL Connector/Python, Excel Power Query, Power BI Desktop**

MySQL Workbench should be included because it supports visual database modeling, EER diagrams, reverse engineering from live databases, forward engineering models into SQL scripts or live databases, table editing, and data insertion.

---

# 1. Learning Outcomes

By the end of the MySQL module, students should be able to:

1. Understand relational databases, schemas, tables, rows, columns, keys, relationships, and constraints.
2. Write clean, correct, readable SQL queries for real-world analysis.
3. Use `SELECT`, filtering, sorting, joins, grouping, subqueries, CTEs, window functions, and set operations.
4. Design normalized and analytics-friendly database structures.
5. Import, export, clean, transform, and validate data using SQL.
6. Build reusable analytical views for dashboards and reports.
7. Connect MySQL with Python, pandas, Excel, and Power BI.
8. Understand indexing, query execution plans, and basic query optimization.
9. Handle real-world business analytics tasks such as sales reports, cohorts, retention, customer segmentation, funnel analysis, inventory analysis, and KPI dashboards.
10. Follow basic security, backup, and production-readiness practices.

---

# 2. Prerequisites

Students should have:

1. Basic computer literacy.
2. Basic understanding of spreadsheets.
3. Basic mathematics: percentages, averages, ratios, growth rate, ranking.
4. Basic Python knowledge is helpful but not required at the start.
5. No prior database knowledge required.

---

# 3. Recommended Duration

For a serious data-analysis course, MySQL should not be taught as a short “SQL basics” module. Recommended duration:

**Minimum:** 30–35 hours
**Ideal:** 45–60 hours
**Advanced with projects:** 70+ hours

Suggested structure:

| Level                  |    Duration | Focus                                       |
| ---------------------- | ----------: | ------------------------------------------- |
| Foundation             | 10–12 hours | SQL basics, schema, simple queries          |
| Intermediate           | 15–20 hours | joins, grouping, subqueries, CTEs, cleaning |
| Advanced Analytics     | 15–20 hours | window functions, performance, BI modeling  |
| Integration & Projects | 10–20 hours | Python, pandas, Excel, Power BI, capstone   |

---

# 4. Module 1 — Introduction to Databases and MySQL

## Topics

1. What is data?
2. Structured, semi-structured, and unstructured data.
3. What is a database?
4. Database vs spreadsheet.
5. DBMS vs RDBMS.
6. What is MySQL?
7. MySQL vs SQL.
8. MySQL vs PostgreSQL vs SQL Server vs SQLite.
9. OLTP vs OLAP.
10. Role of MySQL in data analysis.
11. How analysts use SQL in companies.
12. Database client/server architecture.
13. MySQL Server, MySQL Workbench, MySQL Shell, command-line client.
14. Local database vs cloud database.
15. Real-world analytics pipeline: source data → MySQL → Python/pandas → Excel/Power BI → dashboard.

## Practical

1. Install MySQL Server.
2. Install MySQL Workbench.
3. Connect to local server.
4. Create first database.
5. Run first query.
6. Import a sample dataset.

## Student Outcome

Students should understand why SQL is a core analytics skill and where MySQL fits in the modern data-analysis workflow.

---

# 5. Module 2 — Relational Database Fundamentals

## Topics

1. Tables, rows, and columns.
2. Database, schema, table, field, record.
3. Primary key.
4. Foreign key.
5. Candidate key.
6. Composite key.
7. Surrogate key vs natural key.
8. One-to-one relationship.
9. One-to-many relationship.
10. Many-to-many relationship.
11. Junction/bridge tables.
12. Entity Relationship Diagram.
13. Enhanced ER/EER diagrams.
14. Referential integrity.
15. Cardinality.
16. Data redundancy.
17. Data anomalies.
18. Normalization.
19. First Normal Form.
20. Second Normal Form.
21. Third Normal Form.
22. When denormalization is useful for analytics.
23. Fact tables and dimension tables.
24. Transactional schema vs analytical schema.

Foreign keys should be taught properly because MySQL supports foreign keys and foreign-key constraints to cross-reference related data and maintain consistency between parent and child tables.

## Practical

1. Draw ERD for a retail business.
2. Convert spreadsheet data into relational tables.
3. Create customer, product, order, and order item tables.
4. Identify primary and foreign keys.

## Student Outcome

Students should be able to look at messy business data and design a logical relational structure.

---

# 6. Module 3 — MySQL Environment, Tools, and Workflow

## Topics

1. MySQL Server installation.
2. MySQL Workbench interface.
3. Command-line MySQL client.
4. MySQL Shell overview.
5. Creating connections.
6. Server, port, username, password.
7. Localhost vs remote host.
8. Database creation.
9. Running SQL scripts.
10. Saving scripts.
11. Formatting SQL.
12. Comments in SQL.
13. SQL execution order.
14. Error reading and debugging.
15. Safe update mode.
16. Result grid usage.
17. Exporting result sets.
18. Importing SQL files.
19. Using sample databases.
20. Basic troubleshooting.

## Practical

1. Create a new schema.
2. Run a `.sql` script.
3. Save query results.
4. Practice common errors: missing semicolon, wrong table name, wrong column name, wrong data type.

## Student Outcome

Students should become comfortable using MySQL tools without depending only on the instructor.

---

# 7. Module 4 — Basic SQL Querying with SELECT

## Topics

1. `SELECT`
2. `FROM`
3. Selecting all columns.
4. Selecting specific columns.
5. Column aliases.
6. Table aliases.
7. `DISTINCT`
8. `ORDER BY`
9. Ascending and descending sort.
10. `LIMIT`
11. `OFFSET`
12. Arithmetic expressions.
13. Calculated columns.
14. SQL comments.
15. Query readability.
16. Clause order vs logical execution order.
17. Naming conventions.
18. Avoiding `SELECT *` in production analysis.

## Practical

1. Retrieve all customers.
2. Retrieve selected columns.
3. Sort sales by amount.
4. Find top 10 products.
5. Create calculated revenue column.

## Student Outcome

Students should be able to retrieve and inspect data from a database.

---

# 8. Module 5 — Filtering Data

## Topics

1. `WHERE`
2. Comparison operators.
3. `AND`
4. `OR`
5. `NOT`
6. Operator precedence.
7. Parentheses in conditions.
8. `BETWEEN`
9. `IN`
10. `LIKE`
11. Wildcards `%` and `_`
12. `REGEXP`
13. `IS NULL`
14. `IS NOT NULL`
15. Filtering dates.
16. Filtering text.
17. Case sensitivity and collation basics.
18. Filtering numeric ranges.
19. Common filtering mistakes.
20. SARGable vs non-SARGable filters.

## Practical

1. Find customers from a city.
2. Find orders between two dates.
3. Find products containing a keyword.
4. Find missing phone numbers.
5. Find high-value orders.

## Student Outcome

Students should be able to extract precise subsets of data.

---

# 9. Module 6 — MySQL Data Types

## Topics

1. Why data types matter.
2. Numeric data types.
3. `TINYINT`, `SMALLINT`, `INT`, `BIGINT`.
4. `DECIMAL` vs `FLOAT` vs `DOUBLE`.
5. Why money should usually use `DECIMAL`.
6. Character data types.
7. `CHAR`
8. `VARCHAR`
9. `TEXT`
10. Date and time data types.
11. `DATE`
12. `TIME`
13. `DATETIME`
14. `TIMESTAMP`
15. `YEAR`
16. Boolean handling in MySQL.
17. `ENUM`
18. `SET`
19. Binary data.
20. `BLOB`
21. JSON data type.
22. Spatial data overview.
23. Default values.
24. Type conversion.
25. Choosing the right data type.
26. Character sets and collations.
27. `utf8mb4`.
28. Time zone considerations.

JSON should be included because MySQL has a native `JSON` data type that validates JSON documents and stores them in an optimized internal format for faster element access compared with plain text storage.

## Practical

1. Create a table using proper data types.
2. Store date, numeric, and text data.
3. Insert valid and invalid JSON.
4. Compare `DECIMAL` and `FLOAT` behavior.
5. Fix wrong data type choices.

## Student Outcome

Students should understand how wrong data types create wrong analysis.

---

# 10. Module 7 — Creating and Managing Tables

## Topics

1. `CREATE DATABASE`
2. `DROP DATABASE`
3. `CREATE TABLE`
4. `DROP TABLE`
5. `ALTER TABLE`
6. `RENAME TABLE`
7. `TRUNCATE`
8. `DESCRIBE`
9. `SHOW TABLES`
10. `SHOW COLUMNS`
11. `SHOW CREATE TABLE`
12. `NOT NULL`
13. `DEFAULT`
14. `AUTO_INCREMENT`
15. `PRIMARY KEY`
16. `UNIQUE`
17. `FOREIGN KEY`
18. `CHECK`
19. Generated columns.
20. Temporary tables.
21. Staging tables.
22. Table naming conventions.
23. Column naming conventions.
24. Data dictionary and metadata basics.

## Practical

1. Create a normalized sales database.
2. Add constraints.
3. Alter a table safely.
4. Create a staging table for imports.
5. Create generated columns for derived fields.

## Student Outcome

Students should be able to create clean, structured databases instead of only querying existing ones.

---

# 11. Module 8 — Inserting, Updating, and Deleting Data

## Topics

1. `INSERT`
2. Single-row insert.
3. Multi-row insert.
4. Insert selected columns.
5. `INSERT INTO ... SELECT`
6. `UPDATE`
7. `DELETE`
8. `TRUNCATE` vs `DELETE`
9. `REPLACE`
10. `INSERT ... ON DUPLICATE KEY UPDATE`
11. Safe updates.
12. Avoiding accidental full-table updates.
13. Transactions while modifying data.
14. Data validation before update/delete.
15. Audit columns: created_at, updated_at.
16. Soft delete vs hard delete.
17. Batch updates.

## Practical

1. Insert customer records.
2. Update product prices.
3. Delete test records.
4. Load transformed data from one table to another.
5. Build an upsert example.

## Student Outcome

Students should be able to safely modify data and understand the risks of destructive queries.

---

# 12. Module 9 — Importing and Exporting Data

## Topics

1. CSV import.
2. Excel to CSV workflow.
3. `LOAD DATA`
4. MySQL Workbench import wizard.
5. Handling headers.
6. Handling delimiters.
7. Handling quotes.
8. Handling encoding issues.
9. Handling date formats.
10. Handling missing values.
11. Staging table approach.
12. Data validation after import.
13. Export query result to CSV.
14. Export database dump.
15. Import SQL dump.
16. Backup vs export.
17. Data quality checks after loading.
18. Common import errors.

## Practical

1. Import customer CSV.
2. Import orders CSV.
3. Fix date format problems.
4. Validate row counts.
5. Export cleaned data for Excel or Power BI.

## Student Outcome

Students should be able to move real-world business files into MySQL and validate them.

---

# 13. Module 10 — Built-in Functions for Analysis

## Topics

### String Functions

1. `CONCAT`
2. `LENGTH`
3. `CHAR_LENGTH`
4. `LOWER`
5. `UPPER`
6. `TRIM`
7. `LTRIM`
8. `RTRIM`
9. `SUBSTRING`
10. `LEFT`
11. `RIGHT`
12. `REPLACE`
13. `LOCATE`
14. `REGEXP_REPLACE`, where available.

### Numeric Functions

1. `ROUND`
2. `CEIL`
3. `FLOOR`
4. `ABS`
5. `POWER`
6. `MOD`

### Date and Time Functions

1. `NOW`
2. `CURDATE`
3. `CURTIME`
4. `DATE`
5. `YEAR`
6. `MONTH`
7. `DAY`
8. `DAYNAME`
9. `MONTHNAME`
10. `WEEK`
11. `QUARTER`
12. `DATEDIFF`
13. `TIMESTAMPDIFF`
14. `DATE_ADD`
15. `DATE_SUB`
16. `DATE_FORMAT`

### Conditional and NULL Functions

1. `IF`
2. `CASE`
3. `IFNULL`
4. `NULLIF`
5. `COALESCE`

## Practical

1. Clean customer names.
2. Extract year/month from order dates.
3. Create age buckets.
4. Create revenue categories.
5. Replace missing values.

## Student Outcome

Students should be able to transform raw data into analysis-ready columns.

---

# 14. Module 11 — Aggregation and Business Metrics

## Topics

1. `COUNT`
2. `COUNT(*)` vs `COUNT(column)`
3. `SUM`
4. `AVG`
5. `MIN`
6. `MAX`
7. `GROUP BY`
8. `HAVING`
9. `DISTINCT`
10. Grouping by one column.
11. Grouping by multiple columns.
12. Aggregate filtering.
13. Revenue.
14. Profit.
15. Margin.
16. Average order value.
17. Customer count.
18. Active customers.
19. Repeat customers.
20. Conversion rate.
21. Month-wise analysis.
22. Category-wise analysis.
23. Region-wise analysis.
24. `WITH ROLLUP`
25. Common aggregation mistakes.

## Practical

1. Monthly sales report.
2. Category revenue report.
3. City-wise customer count.
4. Top products by quantity.
5. Profit margin report.

## Student Outcome

Students should be able to produce real business reports using SQL.

---

# 15. Module 12 — Joins

## Topics

1. Why joins are needed.
2. `INNER JOIN`
3. `LEFT JOIN`
4. `RIGHT JOIN`
5. `CROSS JOIN`
6. `SELF JOIN`
7. Multiple-table joins.
8. Joining more than two tables.
9. Join conditions.
10. Composite joins.
11. Natural join warning.
12. Joining on wrong keys.
13. Duplicate rows after joins.
14. One-to-many join multiplication.
15. Many-to-many joins.
16. Anti-join using `LEFT JOIN ... IS NULL`.
17. Semi-join using `EXISTS`.
18. Join vs subquery.
19. Join performance basics.
20. Join debugging checklist.

## Practical

1. Join customers and orders.
2. Join orders and products.
3. Find customers with no orders.
4. Find products never sold.
5. Build complete sales report from multiple tables.

## Student Outcome

Students should be able to combine data correctly without creating duplicate or misleading results.

---

# 16. Module 13 — Subqueries, Derived Tables, and CTEs

## Topics

1. What is a subquery?
2. Scalar subquery.
3. Row subquery.
4. Table subquery.
5. Subquery in `WHERE`.
6. Subquery in `FROM`.
7. Subquery in `SELECT`.
8. Correlated subquery.
9. `EXISTS`
10. `NOT EXISTS`
11. `ANY`
12. `ALL`
13. Derived tables.
14. Common Table Expressions.
15. `WITH`
16. Recursive CTE overview.
17. CTE vs subquery.
18. CTE readability.
19. CTEs for step-by-step analysis.
20. Performance considerations.

MySQL documentation places CTEs, subqueries, derived tables, set operations, and transactional statements as important parts of SQL querying, so they should not be treated as optional “advanced extras” in a serious analytics syllabus.

## Practical

1. Find customers above average spending.
2. Find products priced above category average.
3. Use CTE to build multi-step sales analysis.
4. Use recursive CTE for hierarchy basics.
5. Rewrite a subquery as a join and compare.

## Student Outcome

Students should be able to solve layered business questions cleanly.

---

# 17. Module 14 — Window Functions for Analytics

## Topics

1. What are window functions?
2. Window functions vs aggregate functions.
3. `OVER`
4. `PARTITION BY`
5. `ORDER BY` inside window.
6. Window frame.
7. `ROWS`
8. `RANGE`
9. `ROW_NUMBER`
10. `RANK`
11. `DENSE_RANK`
12. `NTILE`
13. `LAG`
14. `LEAD`
15. Running total.
16. Moving average.
17. Cumulative revenue.
18. First purchase and last purchase.
19. Customer ranking.
20. Product ranking.
21. Month-over-month comparison.
22. Retention analysis.
23. Deduplication using `ROW_NUMBER`.
24. Window function limitations.

Window functions must be included because MySQL 8.4 documents a full window-function section covering descriptions, concepts, syntax, frames, named windows, and restrictions.

## Practical

1. Rank products by monthly revenue.
2. Calculate running sales total.
3. Calculate moving average sales.
4. Find previous order date per customer.
5. Identify duplicate rows using `ROW_NUMBER`.

## Student Outcome

Students should be able to perform analyst-level calculations that are difficult with basic `GROUP BY`.

---

# 18. Module 15 — Set Operations

## Topics

1. `UNION`
2. `UNION ALL`
3. `INTERSECT`
4. `EXCEPT`
5. Duplicate handling.
6. Column compatibility.
7. Combining data from multiple sources.
8. Comparing customer lists.
9. Finding overlap between datasets.
10. Finding records present in one dataset but not another.

## Practical

1. Combine online and offline customer lists.
2. Find customers common to two campaigns.
3. Find customers missing from CRM.
4. Compare old and new product lists.

## Student Outcome

Students should be able to combine and compare datasets cleanly.

---

# 19. Module 16 — Data Cleaning with SQL

## Topics

1. Data profiling.
2. Row count validation.
3. Duplicate detection.
4. Duplicate removal strategy.
5. Missing values.
6. Invalid values.
7. Outlier detection.
8. Whitespace cleaning.
9. Case standardization.
10. Date standardization.
11. Numeric conversion.
12. Text parsing.
13. Category standardization.
14. Null handling.
15. Invalid foreign keys.
16. Orphan records.
17. Referential integrity checks.
18. Staging-to-production workflow.
19. Data quality report.
20. Audit queries.
21. Reconciliation between source and target.
22. Cleaning before Power BI.
23. Cleaning before pandas.

## Practical

1. Clean messy customer data.
2. Standardize city names.
3. Remove duplicate orders.
4. Detect orphan order records.
5. Create a data quality dashboard table.

## Student Outcome

Students should understand that data analysis is not only querying but also cleaning and validating data.

---

# 20. Module 17 — Analytical Case Studies in SQL

## Topics

1. Sales analysis.
2. Customer analysis.
3. Product analysis.
4. Inventory analysis.
5. Marketing campaign analysis.
6. Website/app funnel analysis.
7. Cohort analysis.
8. Retention analysis.
9. Churn indicators.
10. RFM segmentation.
11. ABC product classification.
12. Pareto analysis.
13. Basket analysis introduction.
14. Time-series reporting.
15. Daily, weekly, monthly KPIs.
16. Year-over-year growth.
17. Month-over-month growth.
18. Rolling averages.
19. Target vs actual analysis.
20. Dashboard-ready summary tables.

## Practical

1. Build monthly sales KPI table.
2. Build customer retention report.
3. Build RFM segmentation.
4. Build product performance ranking.
5. Build Power BI-ready reporting views.

## Student Outcome

Students should be able to answer real business questions using MySQL.

---

# 21. Module 18 — Views, Stored Objects, and Reusable Analysis

## Topics

1. What is a view?
2. Creating views.
3. Updating views.
4. Dropping views.
5. Analytical views.
6. Security use of views.
7. View limitations.
8. Stored procedures overview.
9. Stored functions overview.
10. Triggers overview.
11. Events overview.
12. When analysts should use views.
13. When analysts should avoid overusing stored procedures.
14. Reusable KPI layers.
15. Documentation of views.
16. Naming reporting views.

## Practical

1. Create a monthly revenue view.
2. Create customer summary view.
3. Create product performance view.
4. Use views in Power BI.
5. Create a simple stored procedure for refresh logic.

## Student Outcome

Students should be able to create reusable SQL assets for dashboards and reporting.

---

# 22. Module 19 — Indexing and Query Performance

## Topics

1. Why performance matters.
2. Full table scan.
3. Index concept.
4. B-tree index.
5. Primary key index.
6. Unique index.
7. Composite index.
8. Index column order.
9. Covering index.
10. Prefix index.
11. Full-text index overview.
12. Spatial index overview.
13. Indexes and joins.
14. Indexes and filters.
15. Indexes and sorting.
16. When indexes help.
17. When indexes hurt.
18. Write overhead of indexes.
19. SARGability.
20. Functions on indexed columns.
21. `EXPLAIN`
22. `EXPLAIN ANALYZE`
23. Query execution plan.
24. Join order.
25. Rows examined.
26. Cardinality.
27. Slow query log.
28. Basic query tuning checklist.
29. Partitioning overview.
30. Performance mistakes analysts make.

`EXPLAIN` must be taught because MySQL uses it to show how statements are executed, including join order and execution-plan information; MySQL 8.4 supports formats such as traditional, JSON, and tree-style output.

## Practical

1. Run a slow query.
2. Read `EXPLAIN`.
3. Add index.
4. Compare performance before and after index.
5. Optimize a dashboard query.

## Student Outcome

Students should not only write correct queries, but also write reasonably efficient queries.

---

# 23. Module 20 — Transactions, Locks, and Data Consistency

## Topics

1. What is a transaction?
2. ACID properties.
3. `START TRANSACTION`
4. `COMMIT`
5. `ROLLBACK`
6. Autocommit.
7. Savepoints.
8. Isolation levels.
9. Dirty read.
10. Non-repeatable read.
11. Phantom read.
12. Row locks.
13. Table locks.
14. Deadlocks overview.
15. Read consistency.
16. InnoDB basics.
17. Why analysts should understand transactions.
18. Safe data updates.
19. Reporting while data is changing.
20. Transaction examples in ETL.

## Practical

1. Insert records and rollback.
2. Update inside transaction and commit.
3. Simulate two sessions.
4. Understand locked rows.
5. Protect a batch update.

## Student Outcome

Students should understand data consistency and safe database modification.

---

# 24. Module 21 — Security, Users, Roles, and Permissions

## Topics

1. Authentication basics.
2. Creating users.
3. Passwords.
4. Roles.
5. Privileges.
6. `GRANT`
7. `REVOKE`
8. Least privilege principle.
9. Read-only analyst user.
10. Dashboard user.
11. Admin user.
12. Avoiding root user for analysis.
13. SQL injection overview.
14. Parameterized queries.
15. Environment variables for credentials.
16. Secure connection basics.
17. Data privacy.
18. Masking sensitive data.
19. PII handling.
20. Audit mindset.

## Practical

1. Create read-only user.
2. Grant access to one database.
3. Test restricted access.
4. Create a view hiding sensitive columns.
5. Use parameterized query from Python.

## Student Outcome

Students should understand safe and responsible data access.

---

# 25. Module 22 — Backup, Restore, and Database Maintenance Basics

## Topics

1. Why backups matter.
2. Logical backup.
3. Physical backup overview.
4. `mysqldump`
5. Restoring dump files.
6. Exporting selected tables.
7. Exporting query results.
8. Backup before destructive changes.
9. Data migration basics.
10. Schema migration basics.
11. Version control for SQL scripts.
12. Naming script files.
13. Documentation.
14. Basic maintenance mindset.
15. Disaster recovery overview.

## Practical

1. Backup a database.
2. Drop and restore a table.
3. Export schema only.
4. Export data only.
5. Maintain SQL script folder.

## Student Outcome

Students should know how to protect data before working on it.

---

# 26. Module 23 — MySQL with Python

## Topics

1. Why connect MySQL with Python?
2. MySQL Connector/Python.
3. SQLAlchemy overview.
4. DB-API concept.
5. Creating connection.
6. Creating cursor.
7. Executing SQL from Python.
8. Fetching results.
9. Parameterized queries.
10. Preventing SQL injection.
11. Reading MySQL data into pandas.
12. `pandas.read_sql`
13. Writing pandas DataFrame to MySQL.
14. Chunked reading for large data.
15. Batch insert.
16. Error handling.
17. Closing connections.
18. Using environment variables.
19. ETL workflow.
20. Logging pipeline steps.
21. Scheduling pipeline basics.
22. Data validation after loading.
23. MySQL + NumPy/pandas analysis.
24. MySQL + Matplotlib/Seaborn visualization.

MySQL Connector/Python should be covered because the official guide describes it as a self-contained Python driver for communicating with MySQL servers, and it is recommended for MySQL Server 8.0 and higher.

## Practical

1. Connect Python to MySQL.
2. Run a query and print results.
3. Load SQL result into pandas.
4. Clean data in pandas.
5. Write cleaned data back to MySQL.
6. Visualize MySQL data using Matplotlib and Seaborn.

## Student Outcome

Students should be able to combine SQL extraction with Python-based analysis.

---

# 27. Module 24 — MySQL with Excel and Power Query

## Topics

1. Why analysts still use Excel.
2. Export MySQL query results to CSV.
3. Import CSV into Excel.
4. Connect Excel Power Query to MySQL.
5. Data refresh basics.
6. Transform data in Power Query.
7. Load cleaned query results into Excel.
8. Pivot tables from MySQL data.
9. Excel dashboard from MySQL.
10. Common Excel/MySQL data type issues.
11. Date formatting issues.
12. Decimal and currency issues.
13. Refresh errors.
14. When to use Excel vs Power BI.

## Practical

1. Export monthly revenue from MySQL to Excel.
2. Create PivotTable from MySQL data.
3. Build Excel sales summary.
4. Refresh updated data.
5. Compare SQL aggregation with Excel PivotTable.

## Student Outcome

Students should be able to use MySQL as a reliable data source for Excel reporting.

---

# 28. Module 25 — MySQL with Power BI

## Topics

1. Why Power BI needs clean SQL sources.
2. MySQL connector in Power Query.
3. Connecting Power BI Desktop to MySQL.
4. Server and database settings.
5. Authentication.
6. Import mode.
7. DirectQuery mode.
8. Import vs DirectQuery comparison.
9. On-premises data gateway.
10. Native SQL query.
11. Query folding overview.
12. Star schema for Power BI.
13. Fact table.
14. Dimension table.
15. Date table.
16. KPI views.
17. Dashboard-ready views.
18. Refresh strategy.
19. Incremental refresh concept.
20. Performance considerations.
21. Avoiding heavy transformations in Power BI when SQL can do them better.
22. Data model relationships.
23. Power BI visuals from MySQL data.
24. Security and credentials.

Microsoft’s Power Query documentation includes a MySQL database connector where users provide server/database details, credentials, and then load or transform selected data; Power BI DirectQuery should also be taught because it keeps data in the source and queries it at report time instead of importing it, with important performance and limitation considerations.

## Practical

1. Connect Power BI to MySQL.
2. Load a reporting view.
3. Build sales dashboard.
4. Create relationships in Power BI model.
5. Compare Import and DirectQuery behavior.
6. Optimize SQL view for Power BI.

## Student Outcome

Students should be able to use MySQL as a professional Power BI data source.

---

# 29. Module 26 — Data Modeling for Analytics and BI

## Topics

1. Difference between normalized model and star schema.
2. OLTP model.
3. OLAP model.
4. Fact tables.
5. Dimension tables.
6. Grain of fact table.
7. Additive metrics.
8. Semi-additive metrics.
9. Non-additive metrics.
10. Date dimension.
11. Customer dimension.
12. Product dimension.
13. Geography dimension.
14. Slowly Changing Dimensions overview.
15. Bridge tables.
16. Snapshot tables.
17. Summary tables.
18. KPI tables.
19. Reporting views.
20. Dashboard performance.
21. Data mart concept.
22. Building a small analytics layer in MySQL.

## Practical

1. Convert transactional sales schema into star schema.
2. Create fact_sales table.
3. Create dimension tables.
4. Build Power BI-ready model.
5. Build dashboard from star schema.

## Student Outcome

Students should understand the database design expected in business intelligence work.

---

# 30. Module 27 — Semi-Structured Data and JSON Analytics

## Topics

1. Why JSON appears in databases.
2. JSON vs relational columns.
3. When to store JSON.
4. When not to store JSON.
5. JSON validation.
6. JSON path.
7. Extracting JSON values.
8. Searching JSON.
9. Modifying JSON.
10. Aggregating JSON.
11. Generated columns from JSON.
12. Indexing JSON-derived values.
13. API data stored in MySQL.
14. Flattening JSON for reporting.
15. JSON data and Power BI limitations.

## Practical

1. Store API-like JSON data.
2. Extract customer preference fields.
3. Convert JSON into reporting columns.
4. Create generated column from JSON value.
5. Build report from semi-structured data.

## Student Outcome

Students should be able to handle modern mixed-format data.

---

# 31. Module 28 — Real-World Analytics Projects

## Project 1: Retail Sales Analysis

Students build:

1. Database schema.
2. Data import pipeline.
3. Cleaned tables.
4. Sales KPIs.
5. Product performance report.
6. Customer segmentation.
7. Monthly trend report.
8. Power BI dashboard.

## Project 2: E-commerce Customer Analysis

Students build:

1. Customer order database.
2. First purchase analysis.
3. Repeat customer analysis.
4. Cohort retention report.
5. RFM segmentation.
6. Churn-risk indicator.
7. Python visualization.
8. Power BI dashboard.

## Project 3: HR Analytics

Students build:

1. Employee database.
2. Department analysis.
3. Salary analysis.
4. Attrition analysis.
5. Tenure analysis.
6. Diversity-safe aggregate reporting.
7. Excel summary.
8. Power BI dashboard.

## Project 4: Finance/Expense Analysis

Students build:

1. Transaction database.
2. Monthly expense report.
3. Category-wise spending.
4. Budget vs actual.
5. Anomaly detection queries.
6. Rolling average.
7. Dashboard view.

## Project 5: Inventory Analytics

Students build:

1. Product and stock database.
2. Stock movement table.
3. Reorder-level report.
4. Dead-stock report.
5. Fast-moving item report.
6. Supplier performance report.

---

# 32. Capstone Project

## Capstone Title

**End-to-End Business Data Analysis Using MySQL, Python, Excel, and Power BI**

## Capstone Requirements

Students must:

1. Select a business domain.
2. Create database schema.
3. Import raw data.
4. Clean and validate data.
5. Write at least 30 meaningful SQL queries.
6. Use joins, grouping, CTEs, and window functions.
7. Create reporting views.
8. Connect MySQL to Python.
9. Perform pandas-based validation or additional analysis.
10. Create at least two visualizations using Matplotlib or Seaborn.
11. Export or connect data to Excel.
12. Build Power BI dashboard.
13. Present insights, not just charts.
14. Document SQL scripts.
15. Explain database design.
16. Explain business recommendations.

## Minimum SQL Requirements

1. 5 basic queries.
2. 5 filtering queries.
3. 5 join queries.
4. 5 aggregation queries.
5. 3 subquery queries.
6. 3 CTE queries.
7. 3 window function queries.
8. 1 data cleaning workflow.
9. 1 performance optimization example.
10. 3 reporting views.

---

# 33. Assessment Plan

## Weekly Assignments

1. Query practice.
2. Schema design.
3. Data import task.
4. Data cleaning task.
5. Business report task.
6. Optimization task.
7. Python integration task.
8. Power BI integration task.

## Quizzes

1. SQL syntax quiz.
2. Joins quiz.
3. Aggregation quiz.
4. Data types quiz.
5. Window functions quiz.
6. Indexing quiz.
7. Data modeling quiz.

## Practical Exams

### Practical Exam 1 — SQL Foundations

Students must write basic queries, filters, sorting, and aggregations.

### Practical Exam 2 — Intermediate SQL

Students must solve joins, subqueries, CTEs, and data cleaning tasks.

### Practical Exam 3 — Advanced Analytics

Students must solve window functions, cohort analysis, KPI views, and query optimization.

### Final Project

Students present complete database-to-dashboard workflow.

---

# 34. Grading Rubric

| Area                                | Weight |
| ----------------------------------- | -----: |
| SQL correctness                     |    25% |
| Database design                     |    15% |
| Data cleaning and validation        |    15% |
| Analytical thinking                 |    15% |
| Python/pandas integration           |    10% |
| Excel/Power BI integration          |    10% |
| Query readability and documentation |     5% |
| Presentation and business insights  |     5% |

---

# 35. Must-Know Query Patterns

Students should master these patterns before the course is considered complete:

1. Top N records.
2. Bottom N records.
3. Duplicate detection.
4. Missing value detection.
5. Date range filtering.
6. Monthly grouping.
7. Year-over-year comparison.
8. Month-over-month growth.
9. Running total.
10. Moving average.
11. Ranking within category.
12. First transaction per customer.
13. Last transaction per customer.
14. Customers with no orders.
15. Products never sold.
16. Above-average customers.
17. Category contribution percentage.
18. Cumulative percentage.
19. 80/20 Pareto analysis.
20. RFM segmentation.
21. Cohort retention.
22. Funnel conversion.
23. Churn-risk logic.
24. Data reconciliation.
25. Incremental load detection.

---

# 36. Common Mistakes Students Must Be Trained to Avoid

1. Using `SELECT *` everywhere.
2. Forgetting `WHERE` in `UPDATE` or `DELETE`.
3. Misunderstanding `NULL`.
4. Using `COUNT(column)` when `COUNT(*)` is intended.
5. Creating duplicates through joins.
6. Joining on wrong columns.
7. Aggregating at the wrong grain.
8. Filtering after aggregation incorrectly.
9. Using `WHERE` instead of `HAVING`.
10. Misusing `DISTINCT`.
11. Ignoring data types.
12. Storing dates as text.
13. Storing money as floating-point values.
14. Ignoring primary keys.
15. Ignoring foreign keys.
16. Not validating imported row counts.
17. Not checking duplicate records.
18. Not reading error messages.
19. Creating indexes without understanding them.
20. Building dashboards from messy raw tables.
21. Doing everything in Power BI when SQL should prepare the data.
22. Hardcoding credentials in Python scripts.
23. Not documenting SQL logic.
24. Confusing business logic with technical logic.
25. Producing charts without verifying the underlying data.

---

# 37. Recommended Datasets

Use a mix of clean and messy datasets:

1. Retail sales data.
2. E-commerce orders.
3. Customer database.
4. Product catalog.
5. Inventory movements.
6. HR employee data.
7. Marketing campaigns.
8. Website funnel data.
9. Finance transactions.
10. Support tickets.
11. Subscription billing data.
12. Banking-style transaction data.
13. Restaurant orders.
14. Hospital appointment data.
15. Education/student performance data.

Each dataset should include:

1. Missing values.
2. Duplicate records.
3. Wrong date formats.
4. Inconsistent categories.
5. Multiple related tables.
6. Enough rows for performance practice.
7. Business questions to answer.

---

# 38. Recommended Teaching Sequence

## Phase 1 — Foundations

1. Database concepts.
2. MySQL setup.
3. Basic `SELECT`.
4. Filtering.
5. Sorting.
6. Data types.
7. Table creation.

## Phase 2 — Real Querying

1. DML.
2. Functions.
3. Aggregation.
4. Joins.
5. Subqueries.
6. CTEs.

## Phase 3 — Analytics

1. Window functions.
2. Business metrics.
3. Data cleaning.
4. Case studies.
5. Views.

## Phase 4 — Professional Skills

1. Indexing.
2. `EXPLAIN`.
3. Transactions.
4. Security.
5. Backup and restore.

## Phase 5 — Integration

1. MySQL with Python.
2. MySQL with pandas.
3. MySQL with Excel.
4. MySQL with Power BI.
5. Capstone project.

---

# 39. Final Course Completion Checklist

A student should not be certified as complete unless they can:

1. Design a relational schema.
2. Create tables with correct data types and constraints.
3. Import raw CSV data.
4. Clean messy data using SQL.
5. Write joins across 3 or more tables.
6. Build grouped KPI reports.
7. Use CTEs for multi-step logic.
8. Use window functions for ranking and running totals.
9. Create analytical views.
10. Read a basic `EXPLAIN` plan.
11. Add a useful index.
12. Connect MySQL to Python.
13. Load MySQL data into pandas.
14. Create visualizations from SQL data.
15. Connect MySQL to Power BI.
16. Build a dashboard from SQL views.
17. Explain business insights clearly.
18. Protect credentials and use read-only users.
19. Backup and restore a database.
20. Document SQL scripts professionally.

---

# 40. Suggested Final Statement for Students

By completing this MySQL module, students will not only know SQL syntax, but will also understand how databases support real data-analysis work. They will be able to move from raw business data to clean database tables, from database tables to analytical queries, from analytical queries to Python and pandas, and from prepared SQL views to Excel and Power BI dashboards.
