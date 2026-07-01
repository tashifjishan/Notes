# Module 11: Query Optimization Basics in MySQL

## Topics Covered

1. Query Optimization Basics
2. Indexes
3. `EXPLAIN`
4. Query Performance
5. Efficient Joins
6. Filtering Before Joining
7. Scalable Query Writing
8. Common Mistakes
9. Interview Questions
10. Practice Exercises

---

# 1. What is Query Optimization?

**Query optimization** means improving an SQL query so that it returns the same result using less time, less memory, and fewer scanned rows.

In simple words:

> Query optimization means making SQL queries faster and more efficient.

MySQL has an internal **optimizer** that decides how to execute a query, which indexes to use, and in what order tables should be joined. The `EXPLAIN` statement shows information from the optimizer about how MySQL plans to process a query, including join order and index usage. ([MySQL Developer Zone][1])

---

# 2. Why Query Optimization is Important

Poor queries can make an application slow even if the server is powerful.

Query optimization helps to:

| Benefit                 | Explanation                  |
| ----------------------- | ---------------------------- |
| Improve speed           | Query returns results faster |
| Reduce server load      | Less CPU and memory usage    |
| Reduce disk reads       | Fewer rows/pages are scanned |
| Improve user experience | App pages load faster        |
| Handle more users       | Better scalability           |
| Avoid timeout errors    | Useful for large datasets    |

---

# 3. Sample Tables for Examples

We will use these tables:

## customers

| customer_id | customer_name | city      |
| ----------- | ------------- | --------- |
| 1           | Ali           | Lahore    |
| 2           | Sara          | Karachi   |
| 3           | John          | Lahore    |
| 4           | Maria         | Islamabad |

## orders

| order_id | customer_id | order_date | total_amount | status    |
| -------- | ----------- | ---------- | ------------ | --------- |
| 101      | 1           | 2026-01-10 | 5000         | Completed |
| 102      | 1           | 2026-01-12 | 7000         | Pending   |
| 103      | 2           | 2026-01-15 | 3000         | Completed |
| 104      | 3           | 2026-02-01 | 9000         | Completed |

## products

| product_id | product_name | category_id | price |
| ---------- | ------------ | ----------- | ----- |
| 1          | Laptop       | 10          | 90000 |
| 2          | Mouse        | 10          | 1500  |
| 3          | Chair        | 20          | 12000 |

---

# 4. Basic Query Optimization Rules

Before using advanced tools, follow these simple rules:

| Rule                               | Meaning                                                           |
| ---------------------------------- | ----------------------------------------------------------------- |
| Avoid `SELECT *`                   | Select only needed columns                                        |
| Use indexes                        | Especially on `WHERE`, `JOIN`, `ORDER BY`, and `GROUP BY` columns |
| Filter early                       | Reduce rows before joining                                        |
| Avoid unnecessary joins            | Join only required tables                                         |
| Use proper data types              | Do not store numbers as text                                      |
| Avoid functions on indexed columns | They may prevent index usage                                      |
| Check query plan                   | Use `EXPLAIN`                                                     |
| Limit result size                  | Use `LIMIT` where suitable                                        |

---

# 5. Bad Query vs Optimized Query

## Bad Query

```sql
SELECT *
FROM orders;
```

Problem:

* Fetches all columns
* Fetches all rows
* Wastes memory and network bandwidth

## Better Query

```sql
SELECT order_id, customer_id, total_amount
FROM orders
WHERE status = 'Completed';
```

Better because:

* Selects only required columns
* Filters only completed orders
* Can use an index on `status`

---

# 6. Indexes in MySQL

An **index** is a database structure that helps MySQL find rows faster.

Think of an index like the index page of a book. Without an index, MySQL may need to scan every row. With an index, MySQL can directly find matching rows.

MySQL documentation states that one of the best ways to improve `SELECT` performance is to create indexes on columns tested in the query; index entries act like pointers to table rows and help MySQL quickly find matching rows in the `WHERE` clause. ([MySQL Developer Zone][2])

---

# 7. Why Indexes Improve Performance

Without index:

```sql
SELECT *
FROM customers
WHERE city = 'Lahore';
```

MySQL may scan every row.

With index:

```sql
CREATE INDEX idx_customers_city
ON customers(city);
```

Now MySQL can search `city` faster.

---

# 8. Creating an Index

## Syntax

```sql
CREATE INDEX index_name
ON table_name(column_name);
```

## Example

```sql
CREATE INDEX idx_orders_status
ON orders(status);
```

Now this query can become faster:

```sql
SELECT order_id, total_amount
FROM orders
WHERE status = 'Completed';
```

---

# 9. Index on Join Column

Join columns should usually be indexed.

```sql
CREATE INDEX idx_orders_customer_id
ON orders(customer_id);
```

This helps this join:

```sql
SELECT 
    c.customer_name,
    o.order_id,
    o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
```

---

# 10. Primary Key Index

A **primary key** automatically creates an index.

