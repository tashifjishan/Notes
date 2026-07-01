# Module 10: Data Cleaning in MySQL

These notes are written using a **Reddit-style dataset** as the example, meaning raw posts/comments data with usernames, titles, comments, scores, dates, subreddits, URLs, and duplicate rows.

MySQL provides built-in functions such as `COALESCE()`, `CAST()`, `CONVERT()`, `LOWER()`, `UPPER()`, `TRIM()`, `REPLACE()`, `REGEXP_REPLACE()`, and `DATE_FORMAT()` for cleaning and formatting data. `COALESCE()` returns the first non-`NULL` argument, while `CAST()` and `CONVERT()` are used to change data types. MySQL documentation also lists string functions such as `LOWER()`, `TRIM()`, `REPLACE()`, and `REGEXP_REPLACE()` for standardizing messy text values. ([MySQL][1])

---

## 1. What Is Data Cleaning in SQL?

**Data cleaning** means finding and fixing incorrect, incomplete, duplicate, inconsistent, or badly formatted data.

In real databases, raw data may contain:

| Problem           | Example                                                    |
| ----------------- | ---------------------------------------------------------- |
| Missing values    | `NULL`, empty string `''`, `'N/A'`, `'unknown'`            |
| Wrong data type   | Score stored as `'120 points'` instead of `120`            |
| Duplicate rows    | Same Reddit comment inserted twice                         |
| Extra spaces      | `'  AskReddit  '`                                          |
| Inconsistent case | `'AskReddit'`, `'askreddit'`, `'ASKREDDIT'`                |
| Invalid values    | Negative age, invalid email, impossible date               |
| Bad formatting    | Phone numbers, dates, URLs, usernames in different formats |

### Basic data-cleaning workflow

```sql
-- 1. Inspect data
SELECT * FROM reddit_posts_raw LIMIT 20;

-- 2. Find problems
SELECT COUNT(*) FROM reddit_posts_raw WHERE title IS NULL;

-- 3. Clean using SELECT first
SELECT TRIM(LOWER(subreddit)) AS clean_subreddit
FROM reddit_posts_raw;

-- 4. Update only after checking
UPDATE reddit_posts_raw
SET subreddit = TRIM(LOWER(subreddit));
```

**Rule:** First test cleaning logic with `SELECT`. Then apply it with `UPDATE`.

---

# Example Table for This Module

Assume we have this raw Reddit-style table:

```sql
CREATE TABLE reddit_posts_raw (
    id INT PRIMARY KEY AUTO_INCREMENT,
    post_id VARCHAR(50),
    username VARCHAR(100),
    subreddit VARCHAR(100),
    title VARCHAR(255),
    body TEXT,
    score VARCHAR(50),
    comment_count VARCHAR(50),
    created_at VARCHAR(100),
    url VARCHAR(255),
    flair VARCHAR(100)
);
```

Sample dirty data:

```sql
INSERT INTO reddit_posts_raw
(post_id, username, subreddit, title, body, score, comment_count, created_at, url, flair)
VALUES
('p001', ' JohnDoe ', ' AskReddit ', 'Best SQL tips?', NULL, '120', '45', '2026-06-20', 'https://reddit.com/r/AskReddit/p001', NULL),
('p002', NULL, 'mysql', '  How to remove duplicates? ', 'Need help', '80 points', '12 comments', '20/06/2026', 'reddit.com/r/mysql/p002', 'Question'),
('p002', NULL, 'mysql', '  How to remove duplicates? ', 'Need help', '80 points', '12 comments', '20/06/2026', 'reddit.com/r/mysql/p002', 'Question'),
('p003', 'unknown', 'SQL', '', 'Nice post', NULL, '0', 'invalid-date', NULL, '');
```

---

# 2. Handling NULL Values

## What is `NULL`?

`NULL` means **missing, unknown, or not available**.

It is different from:

```sql
''
0
'NULL'
'N/A'
'unknown'
```

Example:

```sql
SELECT *
FROM reddit_posts_raw
WHERE username IS NULL;
```

