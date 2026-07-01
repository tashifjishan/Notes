# Module 7: Subqueries & CTEs in MySQL

These notes cover:

**Scalar Subqueries**
**Correlated Subqueries**
**Nested Queries**
**Common Table Expressions — CTEs**
**WITH Clause in MySQL**

MySQL treats a subquery as a query written inside another SQL statement. CTEs are similar in purpose, but they give a temporary name to a query result so the main query becomes cleaner and easier to read. MySQL documentation defines a CTE as a named temporary result set that exists only within the scope of a single statement. ([MySQL Developer Zone][1])

---

# 1. What is a Subquery?

A **subquery** is a query inside another query.

Basic structure:

```sql
SELECT column_name
FROM table_name
WHERE column_name operator (
    SELECT column_name
    FROM another_table
    WHERE condition
);
```

Example:

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

This query shows employees whose salary is greater than the average salary.

---

# 2. Why Use Subqueries?

Subqueries are useful when one query depends on the result of another query.

Common uses:

| Use Case                    | Example                                         |
| --------------------------- | ----------------------------------------------- |
| Filtering data              | Find employees earning more than average salary |
| Comparing values            | Find products costlier than category average    |
| Checking existence          | Find customers who placed orders                |
| Returning calculated values | Show salary plus company average salary         |
| Breaking complex logic      | Use one query result inside another             |

---

# 3. Sample Tables for Examples

We will use these example tables:

## employees

| employee_id | employee_name | department_id | salary | manager_id |
| ----------- | ------------- | ------------- | ------ | ---------- |
| 1           | Ali           | 10            | 50000  | 3          |
| 2           | Sara          | 10            | 60000  | 3          |
| 3           | Ahmed         | 20            | 90000  | NULL       |
| 4           | John          | 20            | 45000  | 3          |
| 5           | Maria         | 30            | 70000  | 3          |

## departments

| department_id | department_name |
| ------------- | --------------- |
| 10            | IT              |
| 20            | HR              |
| 30            | Sales           |

## customers

| customer_id | customer_name |
| ----------- | ------------- |
| 1           | Hamza         |
| 2           | Ayesha        |
| 3           | Bilal         |

## orders

| order_id | customer_id | total_amount |
| -------- | ----------- | ------------ |
| 101      | 1           | 5000         |
| 102      | 1           | 7000         |
| 103      | 2           | 3000         |

---

# 4. Types of Subqueries

Subqueries can be divided in different ways.

## A. By Output Type

| Type            | Meaning                               |
| --------------- | ------------------------------------- |
| Scalar subquery | Returns one row and one column        |
| Column subquery | Returns one column but many rows      |
| Row subquery    | Returns one row with multiple columns |
| Table subquery  | Returns multiple rows and columns     |

## B. By Dependency

| Type                    | Meaning                            |
| ----------------------- | ---------------------------------- |
| Non-correlated subquery | Inner query can run independently  |
| Correlated subquery     | Inner query depends on outer query |

---

# 5. Scalar Subqueries

A **scalar subquery** returns a single value: one row and one column. MySQL says a scalar subquery can be used almost anywhere a single column value or literal value is allowed. If the scalar subquery result is empty, the result becomes `NULL`. ([MySQL Developer Zone][2])

## Syntax

```sql
SELECT column_name
FROM table_name
WHERE column_name = (
    SELECT single_column
    FROM another_table
    WHERE condition
);
```

---

## Example 1: Employees Earning More Than Average Salary

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

Explanation:

```sql
SELECT AVG(salary)
FROM employees;
```

This inner query returns one value, for example `63000`.

Then the outer query becomes:

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > 63000;
```

Result:

| employee_name | salary |
| ------------- | ------ |
| Ahmed         | 90000  |
| Maria         | 70000  |

---

## Example 2: Scalar Subquery in SELECT Clause

```sql
SELECT 
    employee_name,
    salary,
    (SELECT AVG(salary) FROM employees) AS average_salary