Example:

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50)
);
```

Here, `customer_id` is automatically indexed.

So this query is fast:

```sql
SELECT *
FROM customers
WHERE customer_id = 1;
```

---

# 11. Unique Index

A **unique index** prevents duplicate values and improves searching.

```sql
CREATE UNIQUE INDEX idx_users_email
ON users(email);
```

Useful for:

```sql
SELECT *
FROM users
WHERE email = 'test@example.com';
```

---

# 12. Composite Index

A **composite index** is an index on multiple columns.

```sql
CREATE INDEX idx_orders_status_date
ON orders(status, order_date);
```

Useful for:

```sql
SELECT order_id, total_amount
FROM orders
WHERE status = 'Completed'
AND order_date >= '2026-01-01';
```

---

# 13. Composite Index Order Matters

This index:

```sql
CREATE INDEX idx_orders_status_date
ON orders(status, order_date);
```

Works well for:

```sql
WHERE status = 'Completed';
```

and:

```sql
WHERE status = 'Completed'
AND order_date >= '2026-01-01';
```

But it may not be fully useful for:

```sql
WHERE order_date >= '2026-01-01';
```

because `status` is the first column in the index.

This is called the **leftmost prefix rule**.

---

# 14. Covering Index

A **covering index** contains all columns needed by the query.

Example:

```sql
CREATE INDEX idx_orders_status_amount
ON orders(status, total_amount);
```

Query:

```sql
SELECT total_amount
FROM orders
WHERE status = 'Completed';
```

Here, MySQL may get the required data directly from the index without reading the full table row.

---

# 15. When Indexes Help Most

Indexes are useful on columns used in:

```sql
WHERE
JOIN ON
ORDER BY
GROUP BY
DISTINCT
```

Example:

```sql
CREATE INDEX idx_orders_customer_status
ON orders(customer_id, status);
```

Useful for:

```sql
SELECT *
FROM orders
WHERE customer_id = 1
AND status = 'Completed';
```

---

# 16. When Indexes May Not Help

Indexes may not help when:

| Situation                             | Example                            |
| ------------------------------------- | ---------------------------------- |
| Table is very small                   | Full scan may be faster            |
| Column has low selectivity            | Gender: Male/Female                |
| Function is applied on indexed column | `YEAR(order_date) = 2026`          |
| Leading wildcard is used              | `LIKE '%phone'`                    |
| Wrong composite index order           | Index does not match query pattern |

---

# 17. Avoid Functions on Indexed Columns

## Bad Query

```sql
SELECT *
FROM orders
WHERE YEAR(order_date) = 2026;
```

Problem:

* Function `YEAR()` is applied to indexed column
* MySQL may not use the index efficiently

## Better Query

```sql
SELECT *
FROM orders
WHERE order_date >= '2026-01-01'
AND order_date < '2027-01-01';
```

This is better because the column remains unchanged and can use an index on `order_date`.

---

# 18. Avoid Leading Wildcard

## Bad Query

```sql
SELECT *
FROM products
WHERE product_name LIKE '%phone';
```

This may not use a normal index efficiently because the search starts with `%`.

## Better Query

```sql
SELECT *
FROM products
WHERE product_name LIKE 'phone%';
```

This can use an index more effectively because the search starts from the beginning of the string.

---

# 19. Checking Existing Indexes

```sql
SHOW INDEX FROM orders;
```

This shows indexes available on the `orders` table.

---

# 20. Dropping an Index

```sql
DROP INDEX idx_orders_status
ON orders;
```

Do this only if the index is unused or harmful.

---

# 21. Too Many Indexes Can Be Bad

Indexes improve read performance but can slow down write operations.

Because every time you run:

```sql
INSERT
UPDATE
DELETE
```

MySQL may need to update the indexes too.

So do not create indexes blindly.

---

# 22. What is `EXPLAIN`?

`EXPLAIN` is used to view how MySQL plans to execute a query.

Syntax:

```sql
EXPLAIN
SELECT *
FROM orders
WHERE status = 'Completed';
```

`EXPLAIN` works with `SELECT`, `DELETE`, `INSERT`, `REPLACE`, and `UPDATE`; it displays optimizer information about the execution plan, including how tables are joined and in which order. ([MySQL Developer Zone][1])

---

# 23. Why Use `EXPLAIN`?

Use `EXPLAIN` to answer:

| Question                      | Meaning               |
| ----------------------------- | --------------------- |
| Is MySQL using an index?      | Check `key` column    |
| Which indexes are possible?   | Check `possible_keys` |
| How many rows may be scanned? | Check `rows`          |
| Is it doing full table scan?  | Check `type = ALL`    |
| Is sorting required?          | Check `Extra`         |
| Is temporary table used?      | Check `Extra`         |

MySQL documentation specifically says `EXPLAIN` can help you see where to add indexes and whether tables are joined in an optimal order. ([MySQL Developer Zone][3])

---

# 24. Important Columns in EXPLAIN Output

Example:

```sql
EXPLAIN
SELECT *
FROM orders
WHERE status = 'Completed';
```

Common output columns:

| Column          | Meaning                                        |
| --------------- | ---------------------------------------------- |
| `id`            | Query step number                              |
| `select_type`   | Type of SELECT                                 |
| `table`         | Table being accessed                           |
| `type`          | Access method / join type                      |
| `possible_keys` | Indexes MySQL could use                        |
| `key`           | Index actually used                            |
| `key_len`       | Length of index used                           |
| `ref`           | Column or constant compared with index         |
| `rows`          | Estimated rows to examine                      |
| `filtered`      | Estimated percentage of rows passing condition |
| `Extra`         | Additional information                         |

---

# 25. Understanding EXPLAIN `type`

The `type` column is very important.

From best to worst, common values are:

| Type     | Meaning                                      | Performance            |
| -------- | -------------------------------------------- | ---------------------- |
| `system` | Table has one row                            | Best                   |
| `const`  | One matching row using primary/unique key    | Excellent              |
| `eq_ref` | One matching row per row from previous table | Excellent              |
| `ref`    | Uses non-unique index                        | Good                   |
| `range`  | Uses index range scan                        | Good                   |
| `index`  | Scans entire index                           | Medium                 |
| `ALL`    | Full table scan                              | Worst for large tables |

---

# 26. Example: Full Table Scan

Query:

```sql
EXPLAIN
SELECT *
FROM orders
WHERE status = 'Completed';
```

Possible result:

| table  | type | possible_keys | key  | rows   | Extra       |
| ------ | ---- | ------------- | ---- | ------ | ----------- |
| orders | ALL  | NULL          | NULL | 100000 | Using where |

Meaning:

* No index is used
* MySQL scans all rows
* Bad for large tables

---

# 27. Fixing Full Table Scan with Index

Create index:

```sql
CREATE INDEX idx_orders_status
ON orders(status);
```

Run again:

```sql
EXPLAIN
SELECT *
FROM orders
WHERE status = 'Completed';
```

Better result:

| table  | type | possible_keys     | key               | rows  | Extra                 |
| ------ | ---- | ----------------- | ----------------- | ----- | --------------------- |
| orders | ref  | idx_orders_status | idx_orders_status | 20000 | Using index condition |

Meaning:

* MySQL is using index
* Fewer rows scanned
* Better performance

MySQL also has **Index Condition Pushdown**, where parts of a `WHERE` condition that can be evaluated using index columns may be pushed down to the storage engine, reducing unnecessary row reads. ([MySQL Developer Zone][4])

---

# 28. `EXPLAIN FORMAT=JSON`

For more detailed output:

```sql
EXPLAIN FORMAT=JSON
SELECT *
FROM orders
WHERE status = 'Completed';
```

This gives a detailed JSON execution plan.

Useful for advanced analysis.

---

# 29. `EXPLAIN ANALYZE`

`EXPLAIN` shows estimated execution plan.

`EXPLAIN ANALYZE` actually runs the query and shows real execution information.

```sql
EXPLAIN ANALYZE
SELECT *
FROM orders
WHERE status = 'Completed';
```

MySQL introduced `EXPLAIN ANALYZE` in MySQL 8.0.18 as a way to execute the query, measure timing, count rows, and show where time is spent in the execution plan. ([MySQL Developer Zone][5])

Use carefully on large `UPDATE`, `DELETE`, or heavy queries because it actually executes the query.

---

# 30. Query Performance Basics

Query performance depends on:

| Factor                 | Explanation                              |
| ---------------------- | ---------------------------------------- |
| Number of rows scanned | Fewer scanned rows = faster query        |
| Index usage            | Correct indexes reduce search time       |
| Join strategy          | Efficient joins reduce workload          |
| Sorting                | Large `ORDER BY` can be expensive        |
| Grouping               | `GROUP BY` may need sorting/temp tables  |
| Selected columns       | Fewer columns reduce data transfer       |
| Data types             | Smaller and correct types perform better |
| Server resources       | CPU, RAM, disk speed also matter         |

---

# 31. Measuring Query Performance

Use:

```sql
EXPLAIN SELECT ...
```

Use:

```sql
EXPLAIN ANALYZE SELECT ...
```

Use query timing in MySQL client:

```sql
SELECT ...
```

Also check:

```sql
SHOW INDEX FROM table_name;
```

For slow production queries, DBAs often use slow query logs, but for beginner optimization, start with `EXPLAIN`.

---

# 32. Efficient Joins

A **join** combines rows from two or more tables.

Example:

```sql
SELECT 
    c.customer_name,
    o.order_id,
    o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