Do **not** write:

```sql
WHERE username = NULL;
```

That is incorrect because `NULL` is not compared using `=`.

Correct:

```sql
WHERE username IS NULL;
WHERE username IS NOT NULL;
```

---

## Find NULL values

```sql
SELECT COUNT(*) AS missing_usernames
FROM reddit_posts_raw
WHERE username IS NULL;
```

Find missing title, body, flair:

```sql
SELECT
    SUM(username IS NULL) AS null_usernames,
    SUM(title IS NULL) AS null_titles,
    SUM(body IS NULL) AS null_bodies,
    SUM(flair IS NULL) AS null_flairs
FROM reddit_posts_raw;
```

In MySQL, Boolean conditions like `username IS NULL` return `1` for true and `0` for false, so they can be summed.

---

## Convert empty strings to NULL

Sometimes missing data is stored as an empty string:

```sql
title = ''
flair = ''
```

Clean it:

```sql
UPDATE reddit_posts_raw
SET title = NULL
WHERE TRIM(title) = '';
```

For flair:

```sql
UPDATE reddit_posts_raw
SET flair = NULL
WHERE TRIM(flair) = '';
```

---

## Convert fake missing values to NULL

Common fake missing values:

```text
'N/A'
'NA'
'none'
'unknown'
'-'
'null'
```

Example:

```sql
UPDATE reddit_posts_raw
SET username = NULL
WHERE LOWER(TRIM(username)) IN ('unknown', 'n/a', 'na', 'none', '-', 'null');
```

---

# 3. `COALESCE()` in MySQL

## Meaning

`COALESCE()` returns the **first non-NULL value** from a list. MySQL’s built-in function reference describes `COALESCE()` as returning the first non-`NULL` argument. ([MySQL][1])

### Syntax

```sql
COALESCE(value1, value2, value3, ...)
```

### Example

```sql
SELECT COALESCE(NULL, NULL, 'No flair') AS result;
```

Output:

```text
No flair
```

---

## Use `COALESCE()` to replace NULL while displaying data

```sql
SELECT
    post_id,
    COALESCE(username, 'Anonymous') AS username,
    COALESCE(flair, 'No Flair') AS flair
FROM reddit_posts_raw;
```

This does not change the table. It only changes the output.

---

## Use `COALESCE()` in reports

```sql
SELECT
    subreddit,
    COUNT(*) AS total_posts,
    COALESCE(flair, 'No Flair') AS flair_group
FROM reddit_posts_raw
GROUP BY subreddit, COALESCE(flair, 'No Flair');
```

---

## Use `COALESCE()` with multiple fallback columns

Suppose a user can have `username`, `display_name`, or `user_id`.

```sql
SELECT
    COALESCE(username, display_name, user_id, 'Anonymous') AS user_identity
FROM users;
```

Meaning:

1. Use `username` if available.
2. Otherwise use `display_name`.
3. Otherwise use `user_id`.
4. Otherwise show `'Anonymous'`.

---

## `COALESCE()` vs `IFNULL()`

| Function               | Meaning                                      |
| ---------------------- | -------------------------------------------- |
| `IFNULL(a, b)`         | If `a` is NULL, return `b`                   |
| `COALESCE(a, b, c, d)` | Return first non-NULL value from many values |

Example:

```sql
SELECT IFNULL(flair, 'No Flair') AS clean_flair
FROM reddit_posts_raw;
```

Same idea with `COALESCE()`:

```sql
SELECT COALESCE(flair, 'No Flair') AS clean_flair
FROM reddit_posts_raw;
```

`COALESCE()` is more flexible because it can accept many values.

---

# 4. `CAST()` and `CONVERT()`

## Why type conversion is needed

Raw data often stores numbers and dates as text.

Examples:

```text
score = '80 points'
comment_count = '12 comments'
created_at = '20/06/2026'
```

For analysis, these should be converted into proper numeric or date types.