FROM employees;
```

Output:

| employee_name | salary | average_salary |
| ------------- | ------ | -------------- |
| Ali           | 50000  | 63000          |
| Sara          | 60000  | 63000          |
| Ahmed         | 90000  | 63000          |

The scalar subquery returns the same average value for every row.

---

## Example 3: Scalar Subquery with MAX

```sql
SELECT employee_name, salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);
```

This finds the employee with the highest salary.

---

## Important Rule

A scalar subquery must return only **one value**.

Wrong example:

```sql
SELECT employee_name
FROM employees
WHERE salary = (
    SELECT salary
    FROM employees
);
```

This may return many salaries, so MySQL can throw an error like:

```sql
Subquery returns more than 1 row
```

To fix it, use `IN`, `ANY`, `ALL`, `MAX`, `MIN`, or `LIMIT` depending on the requirement.

Correct version using `IN`:

```sql
SELECT employee_name
FROM employees
WHERE salary IN (
    SELECT salary
    FROM employees
);
```

---

# 6. Non-Correlated Subqueries

A **non-correlated subquery** is independent. It can run by itself.

Example:

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

The inner query:

```sql
SELECT AVG(salary)
FROM employees;
```

does not depend on the outer query.

---

# 7. Correlated Subqueries

A **correlated subquery** depends on the outer query. It uses a column from the outer query inside the inner query. MySQL documentation explains that correlated subqueries can be optimized internally in some cases, but logically they are evaluated in relation to the outer query rows. ([MySQL Developer Zone][3])

## Basic Syntax

```sql
SELECT outer_column
FROM outer_table AS outer_alias
WHERE value operator (
    SELECT inner_column
    FROM inner_table AS inner_alias
    WHERE inner_alias.column = outer_alias.column
);
```

---

## Example 1: Employees Earning More Than Department Average

```sql
SELECT 
    e.employee_name,
    e.department_id,
    e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);
```

Explanation:

For each employee, MySQL compares the employee’s salary with the average salary of that employee’s own department.

Here:

```sql
e2.department_id = e.department_id
```

makes the subquery correlated because `e.department_id` comes from the outer query.

---

## Example 2: Customers Who Have Placed Orders

```sql
SELECT customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

Explanation:

For each customer, the subquery checks whether at least one matching order exists.

Result:

| customer_name |
| ------------- |
| Hamza         |
| Ayesha        |

Bilal is not shown because he has no order.

---

## Example 3: Customers Who Have Not Placed Orders

```sql
SELECT customer_name
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

Result:

| customer_name |
| ------------- |
| Bilal         |

---

## Correlated Subquery vs Non-Correlated Subquery

| Feature                    | Non-Correlated Subquery      | Correlated Subquery             |
| -------------------------- | ---------------------------- | ------------------------------- |
| Depends on outer query?    | No                           | Yes                             |
| Can run independently?     | Yes                          | No                              |
| Usually executes logically | Once                         | Per outer row                   |
| Example use                | Compare with company average | Compare with department average |
| Performance                | Often faster                 | Can be slower if not optimized  |

---

# 8. Nested Queries

A **nested query** means a query inside another query. Subqueries are also called nested queries.

Nested queries can be:

```sql
SELECT ...
FROM ...
WHERE column IN (
    SELECT ...
    FROM ...
    WHERE column IN (
        SELECT ...
        FROM ...
    )
);
```

---

## Example 1: Find Employees in Departments That Exist in Departments Table

```sql
SELECT employee_name
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
);
```

The inner query returns department IDs. The outer query returns employees whose department ID exists in that list.

---

## Example 2: Nested Query with Multiple Levels

```sql
SELECT employee_name
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE department_id IN (
        SELECT department_id
        FROM employees
        WHERE salary > 60000
    )
);
```

Explanation:

1. Innermost query finds departments where salary is greater than 60000.
2. Middle query checks those departments in the departments table.
3. Outer query returns employees from those departments.

---

# 9. Subquery Operators

## 1. `IN`

Used when the subquery returns multiple values.

```sql
SELECT employee_name
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
);
```

---

## 2. `NOT IN`

Used to exclude values.

```sql
SELECT customer_name
FROM customers
WHERE customer_id NOT IN (
    SELECT customer_id
    FROM orders
);
```

Important: Be careful with `NOT IN` if the subquery can return `NULL`. `NOT IN` with `NULL` can produce unexpected results. In many real projects, `NOT EXISTS` is safer.

Better version:

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

## 3. `EXISTS`

Checks whether the subquery returns at least one row.

```sql
SELECT customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