```

This joins customers with their orders.

MySQL executes joins using a nested-loop algorithm or variations of it, so indexing join columns is very important for performance. ([MySQL Developer Zone][6])

---

# 33. Common Join Types

| Join Type    | Meaning                                                             |
| ------------ | ------------------------------------------------------------------- |
| `INNER JOIN` | Returns matching rows only                                          |
| `LEFT JOIN`  | Returns all rows from left table and matching rows from right table |
| `RIGHT JOIN` | Returns all rows from right table and matching rows from left table |
| `CROSS JOIN` | Returns all combinations                                            |

---

# 34. Efficient INNER JOIN Example

```sql
SELECT 
    c.customer_name,
    o.order_id,
    o.total_amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.status = 'Completed';
```

Recommended indexes:

```sql
CREATE INDEX idx_orders_customer_status
ON orders(customer_id, status);

CREATE INDEX idx_customers_customer_id
ON customers(customer_id);
```

Usually `customer_id` in `customers` is already a primary key.

---

# 35. Bad Join Example

```sql
SELECT *
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
```

Problems:

* Uses `SELECT *`
* Returns unnecessary columns
* No filter
* May process many rows
* Can be expensive on large tables

---

# 36. Better Join Example

```sql
SELECT 
    c.customer_name,
    o.order_id,
    o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.status = 'Completed';
