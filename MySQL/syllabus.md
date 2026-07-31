If you're learning **MySQL specifically for Data Analytics**, you do **not** need to become a database administrator (DBA) or backend developer. Instead, your goal is to master querying, data cleaning, aggregation, analysis, optimization, and working with analytical datasets.

Below is a **comprehensive roadmap** that progresses from beginner to advanced. Completing this syllabus will cover **95–100% of the MySQL knowledge expected from a data analyst**, and will also prepare you for tools like Power BI, Tableau, Excel, and Python.

---

# COMPLETE MYSQL SYLLABUS FOR DATA ANALYTICS

## Module 1: Introduction to Databases

### What is a Database?

* Data vs Information
* Database Management System (DBMS)
* Relational Database (RDBMS)
* SQL vs MySQL
* Why MySQL is used
* OLTP vs OLAP
* Structured vs Unstructured Data

### Installation

* Install MySQL Server
* Install MySQL Workbench
* Create first connection
* Import sample databases
* Export databases

---

# Module 2: Database Fundamentals

Understand:

* Database
* Table
* Rows
* Columns
* Records
* Schema
* Primary Key
* Foreign Key
* Composite Key
* Candidate Key
* Surrogate Key

Learn:

* Data types

  * INT
  * FLOAT
  * DECIMAL
  * VARCHAR
  * CHAR
  * TEXT
  * DATE
  * DATETIME
  * TIMESTAMP
  * BOOLEAN

Difference between:

* CHAR vs VARCHAR
* DATE vs DATETIME
* FLOAT vs DECIMAL

---

# Module 3: SQL Basics

### Creating Database

```sql
CREATE DATABASE company;
```

### Using Database

```sql
USE company;
```

### Creating Tables

```sql
CREATE TABLE employees(
id INT PRIMARY KEY,
name VARCHAR(50),
salary INT
);
```

### Dropping

* DROP DATABASE
* DROP TABLE

### Truncate

```sql
TRUNCATE TABLE employees;
```

Difference:

* DELETE
* DROP
* TRUNCATE

---

# Module 4: CRUD Operations

## INSERT

```sql
INSERT INTO employees VALUES(...);
```

Multiple row insertion

---

## SELECT

Everything about SELECT

Selecting

```sql
SELECT *
```

Specific columns

Aliases

```sql
SELECT salary AS Income
```

DISTINCT

LIMIT

OFFSET

ORDER BY

ASC

DESC

---

## UPDATE

```sql
UPDATE employees
SET salary=50000
WHERE id=2;
```

---

## DELETE

Delete rows

Delete all rows

Safe updates

---

# Module 5: Filtering Data

WHERE clause

Operators

```
=
!=
<>
<
>
<=
>=
```

Logical operators

```
AND
OR
NOT
```

BETWEEN

IN

NOT IN

LIKE

Wildcards

```
%
_
```

IS NULL

IS NOT NULL

---

# Module 6: SQL Functions

## Numeric Functions

ABS

ROUND

CEIL

FLOOR

MOD

POWER

SQRT

RAND

---

## String Functions

LENGTH

LOWER

UPPER

CONCAT

SUBSTRING

LEFT

RIGHT

TRIM

LTRIM

RTRIM

REPLACE

REVERSE

LOCATE

INSTR

---

## Date Functions

NOW()

CURDATE()

CURTIME()

YEAR()

MONTH()

DAY()

DATEDIFF()

DATE_ADD()

DATE_SUB()

LAST_DAY()

EXTRACT()

TIMESTAMPDIFF()

---

## NULL Functions

IFNULL()

NULLIF()

COALESCE()

---

## Conditional Functions

IF()

CASE WHEN

---

# Module 7: Aggregate Functions

COUNT()

SUM()

AVG()

MIN()

MAX()

Statistical summaries

Business reporting

---

# Module 8: GROUP BY

Grouping data

Aggregation

Examples

Sales

Departments

Cities

Products

---

# Module 9: HAVING

Difference

```
WHERE
HAVING
```

Filtering grouped results

---

# Module 10: Sorting

ORDER BY

Multiple columns

ASC

DESC

NULL ordering

---

# Module 11: Joins (Very Important)

Concept of relationships

One-to-One

One-to-Many

Many-to-Many

---

## INNER JOIN

---

## LEFT JOIN

---

## RIGHT JOIN

---

## CROSS JOIN

---

## SELF JOIN

---

Learn

Joining

3 tables

4 tables

Multiple joins

Alias usage

---

# Module 12: Set Operations

UNION

UNION ALL

INTERSECT (concept)

EXCEPT (concept)

---

# Module 13: Subqueries

Single-row

Multiple-row

Correlated

Nested

Scalar

Derived tables

Using subqueries in

SELECT

WHERE

FROM

HAV---

# Module 14: Common Table Expressions (CTEs)

```sql
WITH sales AS (...)
```

Recursive CTE

Non-recursive

Why analysts use CTEs

---

# Module 15: Views

Create View

Update View

Drop View

Advantages

Security

Reusable queries

---

# Module 16: Constraints

Primary Key

Foreign Key

Unique

Check

Not Null

Default

Auto Increment

---

# Module 17: Normalization

1NF

2NF

3NF