`EXISTS` is usually used with correlated subqueries.

---

## 4. `ANY` / `SOME`

`ANY` means comparison with at least one value returned by the subquery.

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > ANY (
    SELECT salary
    FROM employees
    WHERE department_id = 10
);
```

This means: salary is greater than at least one salary in department 10.

`SOME` is the same as `ANY`.

---

## 5. `ALL`

`ALL` means comparison with every value returned by the subquery.

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > ALL (
    SELECT salary
    FROM employees
    WHERE department_id = 10
);
```

This means: salary is greater than all salaries in department 10.

---

# 10. Subqueries in Different Clauses

## A. Subquery in WHERE Clause

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

Most common use.

---

## B. Subquery in SELECT Clause

```sql
SELECT 
    employee_name,
    salary,
    (SELECT MAX(salary) FROM employees) AS highest_salary
FROM employees;
```

Used to show calculated values beside each row.

---

## C. Subquery in FROM Clause

A subquery in the `FROM` clause is called a **derived table**.

```sql
SELECT department_id, avg_salary
FROM (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
) AS dept_avg
WHERE avg_salary > 55000;
```

Important: In MySQL, a subquery in the `FROM` clause must have an alias.

Here, the alias is:

```sql
AS dept_avg
```

---

## D. Subquery in HAVING Clause

```sql
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > (
    SELECT AVG(salary)
    FROM employees
);
```

This returns departments whose average salary is greater than the company average.

---

# 11. Common Table Expressions — CTEs

A **Common Table Expression**, or **CTE**, is a named temporary result set used inside a single SQL statement. It is written using the `WITH` clause. MySQL allows a `WITH` clause to contain one or more comma-separated CTE definitions. Each CTE definition contains a subquery and gives that subquery a name. ([MySQL Developer Zone][1])

## Basic Syntax

```sql
WITH cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
SELECT *
FROM cte_name;
```

---

## Example 1: Simple CTE

```sql
WITH high_salary_employees AS (
    SELECT employee_id, employee_name, salary
    FROM employees
    WHERE salary > 60000
)
SELECT *
FROM high_salary_employees;
```

Explanation:

First, the CTE creates a temporary result named `high_salary_employees`.

Then the main query uses it like a normal table.

---

## Same Query Without CTE

```sql
SELECT *
FROM (
    SELECT employee_id, employee_name, salary
    FROM employees
    WHERE salary > 60000
) AS high_salary_employees;
```

Both queries can produce the same result, but the CTE version is easier to read.

---

# 12. WITH Clause in MySQL

The `WITH` clause is used to define CTEs. MySQL syntax supports both non-recursive and recursive CTEs using this general form: `WITH [RECURSIVE] cte_name [(column_names)] AS (subquery)`. The parentheses around the CTE subquery are required. ([MySQL Developer Zone][1])

## General Syntax

```sql
WITH cte_name AS (
    SELECT ...
)
SELECT ...
FROM cte_name;
```

## Multiple CTEs

```sql
WITH 
dept_avg AS (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
),
high_paid AS (
    SELECT employee_id, employee_name, department_id, salary
    FROM employees
    WHERE salary > 60000
)
SELECT 
    h.employee_name,
    h.salary,
    d.avg_salary
FROM high_paid h
JOIN dept_avg d
ON h.department_id = d.department_id;
```

MySQL permits only one `WITH` clause at the same query level, so multiple CTEs should be separated by commas inside the same `WITH` clause. CTE names must also be unique within the same `WITH` clause. ([MySQL Developer Zone][1])

---

# 13. CTE with Column Names

You can define column names after the CTE name.

```sql
WITH salary_summary (dept_id, avg_salary) AS (
    SELECT department_id, AVG(salary)
    FROM employees
    GROUP BY department_id
)
SELECT *
FROM salary_summary;
```

Here:

```sql
salary_summary (dept_id, avg_salary)
```

renames the output columns of the CTE.

---

# 14. CTE Referencing Another CTE

A CTE can reference another CTE defined earlier in the same `WITH` clause. MySQL documentation notes that a CTE can refer to earlier CTEs, but not later ones at the same level. ([MySQL Developer Zone][1])

Correct:

```sql
WITH 
dept_avg AS (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
),
above_avg AS (
    SELECT e.employee_name, e.salary, d.avg_salary
    FROM employees e
    JOIN dept_avg d
    ON e.department_id = d.department_id
    WHERE e.salary > d.avg_salary
)
SELECT *
FROM above_avg;
```

Wrong:

```sql
WITH 
above_avg AS (
    SELECT *
    FROM dept_avg
),
dept_avg AS (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT *
FROM above_avg;
```

This is wrong because `above_avg` tries to use `dept_avg` before it is defined.

---

# 15. Recursive CTEs

A **recursive CTE** is a CTE that refers to itself. MySQL uses `WITH RECURSIVE` for recursive CTEs. Recursive CTEs are commonly used for number series and hierarchical or tree-structured data. ([MySQL Developer Zone][1])

## Example: Generate Numbers 1 to 5

```sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS n

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 5
)
SELECT *
FROM numbers;
```

Result:

| n |
| - |
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |

---

## Recursive CTE Structure

A recursive CTE has two parts:

```sql
WITH RECURSIVE cte_name AS (
    -- Anchor query
    SELECT initial_value

    UNION ALL

    -- Recursive query
    SELECT next_value
    FROM cte_name
    WHERE stopping_condition
)
SELECT *
FROM cte_name;
```

| Part               | Meaning                               |
| ------------------ | ------------------------------------- |
| Anchor query       | Starting point                        |
| Recursive query    | Repeats using previous result         |
| Stopping condition | Prevents infinite recursion           |
| `UNION ALL`        | Combines anchor and recursive results |

---

# 16. Example: Employee Manager Hierarchy

Suppose `employees` table has:

| employee_id | employee_name | manager_id |
| ----------- | ------------- | ---------- |
| 1           | CEO           | NULL       |
| 2           | Manager A     | 1          |
| 3           | Manager B     | 1          |
| 4           | Staff A       | 2          |
| 5           | Staff B       | 2          |

Query:

```sql
WITH RECURSIVE employee_tree AS (
    SELECT 
        employee_id,
        employee_name,
        manager_id,
        1 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT 
        e.employee_id,
        e.employee_name,
        e.manager_id,
        et.level + 1
    FROM employees e
    JOIN employee_tree et
    ON e.manager_id = et.employee_id
)
SELECT *
FROM employee_tree;
```

This shows the hierarchy from CEO to staff.

---

# 17. CTE vs Subquery

| Feature           | Subquery                                      | CTE                                  |
| ----------------- | --------------------------------------------- | ------------------------------------ |
| Readability       | Can become difficult in complex queries       | Easier to read                       |
| Reusability       | Usually used once                             | Can be referenced multiple times     |
| Naming            | No meaningful name unless derived table alias | Has a clear name                     |
| Debugging         | Harder                                        | Easier                               |
| Recursive support | No direct recursive structure                 | Supports recursive CTEs              |
| Best for          | Simple filtering/calculation                  | Complex reports and multi-step logic |

---

# 18. CTE vs Temporary Table

| Feature                     | CTE                          | Temporary Table                      |
| --------------------------- | ---------------------------- | ------------------------------------ |
| Lifetime                    | One statement only           | Session-based                        |
| Stored physically?          | Usually handled by optimizer | Stored as temporary table            |
| Reusable across statements? | No                           | Yes                                  |
| Requires CREATE?            | No                           | Yes                                  |
| Best for                    | Query readability            | Reusing intermediate data many times |

---

# 19. CTE vs View

| Feature             | CTE                    | View                          |
| ------------------- | ---------------------- | ----------------------------- |
| Lifetime            | One statement          | Permanent database object     |
| Stored in database  | No                     | Yes                           |
| Requires permission | No CREATE VIEW needed  | Needs view creation privilege |
| Best for            | One-time complex query | Reusable database logic       |

---

# 20. Performance Notes

Subqueries, CTEs, and joins can often solve the same problem. The best choice depends on readability, indexes, data size, and the optimizer plan. MySQL documentation notes that subqueries, derived tables, views, and CTEs are subject to optimizer strategies such as merging or materialization. ([MySQL Developer Zone][4])

## Best Practices

Use indexes on columns used in:

```sql
WHERE
JOIN
IN
EXISTS
GROUP BY
ORDER BY
```

For example:

```sql
CREATE INDEX idx_employees_department_id
ON employees(department_id);

CREATE INDEX idx_orders_customer_id
ON orders(customer_id);
```

Use `EXISTS` when checking whether related records exist:

```sql
SELECT customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

Use CTEs when the query has many steps:

```sql
WITH step1 AS (...),
step2 AS (...),
step3 AS (...)
SELECT ...
FROM step3;
```

---

# 21. Common MySQL Restrictions and Mistakes

## Mistake 1: Scalar Subquery Returning Multiple Rows

Wrong:

```sql
SELECT employee_name
FROM employees
WHERE salary = (
    SELECT salary
    FROM employees
);
```

Correct:

```sql
SELECT employee_name
FROM employees
WHERE salary IN (
    SELECT salary
    FROM employees
);
```

---

## Mistake 2: Missing Alias for Derived Table

Wrong:

```sql
SELECT *
FROM (
    SELECT department_id, AVG(salary)
    FROM employees
    GROUP BY department_id
);
```

Correct:

```sql
SELECT *
FROM (
    SELECT department_id, AVG(salary)
    FROM employees
    GROUP BY department_id
) AS dept_avg;
```

---

## Mistake 3: Using Same Table in UPDATE Subquery

MySQL has restrictions when modifying a table and selecting from the same table in a subquery. The documentation says that, in general, you cannot modify a table and select from the same table in a subquery, although there are derived-table materialization exceptions. ([MySQL Developer Zone][5])

Problem example:

```sql
UPDATE employees
SET salary = salary + 1000
WHERE salary < (
    SELECT AVG(salary)
    FROM employees
);
```

Safer derived-table version:

```sql
UPDATE employees
SET salary = salary + 1000
WHERE salary < (
    SELECT avg_salary
    FROM (
        SELECT AVG(salary) AS avg_salary
        FROM employees
    ) AS temp_avg
);
```

---

## Mistake 4: Forgetting `RECURSIVE`

Wrong:

```sql
WITH numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM numbers WHERE n < 5
)
SELECT * FROM numbers;
```

Correct:

```sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM numbers WHERE n < 5
)
SELECT * FROM numbers;
```

The `RECURSIVE` keyword is required when a CTE refers to itself. ([MySQL Developer Zone][1])

---

# 22. When to Use What?

## Use Scalar Subquery When:

You need one value.

Example:

```sql
WHERE salary > (SELECT AVG(salary) FROM employees)
```

---

## Use `IN` Subquery When:

You need to match against multiple values.

```sql
WHERE department_id IN (
    SELECT department_id
    FROM departments
)
```

---

## Use `EXISTS` When:

You only need to check whether matching rows exist.

```sql
WHERE EXISTS (
    SELECT 1
    FROM orders
    WHERE orders.customer_id = customers.customer_id
)
```

---

## Use CTE When:

Your query has multiple logical steps.

```sql
WITH sales_summary AS (...),
top_customers AS (...)
SELECT ...
FROM top_customers;
```

---

## Use Recursive CTE When:

You need hierarchy, tree, chain, or sequence.

```sql
WITH RECURSIVE ...
```

---

# 23. Real-World Example: Sales Report Using CTE

Goal: Find customers whose total order amount is greater than average customer spending.

```sql
WITH customer_totals AS (
    SELECT 
        c.customer_id,
        c.customer_name,
        SUM(o.total_amount) AS total_spent
    FROM customers c
    JOIN orders o
    ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.customer_name
),
average_spending AS (
    SELECT AVG(total_spent) AS avg_spent
    FROM customer_totals
)
SELECT 
    ct.customer_name,
    ct.total_spent,
    av.avg_spent