```

Better because:

* Selects only required columns
* Filters completed orders
* Uses clear join condition

---

# 37. Indexes for Joins

For efficient joins, index columns used in `ON`.

Example:

```sql
SELECT 
    c.customer_name,
    o.order_id
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
```

Recommended:

```sql
CREATE INDEX idx_orders_customer_id
ON orders(customer_id);
```

If `customers.customer_id` is primary key, it already has an index.

---

# 38. Efficient Join Checklist

Before writing a join query, check:

| Checklist                             | Yes/No |
| ------------------------------------- | ------ |
| Are join columns indexed?             |        |
| Are data types same on both sides?    |        |
| Are unnecessary tables removed?       |        |
| Are filters added in `WHERE` or `ON`? |        |
| Are only required columns selected?   |        |
| Did you check with `EXPLAIN`?         |        |

---

# 39. Avoid Joining on Different Data Types

Bad design:

```sql
customers.customer_id INT
orders.customer_id VARCHAR(20)
```

Query:

```sql
SELECT *
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
```

Problem:

* MySQL may need implicit conversion
* Index usage may become poor
* Query becomes slower

Better:

```sql
customers.customer_id INT
orders.customer_id INT
```

---

# 40. Avoid Functions in Join Conditions

Bad:

```sql
SELECT *
FROM customers c
JOIN orders o
ON LOWER(c.email) = LOWER(o.email);
```

Problem:

* Function is applied to join columns
* Index may not be used efficiently

Better:

* Store emails in normalized lowercase format
* Index the normalized email column

```sql
SELECT *
FROM customers c
JOIN orders o
ON c.email = o.email;
```

---

# 41. Filtering Before Joining

**Filtering before joining** means reducing rows first, then joining smaller result sets.

This is very important for performance.

Instead of joining millions of rows first, filter the required rows first.

---

# 42. Bad Approach: Join First, Filter Later

```sql
SELECT 
    c.customer_name,
    o.order_id,
    o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.status = 'Completed'
AND o.order_date >= '2026-01-01';
```

This query is not always bad because MySQL optimizer may push filters internally. But for learning and readability, think of it as:

1. Join customers and orders
2. Filter completed orders after joining

For large datasets, we want to make sure filters and indexes help reduce rows early.

---

# 43. Better Approach: Filter Orders First Using Derived Table

```sql
SELECT 
    c.customer_name,
    fo.order_id,
    fo.total_amount
FROM customers c
JOIN (
    SELECT order_id, customer_id, total_amount
    FROM orders
    WHERE status = 'Completed'
    AND order_date >= '2026-01-01'
) AS fo
ON c.customer_id = fo.customer_id;
```

Here:

* `orders` is filtered first
* Only completed 2026 orders are joined
* Join has fewer rows to process

Recommended index:

```sql
CREATE INDEX idx_orders_status_date_customer
ON orders(status, order_date, customer_id);
```

---

# 44. Filtering Before Joining Using CTE

```sql
WITH filtered_orders AS (
    SELECT order_id, customer_id, total_amount
    FROM orders
    WHERE status = 'Completed'
    AND order_date >= '2026-01-01'
)
SELECT 
    c.customer_name,
    fo.order_id,
    fo.total_amount
FROM customers c
JOIN filtered_orders fo
ON c.customer_id = fo.customer_id;
```

This is easier to read than a derived table.

---

# 45. Filtering Before Joining with Aggregation

Bad approach:

```sql
SELECT 
    c.customer_name,
    SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.status = 'Completed'
GROUP BY c.customer_id, c.customer_name;
```

Better for large datasets:

```sql
WITH order_totals AS (
    SELECT 
        customer_id,
        SUM(total_amount) AS total_spent
    FROM orders
    WHERE status = 'Completed'
    GROUP BY customer_id
)
SELECT 
    c.customer_name,
    ot.total_spent