MySQL documentation says `CAST(expr AS type)` takes an expression and produces a value of the specified type. It also states that `CONVERT(expr, type)` is equivalent for type conversion, while `CONVERT(expr USING charset)` is used for character-set conversion. ([MySQL][2])

---

## `CAST()` syntax

```sql
CAST(expression AS datatype)
```

Examples:

```sql
SELECT CAST('120' AS UNSIGNED) AS score_number;
```

```sql
SELECT CAST('99.50' AS DECIMAL(10,2)) AS price_value;
```

```sql
SELECT CAST('2026-06-20' AS DATE) AS clean_date;
```

---

## `CONVERT()` syntax

```sql
CONVERT(expression, datatype)
```

Example:

```sql
SELECT CONVERT('120', UNSIGNED) AS score_number;
```

For character set conversion:

```sql
SELECT CONVERT('test' USING utf8mb4);
```

---

## Common MySQL conversion types

| Type            | Use                         |
| --------------- | --------------------------- |
| `SIGNED`        | Convert to signed integer   |
| `UNSIGNED`      | Convert to positive integer |
| `DECIMAL(10,2)` | Convert to decimal number   |
| `DATE`          | Convert to date             |
| `DATETIME`      | Convert to date and time    |
| `CHAR`          | Convert to string           |
| `TIME`          | Convert to time             |

---

## Clean numeric values before casting

Example dirty values:

```text
'80 points'
'12 comments'
'1,250'
```

Clean and convert:

```sql
SELECT
    score,
    CAST(REPLACE(score, ' points', '') AS UNSIGNED) AS clean_score
FROM reddit_posts_raw;
```

For comment count:

```sql
SELECT
    comment_count,
    CAST(REPLACE(comment_count, ' comments', '') AS UNSIGNED) AS clean_comment_count
FROM reddit_posts_raw;
```

For comma numbers:

```sql
SELECT CAST(REPLACE('1,250', ',', '') AS UNSIGNED) AS clean_number;
```

---

## Safer conversion using validation

Before casting, check that the value is numeric:

```sql
SELECT *
FROM reddit_posts_raw
WHERE score REGEXP '^[0-9]+$';
```

For dirty values like `'80 points'`, clean first:

```sql
SELECT
    score,
    CASE
        WHEN REPLACE(score, ' points', '') REGEXP '^[0-9]+$'
        THEN CAST(REPLACE(score, ' points', '') AS UNSIGNED)
        ELSE NULL
    END AS clean_score
FROM reddit_posts_raw;
```

This prevents wrong conversions.

---

# 5. Removing Duplicates

## What are duplicates?

Duplicates can be of two types:

### 1. Exact duplicates

Every column has the same value.

### 2. Business duplicates

Rows are not exactly the same, but they represent the same real-world item.

Example:

```text
Same post_id = same Reddit post
Same url = same Reddit link
Same username + title + created_at = likely duplicate
```

---

## Find duplicates by one column

```sql
SELECT post_id, COUNT(*) AS total
FROM reddit_posts_raw
GROUP BY post_id
HAVING COUNT(*) > 1;
```

---

## Find duplicates by multiple columns

```sql
SELECT
    post_id,
    username,
    title,
    COUNT(*) AS total
FROM reddit_posts_raw
GROUP BY post_id, username, title
HAVING COUNT(*) > 1;
```

---

## View duplicate rows

```sql
SELECT *
FROM reddit_posts_raw
WHERE post_id IN (
    SELECT post_id
    FROM reddit_posts_raw
    GROUP BY post_id
    HAVING COUNT(*) > 1
);
```

---

## Remove duplicates using self-join

This keeps the row with the smallest `id` and deletes later duplicates.

```sql
DELETE p1
FROM reddit_posts_raw p1
JOIN reddit_posts_raw p2
  ON p1.post_id = p2.post_id
 AND p1.id > p2.id;
```

Meaning:

* `p1` is the duplicate row.
* `p2` is the original row.
* `p1.id > p2.id` keeps the oldest row.

---

## Remove duplicates using `ROW_NUMBER()` in MySQL 8+