FROM customer_totals ct
CROSS JOIN average_spending av
WHERE ct.total_spent > av.avg_spent;
```

Explanation:

1. `customer_totals` calculates total spending per customer.
2. `average_spending` calculates average customer spending.
3. Final query returns customers above average.

---

# 24. Same Problem Using Subquery

```sql
SELECT 
    c.customer_name,
    SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(o.total_amount) > (
    SELECT AVG(customer_total)
    FROM (
        SELECT SUM(total_amount) AS customer_total
        FROM orders
        GROUP BY customer_id
    ) AS totals
);
```

This works, but it is harder to read than the CTE version.

---

# 25. Quick Revision Table

| Concept             | Meaning                                      | Example Keyword                       |
| ------------------- | -------------------------------------------- | ------------------------------------- |
| Subquery            | Query inside another query                   | `SELECT ... WHERE ... (SELECT ...)`   |
| Scalar subquery     | Returns one value                            | `= (SELECT AVG(...))`                 |
| Correlated subquery | Depends on outer query                       | `WHERE o.customer_id = c.customer_id` |
| Nested query        | Query inside query, possibly multiple levels | `IN (SELECT ... IN (SELECT ...))`     |
| CTE                 | Named temporary result set                   | `WITH cte AS (...)`                   |
| Recursive CTE       | CTE that refers to itself                    | `WITH RECURSIVE`                      |
| EXISTS              | Checks if rows exist                         | `WHERE EXISTS (...)`                  |
| IN                  | Matches list of values                       | `WHERE id IN (...)`                   |
| ALL                 | Compare with all values                      | `> ALL (...)`                         |
| ANY                 | Compare with any value                       | `> ANY (...)`                         |

---

# 26. Interview Questions

## Q1. What is a subquery?

A subquery is a query written inside another SQL query. It is used when the result of one query is needed by another query.

---

## Q2. What is a scalar subquery?

A scalar subquery returns exactly one value: one row and one column.

Example:

```sql
SELECT employee_name
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

---

## Q3. What is a correlated subquery?

A correlated subquery is a subquery that uses a value from the outer query.

Example:

```sql
SELECT employee_name
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);
```

---

## Q4. Difference between subquery and correlated subquery?

A normal subquery can run independently. A correlated subquery cannot run independently because it depends on the outer query.

---

## Q5. What is a CTE?

A CTE is a named temporary result set created using the `WITH` clause and used within a single SQL statement.

---

## Q6. Difference between CTE and subquery?

A CTE is usually more readable and reusable within the same statement. A subquery is written directly inside another query and can become difficult to manage in complex queries.

---

## Q7. What is a recursive CTE?

A recursive CTE is a CTE that refers to itself. It is used for hierarchical data, tree structures, and generating sequences.

---

# 27. Practice Exercises

## Exercise 1

Find employees whose salary is greater than the average salary.

```sql
SELECT employee_name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

---

## Exercise 2

Find employees who earn more than the average salary of their own department.

```sql
SELECT employee_name, department_id, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);
```

---

## Exercise 3

Find customers who have placed at least one order.

```sql
SELECT customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

---

## Exercise 4

Use a CTE to find departments with average salary above 55000.

```sql
WITH dept_avg AS (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
)
SELECT *
FROM dept_avg
WHERE avg_salary > 55000;
```

---

## Exercise 5

Generate numbers from 1 to 10 using recursive CTE.

```sql
WITH RECURSIVE numbers AS (
    SELECT 1 AS n

    UNION ALL

    SELECT n + 1
    FROM numbers
    WHERE n < 10
)
SELECT *
FROM numbers;
```

---

# 28. Final Summary

A **scalar subquery** returns one value. A **correlated subquery** depends on the outer query. A **nested query** is a query inside another query. A **CTE** is a named temporary result set created using the `WITH` clause. In MySQL, CTEs make complex queries easier to read, especially when a query has multiple steps or recursive logic.

[1]: https://dev.mysql.com/doc/refman/8.0/en/with.html "MySQL :: MySQL 8.0 Reference Manual :: 15.2.20 WITH (Common Table Expressions)"
[2]: https://dev.mysql.com/doc/refman/8.4/en/scalar-subqueries.html "MySQL :: MySQL 8.4 Reference Manual :: 15.2.15.1 The Subquery as Scalar Operand"
[3]: https://dev.mysql.com/doc/refman/8.4/en/correlated-subqueries.html "MySQL :: MySQL 8.4 Reference Manual :: 15.2.15.7 Correlated Subqueries"
[4]: https://dev.mysql.com/doc/refman/8.1/en/dynindex-statement.html?utm_source=chatgpt.com "MySQL 8.4 Reference Manual :: Statement/Syntax Index"
[5]: https://dev.mysql.com/doc/refman/8.4/en/subquery-restrictions.html "MySQL :: MySQL 8.4 Reference Manual :: 15.2.15.12 Restrictions on Subqueries"
