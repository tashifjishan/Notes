Here's a single dataset that lets you practice nearly every MySQL window function:

* `ROW_NUMBER`
* `RANK`
* `DENSE_RANK`
* `NTILE`
* `PERCENT_RANK`
* `CUME_DIST`
* `SUM OVER`
* `AVG OVER`
* `COUNT OVER`
* `MIN/MAX OVER`
* `LAG`
* `LEAD`
* `FIRST_VALUE`
* `LAST_VALUE`
* `NTH_VALUE`
* `PARTITION BY`
* Running totals
* Moving averages
* Top-N per group
* Deduplication
* Sessionization
* Gaps & islands

---

# Table

```sql
CREATE TABLE employee_sales (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    employee_name VARCHAR(50),
    department VARCHAR(20),
    sale_date DATE,
    sale_amount INT
);
```

---

# Data

```sql
INSERT INTO employee_sales VALUES
(1, 101, 'Alice',   'Sales',   '2025-01-01', 1200),
(2, 102, 'Bob',     'Sales',   '2025-01-02', 1500),
(3, 103, 'Charlie', 'Sales',   '2025-01-03', 1500),
(4, 101, 'Alice',   'Sales',   '2025-01-04', 1800),

(5, 201, 'David',   'Tech',    '2025-01-01', 2000),
(6, 202, 'Emma',    'Tech',    '2025-01-02', 2200),
(7, 203, 'Frank',   'Tech',    '2025-01-03', 2200),
(8, 201, 'David',   'Tech',    '2025-01-04', 2500),

(9, 301, 'Grace',   'HR',      '2025-01-01', 1000),
(10,302, 'Helen',   'HR',      '2025-01-02', 1100),
(11,303, 'Ian',     'HR',      '2025-01-03', 1100),
(12,301, 'Grace',   'HR',      '2025-01-04', 1400),

(13,101, 'Alice',   'Sales',   '2025-01-06', 1600),
(14,102, 'Bob',     'Sales',   '2025-01-07', 1700),

(15,202, 'Emma',    'Tech',    '2025-01-06', 2600),
(16,203, 'Frank',   'Tech',    '2025-01-07', 2800),

(17,302, 'Helen',   'HR',      '2025-01-06', 1500),
(18,303, 'Ian',     'HR',      '2025-01-07', 1500);
```

---

# Practice Questions

## 1. ROW_NUMBER

Assign a row number within each department ordered by sale amount descending.

Expected concepts:

```sql
ROW_NUMBER()
PARTITION BY department
ORDER BY sale_amount DESC
```

---

## 2. RANK

Rank employees by sale amount within each department.

Notice ties:

```text
Sales:
1500
1500
```

---

## 3. DENSE_RANK

Same as above but without gaps.

Compare result with `RANK()`.

---

## 4. NTILE

Split all sales into 4 quartiles.

```sql
NTILE(4)
```

---

## 5. PERCENT_RANK

Calculate relative standing of each sale.

---

## 6. CUME_DIST

Calculate cumulative distribution.

---

## 7. Running Total

```sql
SUM(sale_amount)
OVER (
  ORDER BY sale_date
)
```

---

## 8. Department Running Total

```sql
SUM(sale_amount)
OVER (
  PARTITION BY department
  ORDER BY sale_date
)
```

---

## 9. Department Average

```sql
AVG(sale_amount)
OVER (
  PARTITION BY department
)
```

---

## 10. Department Max Sale

```sql
MAX(sale_amount)
OVER (
  PARTITION BY department
)
```

---

## 11. Previous Sale

```sql
LAG(sale_amount)
```

Find previous sale amount by employee.

---

## 12. Next Sale

```sql
LEAD(sale_amount)
```

Find next sale amount by employee.

---

## 13. Sale Difference

```sql
sale_amount -
LAG(sale_amount)
```

Find growth/decline between sales.

---

## 14. First Sale Value

```sql
FIRST_VALUE(sale_amount)
```

Show first sale for each employee.

---

## 15. Last Sale Value

Practice the frame issue:

```sql
LAST_VALUE(...)
```

Then fix it with:

```sql
ROWS BETWEEN
UNBOUNDED PRECEDING
AND UNBOUNDED FOLLOWING
```

---

## 16. Third Highest Sale

```sql
NTH_VALUE(sale_amount, 3)
```

---

## 17. Moving Average

3-row moving average:

```sql
AVG(sale_amount)
OVER (
  ORDER BY sale_date
  ROWS BETWEEN
    2 PRECEDING
    AND CURRENT ROW
)
```

---

## 18. Top 2 Sales Per Department

Use:

```sql
DENSE_RANK()
```

and filter rank <= 2.

---

## 19. Percentage of Department Total

For each row calculate:

```text
sale_amount / department_total
```

using window functions only.

---

## 20. Count Rows Per Department

```sql
COUNT(*)
OVER (
  PARTITION BY department
)
```

---

# Bonus Dataset for Deduplication

```sql
CREATE TABLE customer_updates (
    customer_id INT,
    customer_name VARCHAR(50),
    updated_at DATETIME
);
```

```sql
INSERT INTO customer_updates VALUES
(1,'John','2025-01-01 10:00:00'),
(1,'John','2025-01-02 11:00:00'),
(1,'John','2025-01-03 12:00:00'),
(2,'Mary','2025-01-01 09:00:00'),
(2,'Mary','2025-01-04 15:00:00'),
(3,'Steve','2025-01-02 08:00:00');
```

Exercise:

```sql
Keep only latest record per customer.
```

---

# Bonus Dataset for Sessionization

```sql
CREATE TABLE user_events (
    user_id INT,
    event_time DATETIME
);
```

```sql
INSERT INTO user_events VALUES
(1,'2025-01-01 10:00:00'),
(1,'2025-01-01 10:10:00'),
(1,'2025-01-01 10:20:00'),
(1,'2025-01-01 11:30:00'),
(1,'2025-01-01 11:35:00'),
(2,'2025-01-01 09:00:00'),
(2,'2025-01-01 09:15:00'),
(2,'2025-01-01 10:10:00');
```

Exercise:

Create a new session whenever the gap between events exceeds **30 minutes** using `LAG()`.

---

If you're preparing for SQL interviews, try solving all 20 questions without looking up syntax. Together they cover roughly 90% of the window-function patterns asked in data engineering, analytics, and backend SQL interviews.