`ROW_NUMBER()` gives each row a number within a group. MySQL documentation states that `ROW_NUMBER()` returns the number of the current row within its partition, and that `ORDER BY` affects the order of numbering. ([MySQL][3])

```sql
WITH ranked_posts AS (
    SELECT
        id,
        post_id,
        ROW_NUMBER() OVER (
            PARTITION BY post_id
            ORDER BY id
        ) AS rn
    FROM reddit_posts_raw
)
DELETE FROM reddit_posts_raw
WHERE id IN (
    SELECT id
    FROM ranked_posts
    WHERE rn > 1
);
```

Meaning:

* `PARTITION BY post_id` groups duplicate posts.
* `ORDER BY id` keeps the first inserted row.
* `rn > 1` means duplicate rows.

---

## Prevent duplicates after cleaning

After removing duplicates, add a unique constraint:

```sql
ALTER TABLE reddit_posts_raw
ADD CONSTRAINT unique_post_id UNIQUE (post_id);
```

Now MySQL will not allow duplicate `post_id`.

---

# 6. Data Validation

## What is data validation?

**Data validation** means checking whether data follows correct rules.

Examples:

| Column          | Validation rule                           |
| --------------- | ----------------------------------------- |
| `score`         | Must be numeric                           |
| `comment_count` | Must be numeric                           |
| `created_at`    | Must be a valid date                      |
| `subreddit`     | Cannot be NULL                            |
| `url`           | Should start with `http://` or `https://` |
| `flair`         | Should belong to allowed categories       |
| `username`      | Should not contain only spaces            |

---

## Validate NULL values

```sql
SELECT *
FROM reddit_posts_raw
WHERE subreddit IS NULL
   OR title IS NULL
   OR created_at IS NULL;
```

---

## Validate empty strings

```sql
SELECT *
FROM reddit_posts_raw
WHERE TRIM(title) = '';
```

---

## Validate numeric values

```sql
SELECT *
FROM reddit_posts_raw
WHERE score NOT REGEXP '^[0-9]+$';
```

For values like `'80 points'`, validate after cleaning:

```sql
SELECT *
FROM reddit_posts_raw
WHERE REPLACE(score, ' points', '') NOT REGEXP '^[0-9]+$';
```

---

## Validate date format

For ISO date format:

```sql
SELECT *
FROM reddit_posts_raw
WHERE created_at NOT REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$';
```

This finds dates not written like:

```text
2026-06-20
```

---

## Validate URL format

```sql
SELECT *
FROM reddit_posts_raw
WHERE url IS NOT NULL
  AND url NOT REGEXP '^https?://';
```

Clean missing protocol:

```sql
UPDATE reddit_posts_raw
SET url = CONCAT('https://', url)
WHERE url IS NOT NULL
  AND url NOT REGEXP '^https?://';
```

---

## Validate category values

Suppose allowed flairs are:

```text
Question
Discussion
Help
News
Tutorial
No Flair
```

Find invalid flairs:

```sql
SELECT DISTINCT flair
FROM reddit_posts_raw
WHERE flair NOT IN ('Question', 'Discussion', 'Help', 'News', 'Tutorial', 'No Flair')
  AND flair IS NOT NULL;
```

---

## Validate score range

```sql
SELECT *
FROM reddit_posts_raw
WHERE CAST(score AS SIGNED) < 0;
```

For safer validation:

```sql
SELECT *
FROM reddit_posts_raw
WHERE score REGEXP '^[0-9]+$'
  AND CAST(score AS UNSIGNED) > 1000000;
```

---

# 7. Data Formatting

Data formatting means making values look consistent.

Common formatting tasks:

| Task              | Function                   |
| ----------------- | -------------------------- |
| Remove spaces     | `TRIM()`                   |
| Lowercase text    | `LOWER()`                  |
| Uppercase text    | `UPPER()`                  |
| Replace text      | `REPLACE()`                |
| Regex replacement | `REGEXP_REPLACE()`         |
| Format date       | `DATE_FORMAT()`            |
| Combine text      | `CONCAT()` / `CONCAT_WS()` |