FROM customers c
JOIN order_totals ot
ON c.customer_id = ot.customer_id;
```

Why better?

* Orders are filtered first
* Orders are grouped first
* Result has fewer rows before joining with customers

---

# 46. Filtering Before Joining with `EXISTS`

If you only need to check whether related records exist, use `EXISTS`.

Example: Find customers who have completed orders.

```sql
SELECT 
    c.customer_id,
    c.customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
    AND o.status = 'Completed'
);
```

This can be better than joining when you do not need order details.

Bad alternative:

```sql
SELECT DISTINCT 
    c.customer_id,
    c.customer_name
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.status = 'Completed';
```

Problem:

* Join can create duplicate customer rows
* `DISTINCT` adds extra work

---

# 47. Filtering Before Joining with Scalar Subquery

A **scalar subquery** returns one value.

Example: Find orders above average order amount.

```sql
SELECT 
    order_id,
    customer_id,
    total_amount
FROM orders
WHERE total_amount > (
    SELECT AVG(total_amount)
    FROM orders
);
```

This filters orders before any join.

Then you can join only filtered rows:

```sql
WITH high_value_orders AS (
    SELECT order_id, customer_id, total_amount
    FROM orders
    WHERE total_amount > (
        SELECT AVG(total_amount)
        FROM orders
    )
)
SELECT 
    c.customer_name,
    h.order_id,
    h.total_amount
FROM high_value_orders h
JOIN customers c
ON h.customer_id = c.customer_id;
```

This is a scalable pattern:

1. Calculate threshold
2. Filter important rows
3. Join reduced result

---

# 48. Efficient Filtering Rules

| Rule                     | Bad                     | Better                         |
| ------------------------ | ----------------------- | ------------------------------ |
| Avoid function on column | `YEAR(order_date)=2026` | Date range                     |
| Avoid leading wildcard   | `LIKE '%abc'`           | `LIKE 'abc%'`                  |
| Avoid `SELECT *`         | `SELECT *`              | Select needed columns          |
| Avoid unnecessary join   | Join table not used     | Remove join                    |
| Avoid duplicate rows     | Join + `DISTINCT`       | Use `EXISTS`                   |
| Filter early             | Join huge tables first  | Filter using CTE/derived table |

---

# 49. Query Optimization Example: Step-by-Step

## Requirement

Find Lahore customers who placed completed orders in 2026.

---

## Version 1: Poor Query

```sql
SELECT *
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE c.city = 'Lahore'
AND o.status = 'Completed'
AND YEAR(o.order_date) = 2026;
```

Problems:

* `SELECT *`
* Uses `YEAR()` on date column
* May not use date index efficiently
* Could scan too many rows

---

## Version 2: Better Query

```sql
SELECT 
    c.customer_name,
    o.order_id,
    o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE c.city = 'Lahore'
AND o.status = 'Completed'
AND o.order_date >= '2026-01-01'
AND o.order_date < '2027-01-01';
```

Better:

* Selects required columns
* Uses date range
* Easier for index usage

---

## Version 3: Add Indexes

```sql
CREATE INDEX idx_customers_city_id
ON customers(city, customer_id);

CREATE INDEX idx_orders_status_date_customer
ON orders(status, order_date, customer_id);
```

Now MySQL can filter customers and orders more efficiently.

---

## Version 4: Check with EXPLAIN

```sql
EXPLAIN
SELECT 
    c.customer_name,
    o.order_id,
    o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE c.city = 'Lahore'
AND o.status = 'Completed'
AND o.order_date >= '2026-01-01'
AND o.order_date < '2027-01-01';
```

Look for:

| EXPLAIN Column | Good Sign                                                   |
| -------------- | ----------------------------------------------------------- |
| `key`          | Index is used                                               |
| `rows`         | Low estimated rows                                          |
| `type`         | `ref`, `range`, `eq_ref`, `const`                           |
| `Extra`        | Avoid large `Using temporary`, `Using filesort` if possible |

---

# 50. `ORDER BY` Optimization

Bad:

```sql
SELECT *
FROM orders
WHERE status = 'Completed'
ORDER BY order_date;
```

Better:

```sql
SELECT order_id, customer_id, total_amount, order_date
FROM orders
WHERE status = 'Completed'
ORDER BY order_date;
```

Useful index:

```sql
CREATE INDEX idx_orders_status_date
ON orders(status, order_date);
```

This index helps both filtering and sorting.

---

# 51. `GROUP BY` Optimization

Query:

```sql
SELECT customer_id, SUM(total_amount) AS total_spent
FROM orders
WHERE status = 'Completed'
GROUP BY customer_id;
```

Useful index:

```sql
CREATE INDEX idx_orders_status_customer
ON orders(status, customer_id);
```

This helps MySQL filter by status and group by customer.

---

# 52. `LIMIT` Optimization

Use `LIMIT` when you do not need all rows.

```sql
SELECT order_id, total_amount
FROM orders
WHERE status = 'Completed'
ORDER BY order_date DESC
LIMIT 10;
```

Useful index:

```sql
CREATE INDEX idx_orders_status_date
ON orders(status, order_date);
```

---

# 53. Avoid Large OFFSET

Bad for large pages:

```sql
SELECT order_id, total_amount
FROM orders
ORDER BY order_id
LIMIT 20 OFFSET 100000;
```

Problem:

* MySQL may scan many rows before returning 20 rows

Better keyset pagination:

```sql
SELECT order_id, total_amount
FROM orders
WHERE order_id > 100000
ORDER BY order_id
LIMIT 20;
```

This is faster when `order_id` is indexed.

---

# 54. `IN` vs `EXISTS`

## Using `IN`

```sql
SELECT customer_name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    WHERE status = 'Completed'
);
```

## Using `EXISTS`

```sql
SELECT customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
    AND o.status = 'Completed'
);
```

General rule:

| Situation                  | Prefer                        |
| -------------------------- | ----------------------------- |
| Need to check existence    | `EXISTS`                      |
| Need to match small list   | `IN`                          |
| Subquery may return `NULL` | `EXISTS` or careful filtering |
| Need actual joined data    | `JOIN`                        |

---

# 55. Avoid `NOT IN` with NULL

Problem:

```sql
SELECT customer_name
FROM customers
WHERE customer_id NOT IN (
    SELECT customer_id
    FROM orders
);
```

If the subquery returns `NULL`, results may become unexpected.

Better:

```sql
SELECT customer_name
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

