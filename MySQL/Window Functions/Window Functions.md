MySQL window functions (introduced in MySQL 8.0) perform calculations across a set of rows related to the current row, without collapsing the result set like `GROUP BY` does.

## Basic Syntax

```sql
function_name(...) OVER (
    [PARTITION BY column1, column2, ...]
    [ORDER BY column1, column2, ...]
    [ROWS | RANGE frame_clause]
)
```

Example:

```sql
SELECT
    employee_id,
    salary,
    AVG(salary) OVER () AS avg_salary
FROM employees;
```

---

# Ranking Functions

### ROW_NUMBER()

Assigns a unique sequential number.

```sql
SELECT
    name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;
```

### RANK()

Leaves gaps after ties.

```sql
SELECT
    name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS rank_num
FROM employees;
```

Example ranking:

| Salary | RANK |
| ------ | ---- |
| 100    | 1    |
| 100    | 1    |
| 90     | 3    |

### DENSE_RANK()

No gaps after ties.

```sql
SELECT
    name,
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;
```

| Salary | DENSE_RANK |
| ------ | ---------- |
| 100    | 1          |
| 100    | 1          |
| 90     | 2          |

### NTILE(n)

Splits rows into buckets.

```sql
SELECT
    name,
    salary,
    NTILE(4) OVER (ORDER BY salary DESC) AS quartile
FROM employees;
```

---

# Aggregate Window Functions

### SUM()

Running total:

```sql
SELECT
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
    ) AS running_total
FROM orders;
```

### AVG()

```sql
SELECT
    employee_id,
    salary,
    AVG(salary) OVER (
        PARTITION BY department_id
    ) AS dept_avg
FROM employees;
```

### COUNT()

```sql
SELECT
    department_id,
    employee_id,
    COUNT(*) OVER (
        PARTITION BY department_id
    ) AS dept_count
FROM employees;
```

### MIN() / MAX()

```sql
SELECT
    employee_id,
    salary,
    MAX(salary) OVER (
        PARTITION BY department_id
    ) AS dept_max_salary
FROM employees;
```

---

# Value Functions

### LAG()

Access previous row.

```sql
SELECT
    sale_date,
    amount,
    LAG(amount) OVER (
        ORDER BY sale_date
    ) AS prev_amount
FROM sales;
```

### LEAD()

Access next row.

```sql
SELECT
    sale_date,
    amount,
    LEAD(amount) OVER (
        ORDER BY sale_date
    ) AS next_amount
FROM sales;
```

### FIRST_VALUE()

```sql
SELECT
    employee_id,
    salary,
    FIRST_VALUE(salary) OVER (
        ORDER BY salary DESC
    ) AS highest_salary
FROM employees;
```

### LAST_VALUE()

Usually requires an explicit frame:

```sql
SELECT
    employee_id,
    salary,
    LAST_VALUE(salary) OVER (
        ORDER BY salary
        ROWS BETWEEN UNBOUNDED PRECEDING
                 AND UNBOUNDED FOLLOWING
    ) AS last_salary
FROM employees;
```

### NTH_VALUE()

```sql
SELECT
    employee_id,
    salary,
    NTH_VALUE(salary, 3) OVER (
        ORDER BY salary DESC
        ROWS BETWEEN UNBOUNDED PRECEDING
                 AND UNBOUNDED FOLLOWING
    ) AS third_highest
FROM employees;
```

---

# PARTITION BY

Equivalent to grouping for window calculations while keeping rows.

```sql
SELECT
    department_id,
    employee_id,
    salary,
    AVG(salary) OVER (
        PARTITION BY department_id
    ) AS dept_avg
FROM employees;
```

---

# Window Frames

### Current row and all previous rows

```sql
ROWS BETWEEN UNBOUNDED PRECEDING
         AND CURRENT ROW
```

Used for running totals.

```sql
SUM(amount) OVER (
    ORDER BY order_date
    ROWS BETWEEN UNBOUNDED PRECEDING
             AND CURRENT ROW
)
```

### Moving 3-row average

```sql
AVG(amount) OVER (
    ORDER BY order_date
    ROWS BETWEEN 2 PRECEDING
             AND CURRENT ROW
)
```

### Entire partition

```sql
ROWS BETWEEN UNBOUNDED PRECEDING
         AND UNBOUNDED FOLLOWING
```

---

# Common Interview Examples

### Top 3 salaries per department

```sql
WITH ranked AS (
    SELECT
        department_id,
        employee_id,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY department_id
            ORDER BY salary DESC
        ) AS rnk
    FROM employees
)
SELECT *
FROM ranked
WHERE rnk <= 3;
```

### Running total

```sql
SELECT
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date
    ) AS running_total
FROM orders;
```

### Difference from previous row

```sql
SELECT
    sale_date,
    amount,
    amount - LAG(amount) OVER (
        ORDER BY sale_date
    ) AS change_amount
FROM sales;
```

### Percent of department total

```sql
SELECT
    employee_id,
    department_id,
    salary,
    ROUND(
        salary * 100 /
        SUM(salary) OVER (
            PARTITION BY department_id
        ),
        2
    ) AS pct_of_dept
FROM employees;
```

---

# Quick Reference Table

| Function        | Purpose                 |
| --------------- | ----------------------- |
| `ROW_NUMBER()`  | Unique row numbering    |
| `RANK()`        | Ranking with gaps       |
| `DENSE_RANK()`  | Ranking without gaps    |
| `NTILE(n)`      | Split into buckets      |
| `LAG()`         | Previous row value      |
| `LEAD()`        | Next row value          |
| `FIRST_VALUE()` | First value in window   |
| `LAST_VALUE()`  | Last value in window    |
| `NTH_VALUE()`   | Nth value in window     |
| `SUM()`         | Running/partition total |
| `AVG()`         | Window average          |
| `COUNT()`       | Window count            |
| `MIN()`         | Window minimum          |
| `MAX()`         | Window maximum          |

### Remember

* `PARTITION BY` = divide rows into groups.
* `ORDER BY` = define row sequence within a partition.
* Frame clauses (`ROWS BETWEEN ...`) control which rows are visible to the function.
* `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()` are the most commonly used interview window functions.
* `LAG()` and `LEAD()` are ideal for time-series comparisons and change detection.