MySQL documentation describes `TRIM()` as removing prefixes/suffixes, with spaces removed by default when no removal string is specified. It also describes `LOWER()` as converting a string to lowercase according to character-set mapping, and `REPLACE()` as replacing all occurrences of one string with another. ([MySQL][4])

---

## Remove extra spaces

```sql
SELECT
    username,
    TRIM(username) AS clean_username
FROM reddit_posts_raw;
```

Update:

```sql
UPDATE reddit_posts_raw
SET username = TRIM(username);
```

---

## Standardize case

For subreddit names:

```sql
UPDATE reddit_posts_raw
SET subreddit = LOWER(TRIM(subreddit));
```

Example:

```text
' AskReddit ' → 'askreddit'
'MYSQL' → 'mysql'
'SQL ' → 'sql'
```

---

## Format usernames

Remove spaces and make lowercase:

```sql
UPDATE reddit_posts_raw
SET username = LOWER(TRIM(username))
WHERE username IS NOT NULL;
```

---

## Clean post titles

Remove extra leading/trailing spaces:

```sql
UPDATE reddit_posts_raw
SET title = TRIM(title);
```

Remove repeated spaces inside title:

```sql
UPDATE reddit_posts_raw
SET title = REGEXP_REPLACE(title, '[ ]+', ' ');
```

Example:

```text
'How   to   learn   MySQL?' → 'How to learn MySQL?'
```

`REGEXP_REPLACE()` is useful when the pattern is not a fixed word but a repeated or flexible pattern. MySQL’s string-function list includes `REGEXP_REPLACE()` for replacing substrings that match a regular expression. ([MySQL][4])

---

## Clean Reddit URLs

Some URLs may be stored like:

```text
reddit.com/r/mysql/p002
```

Convert them to:

```text
https://reddit.com/r/mysql/p002
```

```sql
UPDATE reddit_posts_raw
SET url = CONCAT('https://', url)
WHERE url IS NOT NULL
  AND url NOT LIKE 'http://%'
  AND url NOT LIKE 'https://%';
```

---

## Format dates

If date is already stored as a real `DATE` column:

```sql
SELECT DATE_FORMAT(created_at, '%d-%m-%Y') AS formatted_date
FROM reddit_posts_clean;
```

MySQL lists `DATE_FORMAT()` as the function used to format dates. ([MySQL][1])

Common date formats:

| Format            | Output                    |
| ----------------- | ------------------------- |
| `'%Y-%m-%d'`      | `2026-06-20`              |
| `'%d-%m-%Y'`      | `20-06-2026`              |
| `'%M %d, %Y'`     | `June 20, 2026`           |
| `'%W, %M %d, %Y'` | `Saturday, June 20, 2026` |

---

## Convert text date to real date

For text date like:

```text
20/06/2026
```

Use:

```sql
SELECT STR_TO_DATE(created_at, '%d/%m/%Y') AS clean_date
FROM reddit_posts_raw;
```

For text date like:

```text
2026-06-20
```

Use:

```sql
SELECT CAST(created_at AS DATE) AS clean_date
FROM reddit_posts_raw;
```

---

# 8. Creating a Clean Table

A good professional method is to keep the raw table unchanged and create a cleaned table.