---

# 56. Query Optimization with Joins: Practical Example

## Requirement

Show customers who spent more than 10,000 on completed orders.

Bad:

```sql
SELECT 
    c.customer_name,
    SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(o.total_amount) > 10000
AND o.status = 'Completed';
```

Problem:

* `o.status = 'Completed'` should be in `WHERE`, not `HAVING`
* `HAVING` should filter grouped results
* `WHERE` should filter rows before grouping

Better:

```sql
SELECT 
    c.customer_name,
    SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.status = 'Completed'
GROUP BY c.customer_id, c.customer_name
HAVING SUM(o.total_amount) > 10000;
```

Even better with CTE:

```sql
WITH completed_order_totals AS (
    SELECT 
        customer_id,
        SUM(total_amount) AS total_spent
    FROM orders
    WHERE status = 'Completed'
    GROUP BY customer_id
    HAVING SUM(total_amount) > 10000
)
SELECT 
    c.customer_name,
    cot.total_spent
FROM completed_order_totals cot
JOIN customers c
ON cot.customer_id = c.customer_id;
```

---

# 57. WHERE vs HAVING for Performance

| Clause   | Used For       | Runs Before/After Grouping |
| -------- | -------------- | -------------------------- |
| `WHERE`  | Filters rows   | Before grouping            |
| `HAVING` | Filters groups | After grouping             |

Use `WHERE` whenever possible because it reduces rows earlier.

Bad:

```sql
SELECT customer_id, SUM(total_amount)
FROM orders
GROUP BY customer_id
HAVING status = 'Completed';
```

Better:

```sql
SELECT customer_id, SUM(total_amount)
FROM orders
WHERE status = 'Completed'
GROUP BY customer_id;
```

---

# 58. Select Only Required Columns

Bad:

```sql
SELECT *
FROM orders
WHERE status = 'Completed';
```

Better:

```sql
SELECT order_id, customer_id, total_amount
FROM orders
WHERE status = 'Completed';
```

Benefits:

* Less data transfer
* Less memory usage
* Can use covering index
* Cleaner output

---

# 59. Avoid Unnecessary DISTINCT

Bad:

```sql
SELECT DISTINCT c.customer_name
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id;
```

If you only want customers who have orders, use:

```sql
SELECT c.customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

This avoids duplicate rows before removing them.

---

# 60. Avoid OR When It Blocks Index Usage

Sometimes `OR` can make index usage less efficient.

Example:

```sql
SELECT *
FROM orders
WHERE status = 'Completed'
OR status = 'Pending';
```

Better:

```sql
SELECT *
FROM orders
WHERE status IN ('Completed', 'Pending');
```

For different columns:

```sql
SELECT *
FROM users
WHERE email = 'a@test.com'
OR phone = '12345';
```

Possible alternative:

```sql
SELECT *
FROM users
WHERE email = 'a@test.com'

UNION