BCNF (overview)

Denormalization

Why analytics databases are often denormalized

---

# Module 18: Indexing

What is Index

Clustered

Non-clustered (concept)

Composite Index

Unique Index

When NOT to use indexes

EXPLAIN

Query execution plan

---

# Module 19: Window Functions (Must Learn)

ROW_NUMBER()

RANK()

DENSE_RANK()

NTILE()

LAG()

LEAD()

FIRST_VALUE()

LAST_VALUE()

SUM OVER()

AVG OVER()

COUNT OVER()

Running totals

Moving averages

Ranking

Top N

Percentiles

---

# Module 20: Advanced SQL

CASE

Nested CASE

COALESCE

NULL handling

Pivoting (using CASE)

Unpivot concepts

---

# Module 21: Date Analytics

Monthly reports

Yearly reports

Quarterly reports

Rolling dates

Financial year calculations

Week calculations

Weekend detection

Business day calculations

---

# Module 22: Data Cleaning in SQL

Removing duplicates

TRIM spaces

Replacing NULLs

Splitting strings

Merging columns

Finding invalid data

Data standardization

Type conversions

Cleaning dates

---

# Module 23: Analytical SQL Problems

Top selling products

Customer retention

Monthly revenue

Running total

Moving average

Cumulative sales

Top customers

Revenue growth

Year-over-year growth

Category ranking

Sales by city

Sales funnel

Churn

Repeat customers

Average order value

Median

Percentile

---

# Module 24: Temporary Tables

Create

Drop

Use cases

Performance

---

# Module 25: Transactions

COMMIT

ROLLBACK

SAVEPOINT

ACID Properties

Isolation levels (overview)

---

# Module 26: Stored Procedures (Basic)

Create

Call

Parameters

Variables

Control flow

Useful to know, but not a major focus for analysts.

---

# Module 27: Stored Functions

Create Function

Return values

Parameters

---

# Module 28: Triggers (Awareness)

BEFORE INSERT

AFTER INSERT

UPDATE

DELETE

Business rules

---

# Module 29: Import and Export

CSV import

Excel import

Export CSV

Export SQL

Load large datasets

---

# Module 30: Performance Optimization

EXPLAIN

Indexes

Avoid SELECT *

Filtering early

Join optimization

Subquery vs JOIN

CTE performance

Window function optimization

---

# Module 31: MySQL Security (Basic)

Users

Roles

Privileges

GRANT

REVOKE

Passwords

---

# Module 32: MySQL with Excel

Import

ODBC

Refresh data

Power Query

---

# Module 33: MySQL with Python

Using

* mysql-connector-python
* SQLAlchemy
* pandas

Read SQL into pandas

```python
pd.read_sql()
```

Write data back

---

# Module 34: MySQL with Power BI

Direct Query

Import Mode

Relationships

Scheduled refresh

---

# Module 35: MySQL with Tableau

Connecting

Live connection

Extracts

Custom SQL

---

# Module 36: Real Business Database Design

Sales database

Retail database

HR database

Bank database

Hospital database

E-commerce database

Star schema

Snowflake schema

Fact tables

Dimension tables

---

# Module 37: Analytics Case Studies

Retail Analytics

Sales Analytics

HR Analytics

Marketing Analytics

Customer Analytics

Healthcare Analytics

Finance Analytics

Supply Chain Analytics

Telecommunications Analytics

---

# Module 38: Interview SQL

Top 100 SQL interview questions

LeetCode SQL problems

StrataScratch SQL

DataLemur SQL

Advanced joins

Window function questions

Ranking questions

Revenue questions

Retention questions

---

# Module 39: Real Projects

Complete end-to-end projects such as:

* Sales Dashboard
* Netflix Dataset Analysis
* Spotify Data Analysis
* IPL Data Analysis
* Walmart Sales Analysis
* Amazon Orders Analysis
* AdventureWorks Analysis
* Chinook Database Analysis
* Northwind Database Analysis
* E-commerce Customer Analytics
* COVID-19 Data Analysis
* Employee Attrition Analysis

---

# Module 40: Capstone Project

Bring everything together in a business-focused project:

* Design the schema
* Import raw data
* Clean the data
* Write analytical SQL queries
* Build reusable views and CTEs
* Optimize slow queries with indexes
* Connect to Power BI or Tableau
* Create an executive dashboard
* Present business insights and recommendations

## Suggested Learning Order

1. Database fundamentals
2. SQL basics (DDL & CRUD)
3. Filtering, sorting, and functions
4. Aggregate functions, `GROUP BY`, and `HAVING`
5. Joins
6. Subqueries and CTEs
7. Window functions
8. Data cleaning techniques
9. Analytical SQL patterns
10. Performance optimization
11. Integration with Python, Excel, and BI tools
12. Real-world projects and interview practice

## Topics You Can Treat as Secondary

For a data analytics career, you should understand these concepts but don't need deep expertise unless your role expands into database engineering:

* Stored procedures
* Stored functions
* Triggers
* User and privilege management
* Transaction isolation details
* Advanced server administration, replication, backups, and high availability

Focusing your effort on querying, joins, window functions, data cleaning, analytical patterns, and BI integration will provide the highest return for data analytics roles.