```sql
CREATE TABLE reddit_posts_clean AS
SELECT
    id,
    post_id,

    COALESCE(NULLIF(LOWER(TRIM(username)), ''), 'anonymous') AS username,

    LOWER(TRIM(subreddit)) AS subreddit,

    NULLIF(TRIM(title), '') AS title,

    COALESCE(NULLIF(TRIM(body), ''), 'No body text') AS body,

    CASE
        WHEN REPLACE(score, ' points', '') REGEXP '^[0-9]+$'
        THEN CAST(REPLACE(score, ' points', '') AS UNSIGNED)
        ELSE NULL
    END AS score,

    CASE
        WHEN REPLACE(comment_count, ' comments', '') REGEXP '^[0-9]+$'
        THEN CAST(REPLACE(comment_count, ' comments', '') AS UNSIGNED)
        ELSE NULL
    END AS comment_count,

    CASE
        WHEN created_at REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
        THEN CAST(created_at AS DATE)
        WHEN created_at REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$'
        THEN STR_TO_DATE(created_at, '%d/%m/%Y')
        ELSE NULL
    END AS created_at,

    CASE
        WHEN url IS NULL OR TRIM(url) = '' THEN NULL
        WHEN url LIKE 'http://%' OR url LIKE 'https://%' THEN TRIM(url)
        ELSE CONCAT('https://', TRIM(url))
    END AS url,

    COALESCE(NULLIF(TRIM(flair), ''), 'No Flair') AS flair

FROM reddit_posts_raw;
```

This query cleans:

* usernames
* subreddit names
* empty titles
* missing body text
* score values
* comment count values
* dates
* URLs
* flair values

---

# 9. Complete Cleaning Checklist

## Step 1: Profile the data

```sql
SELECT COUNT(*) AS total_rows
FROM reddit_posts_raw;
```

```sql
SELECT *
FROM reddit_posts_raw
LIMIT 20;
```

---

## Step 2: Check missing values

```sql
SELECT
    SUM(username IS NULL OR TRIM(username) = '') AS missing_username,
    SUM(subreddit IS NULL OR TRIM(subreddit) = '') AS missing_subreddit,
    SUM(title IS NULL OR TRIM(title) = '') AS missing_title,
    SUM(score IS NULL OR TRIM(score) = '') AS missing_score
FROM reddit_posts_raw;
```

---

## Step 3: Check duplicates

```sql
SELECT post_id, COUNT(*) AS total
FROM reddit_posts_raw
GROUP BY post_id
HAVING COUNT(*) > 1;
```

---

## Step 4: Check invalid numeric values

```sql
SELECT score
FROM reddit_posts_raw
WHERE REPLACE(score, ' points', '') NOT REGEXP '^[0-9]+$'
  AND score IS NOT NULL;
```

---

## Step 5: Check invalid dates

```sql
SELECT created_at
FROM reddit_posts_raw
WHERE created_at IS NOT NULL
  AND created_at NOT REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
  AND created_at NOT REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$';
```

---

## Step 6: Check inconsistent categories

```sql
SELECT DISTINCT subreddit
FROM reddit_posts_raw
ORDER BY subreddit;
```

Clean:

```sql
UPDATE reddit_posts_raw
SET subreddit = LOWER(TRIM(subreddit));
```

---

# 10. Common Mistakes in SQL Data Cleaning

## Mistake 1: Comparing NULL with `=`

Wrong:

```sql
WHERE username = NULL;
```

Correct:

```sql
WHERE username IS NULL;
```

---

## Mistake 2: Updating without checking first

Wrong:

```sql
UPDATE reddit_posts_raw
SET score = CAST(score AS UNSIGNED);
```

Better:

```sql
SELECT score, CAST(score AS UNSIGNED)
FROM reddit_posts_raw;
```

Then update only after checking.

---

## Mistake 3: Deleting duplicates without backup

Before deleting:

```sql
CREATE TABLE reddit_posts_backup AS
SELECT *
FROM reddit_posts_raw;
```

Then delete duplicates.

---

## Mistake 4: Treating empty string as NULL

These are different:

```sql
NULL
''
' '
```

Clean them:

```sql
UPDATE reddit_posts_raw
SET title = NULL
WHERE title IS NULL OR TRIM(title) = '';
```

---

## Mistake 5: Using `CONCAT()` with NULL

In MySQL, `CONCAT()` returns `NULL` if any argument is `NULL`, so use `COALESCE()` when needed. ([MySQL][4])

Problem:

```sql
SELECT CONCAT(username, ' posted in ', subreddit)
FROM reddit_posts_raw;
```

If `username` is `NULL`, the whole result becomes `NULL`.

Better:

```sql
SELECT CONCAT(
    COALESCE(username, 'Anonymous'),
    ' posted in ',
    COALESCE(subreddit, 'unknown subreddit')
) AS activity
FROM reddit_posts_raw;
```

---

# 11. Important MySQL Functions Summary

| Function           | Purpose                            | Example                               |
| ------------------ | ---------------------------------- | ------------------------------------- |
| `IS NULL`          | Find missing values                | `WHERE username IS NULL`              |
| `IS NOT NULL`      | Find available values              | `WHERE score IS NOT NULL`             |
| `COALESCE()`       | Replace NULL with fallback         | `COALESCE(flair, 'No Flair')`         |
| `NULLIF()`         | Convert a value to NULL if matched | `NULLIF(TRIM(title), '')`             |
| `CAST()`           | Convert data type                  | `CAST(score AS UNSIGNED)`             |
| `CONVERT()`        | Convert type or character set      | `CONVERT(score, UNSIGNED)`            |
| `TRIM()`           | Remove spaces                      | `TRIM(username)`                      |
| `LOWER()`          | Convert to lowercase               | `LOWER(subreddit)`                    |
| `UPPER()`          | Convert to uppercase               | `UPPER(country_code)`                 |
| `REPLACE()`        | Replace fixed text                 | `REPLACE(score, ' points', '')`       |
| `REGEXP_REPLACE()` | Replace pattern-based text         | `REGEXP_REPLACE(title, '[ ]+', ' ')`  |
| `STR_TO_DATE()`    | Convert string to date             | `STR_TO_DATE(created_at, '%d/%m/%Y')` |
| `DATE_FORMAT()`    | Format date output                 | `DATE_FORMAT(created_at, '%d-%m-%Y')` |
| `ROW_NUMBER()`     | Rank duplicate rows                | `ROW_NUMBER() OVER (...)`             |

---

# 12. Assignment-Ready Explanation

**Data cleaning in SQL** is the process of improving raw data quality by handling missing values, correcting data types, removing duplicate records, validating incorrect entries, and formatting values consistently. In MySQL, missing values are handled using `IS NULL`, `IS NOT NULL`, `COALESCE()`, and `NULLIF()`. Data types can be corrected using `CAST()` and `CONVERT()`, for example converting text scores into numeric values or text dates into proper date values. Duplicate records can be identified using `GROUP BY` with `HAVING COUNT(*) > 1`, and removed using self-joins or `ROW_NUMBER()` in MySQL 8+. Data validation is done using conditions, ranges, `REGEXP`, and allowed-value checks. Formatting is performed using functions such as `TRIM()`, `LOWER()`, `UPPER()`, `REPLACE()`, `REGEXP_REPLACE()`, and `DATE_FORMAT()`.

For example, in a Reddit dataset, raw values such as `' AskReddit '`, `'80 points'`, `'12 comments'`, empty titles, missing usernames, and duplicate post IDs can be cleaned using SQL functions. The final goal is to create accurate, consistent, analysis-ready data.

---

# 13. Practice Questions

## Q1. Find all posts where username is missing.

```sql
SELECT *
FROM reddit_posts_raw
WHERE username IS NULL OR TRIM(username) = '';
```

## Q2. Replace missing usernames with `'anonymous'`.

```sql
SELECT COALESCE(NULLIF(TRIM(username), ''), 'anonymous') AS clean_username
FROM reddit_posts_raw;
```

## Q3. Convert score from text to number.

```sql
SELECT
    score,
    CAST(REPLACE(score, ' points', '') AS UNSIGNED) AS clean_score
FROM reddit_posts_raw;
```

## Q4. Find duplicate Reddit posts.

```sql
SELECT post_id, COUNT(*) AS total
FROM reddit_posts_raw
GROUP BY post_id
HAVING COUNT(*) > 1;
```

## Q5. Remove duplicate posts and keep the first row.

```sql
DELETE p1
FROM reddit_posts_raw p1
JOIN reddit_posts_raw p2
  ON p1.post_id = p2.post_id
 AND p1.id > p2.id;
```