SELECT *
FROM users
WHERE phone = '12345';
```

This can allow separate indexes on `email` and `phone`.

---

# 61. Avoid Implicit Type Conversion

Bad:

```sql
SELECT *
FROM orders
WHERE customer_id = '10';
```

If `customer_id` is integer, use:

```sql
SELECT *
FROM orders
WHERE customer_id = 10;
```

Why?

* Avoids unnecessary conversion
* Helps index usage
* Cleaner SQL

---

# 62. Optimizing COUNT Queries

Bad:

```sql
SELECT COUNT(*)
FROM orders
WHERE YEAR(order_date) = 2026;
```

Better:

```sql
SELECT COUNT(*)
FROM orders
WHERE order_date >= '2026-01-01'
AND order_date < '2027-01-01';
```

Index:

```sql
CREATE INDEX idx_orders_order_date
ON orders(order_date);
```

---

# 63. Optimizing Search Queries

Bad:

```sql
SELECT *
FROM products
WHERE product_name LIKE '%laptop%';
```

This is slow on large tables.

Better options:

1. Use prefix search if possible:

```sql
SELECT *
FROM products
WHERE product_name LIKE 'laptop%';
```

2. Use full-text index for text search:

```sql
CREATE FULLTEXT INDEX idx_products_name
ON products(product_name);
```

Query:

```sql
SELECT *
FROM products
WHERE MATCH(product_name) AGAINST('laptop');
```

---

# 64. Efficient Join Order

In many cases, MySQL chooses join order automatically.

But as a developer, you should still write queries clearly:

* Start from the most relevant table
* Apply filters early
* Use proper indexes
* Avoid unnecessary joins
* Use `EXPLAIN` to verify actual plan

`EXPLAIN` helps check whether the optimizer joins tables in a good order. ([MySQL Developer Zone][3])

---

# 65. Inner Join vs Left Join Performance

Use `INNER JOIN` when matching rows are required.

```sql
SELECT c.customer_name, o.order_id
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;
```

Use `LEFT JOIN` only when you need all rows from the left table.

```sql
SELECT c.customer_name, o.order_id
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;
```

Do not use `LEFT JOIN` unnecessarily.

---

# 66. LEFT JOIN Filter Mistake

Wrong:

```sql
SELECT c.customer_name, o.order_id
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.status = 'Completed';
```

Problem:

* The `WHERE` condition can remove customers without orders
* It behaves like an `INNER JOIN`

Better if you want all customers and only completed orders if available:

```sql
SELECT c.customer_name, o.order_id
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
AND o.status = 'Completed';
```

MySQL documentation explains that for a `LEFT JOIN`, the join condition is used to decide how to retrieve rows from the right table, so placing filters in `ON` versus `WHERE` can change both meaning and execution behavior. ([MySQL Developer Zone][7])

---

# 67. Query Optimization Workflow

Use this workflow in real projects:

## Step 1: Identify Slow Query

Find query that is slow.

## Step 2: Run EXPLAIN

```sql
EXPLAIN SELECT ...
```

## Step 3: Check Full Table Scans

Look for:

```sql
type = ALL
key = NULL
rows = very high
```

## Step 4: Add or Improve Index

Create index on:

* Filter columns
* Join columns
* Sorting columns
* Grouping columns

## Step 5: Rewrite Query

Improve:

* `WHERE`
* `JOIN`
* `GROUP BY`
* `ORDER BY`
* Subqueries
* CTEs

## Step 6: Test Again

Run:

```sql
EXPLAIN SELECT ...
```

or:

```sql
EXPLAIN ANALYZE SELECT ...
```

## Step 7: Compare Results

Compare:

* Execution time
* Rows scanned
* Index used
* Query output correctness

---

# 68. Common Optimization Mistakes

## Mistake 1: Creating Index on Every Column

Bad idea.

Indexes use storage and slow down writes.

Create indexes based on query patterns.

---

## Mistake 2: Not Using EXPLAIN

Never guess performance.

Use:

```sql
EXPLAIN SELECT ...
```

---

## Mistake 3: Using `SELECT *`

Bad:

```sql
SELECT *
FROM orders;
```

Better:

```sql
SELECT order_id, customer_id, total_amount
FROM orders;
```

---

## Mistake 4: Filtering After Grouping

Bad:

```sql
SELECT customer_id, SUM(total_amount)
FROM orders
GROUP BY customer_id
HAVING status = 'Completed';
```

Better:

```sql
SELECT customer_id, SUM(total_amount)
FROM orders
WHERE status = 'Completed'
GROUP BY customer_id;
```

---

## Mistake 5: Missing Index on Foreign Key

Bad:

```sql
JOIN orders o
ON c.customer_id = o.customer_id
```

without index on `orders.customer_id`.

Better:

```sql
CREATE INDEX idx_orders_customer_id
ON orders(customer_id);
```

---

## Mistake 6: Using Functions on Indexed Columns

Bad:

```sql
WHERE DATE(created_at) = '2026-01-01'
```

Better:

```sql
WHERE created_at >= '2026-01-01'
AND created_at < '2026-01-02'
```

---

# 69. Quick Revision Table

| Concept            | Meaning                           | Example                    |
| ------------------ | --------------------------------- | -------------------------- |
| Query optimization | Making SQL faster                 | Rewrite query, add index   |
| Index              | Helps MySQL find rows faster      | `CREATE INDEX`             |
| Primary key index  | Automatic unique index            | `id INT PRIMARY KEY`       |
| Composite index    | Index on multiple columns         | `(status, order_date)`     |
| Covering index     | Index contains all needed columns | `status, total_amount`     |
| EXPLAIN            | Shows query execution plan        | `EXPLAIN SELECT ...`       |
| Full table scan    | Reads all rows                    | `type = ALL`               |
| Efficient join     | Join using indexed columns        | `ON customer_id`           |
| Filter before join | Reduce rows before joining        | CTE/derived table          |
| WHERE              | Filters rows before grouping      | `WHERE status='Completed'` |
| HAVING             | Filters groups after grouping     | `HAVING SUM(total)>10000`  |

---

# 70. Interview Questions and Answers

## Q1. What is query optimization?

Query optimization is the process of improving SQL queries so they execute faster and use fewer resources.

---

## Q2. What is an index?

An index is a database structure that helps MySQL find rows faster without scanning the entire table.

---

## Q3. Which columns should be indexed?

Columns used frequently in:

```sql
WHERE
JOIN
ORDER BY
GROUP BY
```

should be considered for indexing.

---

## Q4. Can too many indexes be harmful?

Yes. Too many indexes slow down `INSERT`, `UPDATE`, and `DELETE` operations because indexes also need to be updated.

---

## Q5. What is EXPLAIN?

`EXPLAIN` shows how MySQL plans to execute a query, including index usage, join order, estimated rows scanned, and access type.

---

## Q6. What does `type = ALL` mean in EXPLAIN?

It means MySQL is doing a full table scan. This is usually bad for large tables.

---

## Q7. What does `key = NULL` mean in EXPLAIN?

It means MySQL did not use an index for that table.

---

## Q8. What is a composite index?

A composite index is an index created on more than one column.

Example:

```sql
CREATE INDEX idx_status_date
ON orders(status, order_date);
```

---

## Q9. What is filtering before joining?

Filtering before joining means reducing rows first using `WHERE`, CTEs, derived tables, or aggregation, then joining the smaller result set.

---

## Q10. Difference between WHERE and HAVING?

`WHERE` filters rows before grouping. `HAVING` filters grouped results after `GROUP BY`.

---

# 71. Practice Exercises

## Exercise 1

Create an index on `orders.status`.

```sql
CREATE INDEX idx_orders_status
ON orders(status);
```

---

## Exercise 2

Use `EXPLAIN` to check this query:

```sql
EXPLAIN
SELECT order_id, total_amount
FROM orders
WHERE status = 'Completed';
```

---

## Exercise 3

Optimize this query:

```sql
SELECT *
FROM orders
WHERE YEAR(order_date) = 2026;
```

Correct answer:

```sql
SELECT order_id, customer_id, total_amount, order_date
FROM orders
WHERE order_date >= '2026-01-01'
AND order_date < '2027-01-01';
```

Index:

```sql
CREATE INDEX idx_orders_order_date
ON orders(order_date);
```

---

## Exercise 4

Create an efficient join query between customers and orders.

```sql
SELECT 
    c.customer_name,
    o.order_id,
    o.total_amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.status = 'Completed';
