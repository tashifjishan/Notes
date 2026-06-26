
## Distribution Functions

### PERCENT_RANK()

Returns the relative rank from 0 to 1.

```sql
SELECT
    employee_id,
    salary,
    PERCENT_RANK() OVER (
        ORDER BY salary
    ) AS pct_rank
FROM employees;
```

Formula:

```text
(rank - 1) / (total_rows - 1)
```

---

### CUME_DIST()

Returns the cumulative distribution.

```sql
SELECT
    employee_id,
    salary,
    CUME_DIST() OVER (
        ORDER BY salary
    ) AS cume_dist
FROM employees;
```

Example:

| Salary | CUME_DIST |
| ------ | --------- |
| 100    | 0.25      |
| 200    | 0.50      |
| 300    | 0.75      |
| 400    | 1.00      |

Useful for percentiles.

---

## Named Windows

Avoid repeating the same window specification.

```sql
SELECT
    employee_id,
    salary,
    AVG(salary) OVER w AS avg_sal,
    MAX(salary) OVER w AS max_sal
FROM employees
WINDOW w AS (
    PARTITION BY department_id
);
```

---

## Multiple Window Definitions

```sql
SELECT
    employee_id,
    salary,
    AVG(salary) OVER dept_win,
    RANK() OVER rank_win
FROM employees
WINDOW
    dept_win AS (
        PARTITION BY department_id
    ),
    rank_win AS (
        ORDER BY salary DESC
    );
```

---

## RANGE vs ROWS

Most examples use `ROWS`.

### ROWS

Physical row count.

```sql
ROWS BETWEEN 2 PRECEDING
         AND CURRENT ROW
```

Exactly 2 rows back.

### RANGE

Logical value range based on ORDER BY.

```sql
RANGE BETWEEN UNBOUNDED PRECEDING
          AND CURRENT ROW
```

Rows with equal ordering values are treated together.

Example:

```text
salary
------
100
100
200
```

With `RANGE`, both `100` rows belong to the same frame.

---

## Window Functions in Common Patterns

### Deduplication

Keep latest row per key.

```sql
WITH ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY customer_id
               ORDER BY updated_at DESC
           ) AS rn
    FROM customers
)
SELECT *
FROM ranked
WHERE rn = 1;
```

---

### Gaps and Islands

Detect breaks in sequences.

```sql
SELECT
    id,
    order_date,
    ROW_NUMBER() OVER (
        ORDER BY order_date
    ) AS rn
FROM orders;
```

Often combined with date arithmetic to identify contiguous ranges.

---

### Sessionization

Group events into sessions using `LAG()`.

```sql
SELECT
    user_id,
    event_time,
    CASE
        WHEN TIMESTAMPDIFF(
            MINUTE,
            LAG(event_time) OVER (
                PARTITION BY user_id
                ORDER BY event_time
            ),
            event_time
        ) > 30
        THEN 1
        ELSE 0
    END AS new_session
FROM events;
```

---

## Important Restrictions

Window functions:

❌ Cannot be used in:

```sql
WHERE
GROUP BY
HAVING
```

This fails:

```sql
SELECT *
FROM employees
WHERE ROW_NUMBER() OVER (...) = 1;
```

Use a derived table or CTE:

```sql
WITH ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (...) AS rn
    FROM employees
)
SELECT *
FROM ranked
WHERE rn = 1;
```

---

## Execution Order Reminder

Conceptually:

```text
FROM
WHERE
GROUP BY
HAVING
WINDOW FUNCTIONS
SELECT
ORDER BY
LIMIT
```

That's why window functions aren't available in `WHERE`.

---

## Complete MySQL Window Function Set

Ranking:

```text
ROW_NUMBER()
RANK()
DENSE_RANK()
NTILE()
```

Distribution:

```text
PERCENT_RANK()
CUME_DIST()
```

Value:

```text
LAG()
LEAD()
FIRST_VALUE()
LAST_VALUE()
NTH_VALUE()
```

Aggregate window functions:

```text
SUM()
AVG()
COUNT()
MIN()
MAX()
```

And most aggregate functions can operate as window functions when used with `OVER()`:

```sql
SUM(x) OVER (...)
AVG(x) OVER (...)
COUNT(x) OVER (...)
```

## One subtle MySQL gotcha

`LAST_VALUE()` surprises many people:

```sql
LAST_VALUE(salary) OVER (
    ORDER BY salary
)
```

does **not** usually return the last salary in the partition. By default, it returns the last value in the **current frame**, which often ends at the current row.

To get the actual last value in the partition:

```sql
LAST_VALUE(salary) OVER (
    ORDER BY salary
    ROWS BETWEEN UNBOUNDED PRECEDING
             AND UNBOUNDED FOLLOWING
)
```

This is probably the most common window-function bug seen in MySQL code reviews.