## Q6. Clean subreddit names.

```sql
UPDATE reddit_posts_raw
SET subreddit = LOWER(TRIM(subreddit));
```

## Q7. Validate URLs.

```sql
SELECT *
FROM reddit_posts_raw
WHERE url IS NOT NULL
  AND url NOT REGEXP '^https?://';
```

## Q8. Format dates as `DD-MM-YYYY`.

```sql
SELECT DATE_FORMAT(created_at, '%d-%m-%Y') AS formatted_date
FROM reddit_posts_clean;
```

---

# 14. Mini Project: Clean Reddit Data

### Task

Clean a raw Reddit dataset and create a final clean table.

### Requirements

Your final table should have:

| Column          | Cleaned rule                                          |
| --------------- | ----------------------------------------------------- |
| `post_id`       | Not duplicate                                         |
| `username`      | Lowercase, trimmed, missing replaced with `anonymous` |
| `subreddit`     | Lowercase and trimmed                                 |
| `title`         | Trimmed, empty title converted to NULL                |
| `body`          | Missing body replaced with `No body text`             |
| `score`         | Converted to number                                   |
| `comment_count` | Converted to number                                   |
| `created_at`    | Converted to `DATE`                                   |
| `url`           | Starts with `https://`                                |
| `flair`         | Missing replaced with `No Flair`                      |

### Final query

```sql
CREATE TABLE reddit_posts_final AS
WITH cleaned AS (
    SELECT
        id,
        post_id,
        COALESCE(NULLIF(LOWER(TRIM(username)), ''), 'anonymous') AS username,
        LOWER(TRIM(subreddit)) AS subreddit,
        NULLIF(TRIM(title), '') AS title,
        COALESCE(NULLIF(TRIM(body), ''), 'No body text') AS body,

        CASE
            WHEN REPLACE(score, ' points', '') REGEXP '^[0-9]+$'
            THEN CAST(REPLACE(score, ' points', '') AS UNSIGNED)
            ELSE NULL
        END AS score,

        CASE
            WHEN REPLACE(comment_count, ' comments', '') REGEXP '^[0-9]+$'
            THEN CAST(REPLACE(comment_count, ' comments', '') AS UNSIGNED)
            ELSE NULL
        END AS comment_count,

        CASE
            WHEN created_at REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
            THEN CAST(created_at AS DATE)
            WHEN created_at REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$'
            THEN STR_TO_DATE(created_at, '%d/%m/%Y')
            ELSE NULL
        END AS created_at,

        CASE
            WHEN url IS NULL OR TRIM(url) = '' THEN NULL
            WHEN url LIKE 'http://%' OR url LIKE 'https://%' THEN TRIM(url)
            ELSE CONCAT('https://', TRIM(url))
        END AS url,

        COALESCE(NULLIF(TRIM(flair), ''), 'No Flair') AS flair,

        ROW_NUMBER() OVER (
            PARTITION BY post_id
            ORDER BY id
        ) AS rn
    FROM reddit_posts_raw
)
SELECT
    post_id,
    username,
    subreddit,
    title,
    body,
    score,
    comment_count,
    created_at,
    url,
    flair
FROM cleaned
WHERE rn = 1;
```

This final query performs **NULL handling, type conversion, duplicate removal, validation, and formatting** in one cleaning pipeline.

[1]: https://dev.mysql.com/doc/refman/8.0/en/built-in-function-reference.html "MySQL :: MySQL 8.0 Reference Manual :: 14.1 Built-In Function and Operator Reference"
[2]: https://dev.mysql.com/doc/en/cast-functions.html "MySQL :: MySQL 9.7 Reference Manual :: 14.10 Cast Functions and Operators"
[3]: https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html "MySQL :: MySQL 8.0 Reference Manual :: 14.20.1 Window Function Descriptions"
[4]: https://dev.mysql.com/doc/en/string-functions.html "MySQL :: MySQL 9.7 Reference Manual :: 14.8 String Functions and Operators"