```

Index:

```sql
CREATE INDEX idx_orders_customer_status
ON orders(customer_id, status);
```

---

## Exercise 5

Filter before joining using a CTE.

```sql
WITH filtered_orders AS (
    SELECT order_id, customer_id, total_amount
    FROM orders
    WHERE status = 'Completed'
)
SELECT 
    c.customer_name,
    fo.order_id,
    fo.total_amount
FROM customers c
JOIN filtered_orders fo
ON c.customer_id = fo.customer_id;
```

---

# 72. Final Summary

Query optimization in MySQL means writing SQL in a way that reduces unnecessary work. The most important beginner-level tools are **indexes** and **EXPLAIN**. Indexes help MySQL find rows faster, while `EXPLAIN` helps you understand whether the query is using indexes properly. Efficient joins require indexed join columns, matching data types, selected columns only, and early filtering. For scalable queries, filter rows before joining, avoid functions on indexed columns, use `WHERE` before `GROUP BY`, and always test performance with `EXPLAIN`.

[1]: https://dev.mysql.com/doc/refman/8.0/en/explain.html?utm_source=chatgpt.com "MySQL 8.0 Reference Manual :: 15.8.2 EXPLAIN Statement"
[2]: https://dev.mysql.com/doc/refman/8.0/en/optimization-indexes.html?utm_source=chatgpt.com "10.3 Optimization and Indexes"
[3]: https://dev.mysql.com/doc/refman/8.1/en/using-explain.html?utm_source=chatgpt.com "10.8.1 Optimizing Queries with EXPLAIN"
[4]: https://dev.mysql.com/doc/refman/8.4/en/index-condition-pushdown-optimization.html?utm_source=chatgpt.com "10.2.1.6 Index Condition Pushdown Optimization"
[5]: https://dev.mysql.com/blog-archive/mysql-explain-analyze/?utm_source=chatgpt.com "MySQL EXPLAIN ANALYZE"
[6]: https://dev.mysql.com/doc/search/?d=201&p=1&q=join&utm_source=chatgpt.com "MySQL 8.0 Reference Manual"
[7]: https://dev.mysql.com/doc/refman/8.0/en/outer-join-optimization.html?utm_source=chatgpt.com "10.2.1.9 Outer Join Optimization"
