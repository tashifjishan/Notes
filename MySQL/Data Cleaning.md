# MySQL Data Cleaning Cheat Sheet

## 1. What Data Cleaning Means

Data cleaning is the process of finding, fixing, standardizing, or separating messy data so it becomes reliable for analysis, reporting, dashboards, machine learning, or business decisions.

The goal is not always to “delete bad data.” A professional cleaning process usually separates data into:

1. **Clean records**
   Rows that are valid and ready to use.

2. **Rejected records**
   Rows that have serious issues and need review.

3. **Flagged records**
   Rows that are usable but suspicious.

4. **Original raw data**
   The untouched source table, kept for audit and backup.

A good rule:

```text
Never destroy raw data.
Profile first.
Clean second.
Validate third.
Document everything.
```

---

# 2. Basic Data Cleaning Workflow

## Step 1: Understand the Dataset

Before cleaning, inspect the structure.

```sql
DESCRIBE table_name;
```

Check sample rows:

```sql
SELECT *
FROM table_name
LIMIT 20;
```

Check row count:

```sql
SELECT COUNT(*) AS total_rows
FROM table_name;
```

Check columns and datatypes:

```sql
SHOW COLUMNS FROM table_name;
```

---

## Step 2: Profile Each Column

Profiling means understanding what values exist before deciding what to clean.

### Check distinct values

```sql
SELECT DISTINCT column_name
FROM table_name
ORDER BY column_name;
```

### Check value frequency

```sql
SELECT
    column_name,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY column_name
ORDER BY total_rows DESC;
```

### Check normalized frequency

Useful for messy text values with different casing or spaces.

```sql
SELECT
    LOWER(TRIM(column_name)) AS normalized_value,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(column_name))
ORDER BY total_rows DESC;
```

---

## Step 3: Detect Missing or Suspicious Values

Missing values are not always `NULL`. They can also appear as text placeholders.

Common missing-like values:

```text
NULL
''
' '
'N/A'
'NA'
'na'
'n/a'
'none'
'null'
'unknown'
'not available'
'not provided'
'-'
'--'
'?'
'0'
'0000'
'test'
'dummy'
```

Check missing values:

```sql
SELECT *
FROM table_name
WHERE column_name IS NULL
   OR TRIM(column_name) = '';
```

Check common placeholders:

```sql
SELECT *
FROM table_name
WHERE LOWER(TRIM(column_name)) IN (
    'n/a',
    'na',
    'none',
    'null',
    'unknown',
    'not available',
    'not provided',
    '-',
    '--',
    '?',
    'test',
    'dummy'
);
```

Better approach for large datasets:

```sql
SELECT
    LOWER(TRIM(column_name)) AS value_found,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(column_name))
ORDER BY total_rows DESC;
```

This helps you discover unknown bad values instead of guessing them in advance.

---

# 3. Core MySQL Cleaning Functions

## Remove Spaces

```sql
TRIM(column_name)
LTRIM(column_name)
RTRIM(column_name)
```

Example:

```sql
SELECT TRIM(customer_name) AS clean_name
FROM customers;
```

---

## Change Case

```sql
LOWER(column_name)
UPPER(column_name)
```

Example:

```sql
SELECT LOWER(TRIM(email)) AS clean_email
FROM customers;
```

Most-used pattern:

```sql
LOWER(TRIM(column_name))
```

---

## Replace Text

```sql
REPLACE(column_name, 'old_value', 'new_value')
```

Example:

```sql
SELECT REPLACE(phone, '-', '') AS clean_phone
FROM customers;
```

Multiple replacements:

```sql
SELECT
    REPLACE(
        REPLACE(
            REPLACE(column_name, '$', ''),
        ',', ''),
    'USD', '') AS cleaned_value
FROM table_name;
```

---

## Remove Characters Using Regex

MySQL 8+ supports `REGEXP_REPLACE`.

Remove all non-numeric characters:

```sql
REGEXP_REPLACE(column_name, '[^0-9]', '')
```

Remove everything except numbers and decimal point:

```sql
REGEXP_REPLACE(column_name, '[^0-9.]', '')
```

Example:

```sql
SELECT
    REGEXP_REPLACE(phone, '[^0-9]', '') AS clean_phone
FROM customers;
```

---

## Convert Blank to NULL

```sql
NULLIF(TRIM(column_name), '')
```

Example:

```sql
SELECT NULLIF(TRIM(customer_name), '') AS clean_customer_name
FROM customers;
```

---

## Replace NULL With Default Value

```sql
COALESCE(column_name, 'Unknown')
```

Example:

```sql
SELECT COALESCE(city, 'Unknown') AS city
FROM customers;
```

Be careful: do not blindly replace missing values with fake values unless it makes business sense.

---

## Convert Datatype

```sql
CAST(column_name AS datatype)
```

Examples:

```sql
CAST(quantity AS UNSIGNED)
CAST(price AS DECIMAL(10,2))
CAST(order_date AS DATE)
```

---

## Conditional Cleaning

```sql
CASE
    WHEN condition THEN clean_value
    WHEN condition THEN clean_value
    ELSE original_value
END
```

Example:

```sql
SELECT
    CASE
        WHEN LOWER(TRIM(status)) IN ('completed', 'complete', 'delivered') THEN 'Completed'
        WHEN LOWER(TRIM(status)) IN ('cancelled', 'canceled') THEN 'Cancelled'
        WHEN LOWER(TRIM(status)) IN ('pending', 'in progress') THEN 'Pending'
        ELSE 'Other'
    END AS clean_status
FROM orders;
```

---

# 4. General Column-Type Cleaning Guide

This is one of the most important sections.

Different datatype columns have different types of problems. You should not clean every column in the same way.

---

# 5. Text / String Columns

Examples:

```text
customer_name
product_name
city
country
company_name
address
department
job_title
```

## What Text Columns May Contain

Text columns may contain:

```text
Extra spaces
Mixed casing
Typos
Abbreviations
Special characters
Duplicate names with different spelling
Placeholder values
Numbers inside text
Symbols
Encoding issues
Multiple values in one field
```

Examples:

```text
' Ali Khan '
'ali khan'
'ALI KHAN'
'Ali  Khan'
'Ali-Khan'
'N/A'
'Unknown'
'Test User'
'Customer123'
```

---

## What to Look For in Text Columns

### 1. Leading and trailing spaces

```sql
SELECT *
FROM table_name
WHERE column_name <> TRIM(column_name);
```

### 2. Blank values

```sql
SELECT *
FROM table_name
WHERE column_name IS NULL
   OR TRIM(column_name) = '';
```

### 3. Placeholder values

```sql
SELECT
    LOWER(TRIM(column_name)) AS value_found,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(column_name))
ORDER BY total_rows DESC;
```

### 4. Very short text

```sql
SELECT *
FROM table_name
WHERE CHAR_LENGTH(TRIM(column_name)) <= 2;
```

### 5. Text with numbers

Useful for names, cities, countries, categories.

```sql
SELECT *
FROM table_name
WHERE column_name REGEXP '[0-9]';
```

### 6. Text with no letters

```sql
SELECT *
FROM table_name
WHERE column_name NOT REGEXP '[A-Za-z]';
```

### 7. Multiple spaces inside text

```sql
SELECT *
FROM table_name
WHERE column_name REGEXP ' {2,}';
```

---

## Best Practices for Text Columns

1. Use `TRIM()` on most text fields.
2. Use `LOWER(TRIM())` for matching.
3. Do not permanently lowercase names if display formatting matters.
4. Use mapping tables for standard categories.
5. Do not guess typos blindly.
6. Keep original value and cleaned value when possible.
7. Flag suspicious values instead of deleting them immediately.

---

# 6. Name Columns

Examples:

```text
customer_name
employee_name
student_name
supplier_name
```

## What Names May Contain

```text
Extra spaces
Mixed case
Initials
Titles
Numbers
Fake values
Single-character names
Repeated dummy names
Special characters
```

Examples:

```text
' Mr. Ali Khan '
'ali khan'
'ALI'
'A'
'Unknown'
'Test'
'Customer 1'
'12345'
```

---

## What to Look For

### Missing names

```sql
SELECT *
FROM table_name
WHERE name IS NULL
   OR TRIM(name) = '';
```

### Placeholder names

```sql
SELECT *
FROM table_name
WHERE LOWER(TRIM(name)) IN (
    'unknown',
    'n/a',
    'na',
    'none',
    'null',
    'test',
    'dummy',
    'customer'
);
```

### Very short names

```sql
SELECT *
FROM table_name
WHERE CHAR_LENGTH(TRIM(name)) <= 2;
```

### Names with numbers

```sql
SELECT *
FROM table_name
WHERE name REGEXP '[0-9]';
```

### Most repeated names

```sql
SELECT
    LOWER(TRIM(name)) AS normalized_name,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(name))
ORDER BY total_rows DESC;
```

---

## Best Practices for Name Columns

1. Do not delete short names automatically. Some real names are short.
2. Do not force every name into title case if your SQL cannot handle it properly.
3. Remove leading and trailing spaces.
4. Keep original name for audit.
5. Use quality flags such as `Missing`, `Too Short`, `Contains Number`, `Placeholder`, `Looks Valid`.

Example:

```sql
SELECT
    name,
    CASE
        WHEN name IS NULL THEN 'Missing'
        WHEN TRIM(name) = '' THEN 'Blank'
        WHEN LOWER(TRIM(name)) IN ('unknown', 'n/a', 'na', 'test', 'dummy') THEN 'Placeholder'
        WHEN CHAR_LENGTH(TRIM(name)) <= 2 THEN 'Too Short'
        WHEN name REGEXP '[0-9]' THEN 'Contains Number'
        ELSE 'Looks Valid'
    END AS name_quality_status
FROM table_name;
```

---

# 7. Email Columns

Examples:

```text
email
customer_email
user_email
contact_email
```

## What Email Columns May Contain

```text
Uppercase letters
Extra spaces
Invalid format
Missing @
Missing domain
Placeholder emails
Multiple emails in one field
Fake emails
Trailing punctuation
```

Examples:

```text
' Ali@GMAIL.COM '
'john@gmail'
'noemail.com'
'test@test.com'
'unknown'
'abc@'
'abc@@gmail.com'
```

---

## What to Look For

### Normalize email

```sql
LOWER(TRIM(email))
```

### Missing email

```sql
SELECT *
FROM table_name
WHERE email IS NULL
   OR TRIM(email) = '';
```

### Basic invalid email

```sql
SELECT *
FROM table_name
WHERE email NOT LIKE '%@%.%';
```

### Better invalid email check

```sql
SELECT *
FROM table_name
WHERE email IS NULL
   OR LOWER(TRIM(email)) NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$';
```

### Duplicate emails

```sql
SELECT
    LOWER(TRIM(email)) AS clean_email,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(email))
HAVING COUNT(*) > 1;
```

---

## Best Practices for Email Columns

1. Always lowercase emails.
2. Always trim emails.
3. Use email as a possible duplicate key, but do not assume it is always unique.
4. Watch out for shared company emails.
5. Watch out for fake emails like `test@test.com`.
6. Do not use only `LIKE '%@%'` for serious validation.
7. Store invalid emails in a rejected or flagged table.

---

# 8. Phone Number Columns

Examples:

```text
phone
mobile
contact_number
whatsapp_number
```

## What Phone Columns May Contain

```text
Spaces
Dashes
Country codes
Brackets
Text
Extensions
Missing values
Fake numbers
Different formats
```

Examples:

```text
'0300-1234567'
'+92 300 1234567'
'(555) 222-1111'
'not available'
'0000000000'
'12345'
```

---

## What to Look For

### Remove all non-numeric characters

```sql
SELECT
    REGEXP_REPLACE(phone, '[^0-9]', '') AS clean_phone
FROM table_name;
```

### Missing phone

```sql
SELECT *
FROM table_name
WHERE phone IS NULL
   OR TRIM(phone) = '';
```

### Phone contains letters

```sql
SELECT *
FROM table_name
WHERE phone REGEXP '[A-Za-z]';
```

### Phone too short or too long

```sql
SELECT *
FROM table_name
WHERE CHAR_LENGTH(REGEXP_REPLACE(phone, '[^0-9]', '')) < 7
   OR CHAR_LENGTH(REGEXP_REPLACE(phone, '[^0-9]', '')) > 15;
```

### Fake repeated numbers

```sql
SELECT *
FROM table_name
WHERE REGEXP_REPLACE(phone, '[^0-9]', '') REGEXP '^(0+|1+|9+)$';
```

---

## Best Practices for Phone Columns

1. Keep phone numbers as text, not numeric.
2. Do not remove leading zeroes accidentally.
3. Store cleaned phone separately.
4. Keep country code if available.
5. Validate length according to country rules.
6. Do not assume all phone numbers follow one country’s format.
7. Use phone as a weak duplicate indicator, not a perfect key.

---

# 9. Numeric Columns

Examples:

```text
quantity
age
score
rating
stock
number_of_items
years_experience
```

## What Numeric Columns May Contain

```text
Text values
Negative values
Zero values
Decimals in integer fields
Commas
Currency symbols
Units
Outliers
Impossible values
Missing values
```

Examples:

```text
'10'
'1,000'
'two'
'-5'
'0'
'99 years'
'10 pcs'
'N/A'
```

---

## What to Look For

### Non-numeric values

For integers:

```sql
SELECT *
FROM table_name
WHERE column_name NOT REGEXP '^-?[0-9]+$';
```

For decimals:

```sql
SELECT *
FROM table_name
WHERE column_name NOT REGEXP '^-?[0-9]+(\\.[0-9]+)?$';
```

### Negative values

```sql
SELECT *
FROM table_name
WHERE CAST(column_name AS SIGNED) < 0;
```

### Zero values

```sql
SELECT *
FROM table_name
WHERE CAST(column_name AS DECIMAL(10,2)) = 0;
```

### Very high outliers

```sql
SELECT *
FROM table_name
WHERE CAST(column_name AS DECIMAL(10,2)) > 100000;
```

### Summary statistics

```sql
SELECT
    COUNT(*) AS total_rows,
    MIN(CAST(column_name AS DECIMAL(10,2))) AS min_value,
    MAX(CAST(column_name AS DECIMAL(10,2))) AS max_value,
    AVG(CAST(column_name AS DECIMAL(10,2))) AS avg_value
FROM table_name
WHERE column_name REGEXP '^-?[0-9]+(\\.[0-9]+)?$';
```

---

## Best Practices for Numeric Columns

1. Understand whether zero is valid or not.
2. Understand whether negative values are valid or not.
3. Validate numeric ranges using business logic.
4. Do not cast dirty text directly without checking.
5. Remove commas and units before casting.
6. Keep rejected rows where conversion fails.
7. Use `DECIMAL` for money, not `FLOAT`.

---

# 10. Currency / Price Columns

Examples:

```text
price
unit_price
total_amount
sales
revenue
cost
discount
tax
```

## What Currency Columns May Contain

```text
Currency symbols
Commas
Currency codes
Text
Negative values
Multiple currencies
Blank values
Decimal issues
```

Examples:

```text
'$12.50'
'12.50 USD'
'2,500 PKR'
'60 dollars'
'€99.99'
'free'
'N/A'
```

---

## What to Look For

### Remove currency symbols and text

```sql
SELECT
    price,
    CAST(REGEXP_REPLACE(price, '[^0-9.]', '') AS DECIMAL(10,2)) AS clean_price
FROM table_name;
```

### Detect multiple currencies

```sql
SELECT *
FROM table_name
WHERE price REGEXP 'USD|PKR|EUR|GBP|INR|\\$|€|£';
```

### Detect non-convertible price

```sql
SELECT *
FROM table_name
WHERE REGEXP_REPLACE(price, '[^0-9.]', '') = '';
```

### Detect negative price

```sql
SELECT *
FROM table_name
WHERE CAST(REGEXP_REPLACE(price, '[^0-9.-]', '') AS DECIMAL(10,2)) < 0;
```

---

## Best Practices for Currency Columns

1. Store amount and currency in separate columns.
2. Do not mix currencies in one column.
3. Use `DECIMAL(10,2)` or a suitable precision.
4. Do not use `FLOAT` for financial values.
5. Decide whether negative values mean refund, discount, or error.
6. Keep original price string if source data is messy.
7. Convert currencies only using a clear exchange-rate rule and date.

---

# 11. Date Columns

Examples:

```text
order_date
created_at
birth_date
payment_date
joining_date
delivery_date
```

## What Date Columns May Contain

```text
Different date formats
Invalid dates
Blank dates
Text month names
Datetime mixed with date
Wrong timezone
Future dates
Old impossible dates
Ambiguous day/month order
```

Examples:

```text
'2026-01-15'
'15/01/2026'
'01/15/2026'
'2026/01/15'
'Jan 15 2026'
'15 Jan 2026'
'2026-13-01'
'0000-00-00'
''
```

---

## What to Look For

### Missing dates

```sql
SELECT *
FROM table_name
WHERE date_column IS NULL
   OR TRIM(date_column) = '';
```

### Invalid zero dates

```sql
SELECT *
FROM table_name
WHERE date_column = '0000-00-00';
```

### Convert known format

```sql
SELECT STR_TO_DATE(date_column, '%d/%m/%Y') AS clean_date
FROM table_name;
```

### Handle multiple date formats

```sql
SELECT
    date_column,
    CASE
        WHEN date_column REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
            THEN STR_TO_DATE(date_column, '%Y-%m-%d')

        WHEN date_column REGEXP '^[0-9]{2}/[0-9]{2}/[0-9]{4}$'
            THEN STR_TO_DATE(date_column, '%d/%m/%Y')

        WHEN date_column REGEXP '^[0-9]{4}/[0-9]{2}/[0-9]{2}$'
            THEN STR_TO_DATE(date_column, '%Y/%m/%d')

        WHEN date_column REGEXP '^[A-Za-z]{3} [0-9]{2} [0-9]{4}$'
            THEN STR_TO_DATE(date_column, '%b %d %Y')

        WHEN date_column REGEXP '^[0-9]{2} [A-Za-z]{3} [0-9]{4}$'
            THEN STR_TO_DATE(date_column, '%d %b %Y')

        ELSE NULL
    END AS clean_date
FROM table_name;
```

### Future dates

```sql
SELECT *
FROM table_name
WHERE clean_date > CURDATE();
```

### Too old dates

```sql
SELECT *
FROM table_name
WHERE clean_date < '1900-01-01';
```

---

## Best Practices for Date Columns

1. Store dates as `DATE`, not text.
2. Store timestamps as `DATETIME` or `TIMESTAMP`.
3. Standard format should be `YYYY-MM-DD`.
4. Be careful with `DD/MM/YYYY` versus `MM/DD/YYYY`.
5. Never assume ambiguous dates without source context.
6. Check future dates where they should not exist.
7. Check impossible old dates.
8. Keep timezone rules clear for timestamp data.
9. Do not mix date-only and datetime values in one column.

---

# 12. Boolean Columns

Examples:

```text
is_active
is_deleted
has_paid
email_verified
subscribed
```

## What Boolean Columns May Contain

```text
1
0
Y
N
Yes
No
True
False
T
F
Active
Inactive
Paid
Unpaid
Blank
```

---

## What to Look For

### Value frequency

```sql
SELECT
    LOWER(TRIM(boolean_column)) AS value_found,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(boolean_column))
ORDER BY total_rows DESC;
```

### Standardize boolean values

```sql
SELECT
    CASE
        WHEN LOWER(TRIM(boolean_column)) IN ('1', 'y', 'yes', 'true', 't', 'active', 'paid') THEN 1
        WHEN LOWER(TRIM(boolean_column)) IN ('0', 'n', 'no', 'false', 'f', 'inactive', 'unpaid') THEN 0
        ELSE NULL
    END AS clean_boolean
FROM table_name;
```

---

## Best Practices for Boolean Columns

1. Use `TINYINT(1)` or a controlled allowed-value system.
2. Standardize to `1` and `0`.
3. Do not assume blank means false.
4. Treat unknown separately from false.
5. Document meaning clearly.

Important distinction:

```text
NULL  = unknown
0     = false
1     = true
```

---

# 13. Categorical Columns

Examples:

```text
status
category
department
payment_method
country
gender
priority
order_type
```

## What Categorical Columns May Contain

```text
Different casing
Typos
Abbreviations
Synonyms
Old category names
New category names
Mixed languages
Extra spaces
Plural/singular variants
```

Examples:

```text
'completed'
'complete'
'Completed'
'delivered'
'cancelled'
'canceled'
'COD'
'Cash on Delivery'
'cash'
```

---

## What to Look For

### Frequency table

```sql
SELECT
    LOWER(TRIM(category_column)) AS normalized_value,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(category_column))
ORDER BY total_rows DESC;
```

### Rare categories

```sql
SELECT
    LOWER(TRIM(category_column)) AS normalized_value,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(category_column))
HAVING COUNT(*) <= 5
ORDER BY total_rows ASC;
```

### Standardize with CASE

```sql
SELECT
    CASE
        WHEN LOWER(TRIM(payment_method)) IN ('card', 'credit card', 'debit card') THEN 'Card'
        WHEN LOWER(TRIM(payment_method)) IN ('cash', 'cod', 'cash on delivery') THEN 'Cash'
        WHEN LOWER(TRIM(payment_method)) IN ('paypal') THEN 'PayPal'
        ELSE 'Other'
    END AS clean_payment_method
FROM table_name;
```

---

## Better Practice: Use Mapping Tables

Instead of hardcoding many `CASE` conditions, create a reference table.

```sql
CREATE TABLE payment_method_map (
    raw_value VARCHAR(100),
    clean_value VARCHAR(100)
);
```

Insert mappings:

```sql
INSERT INTO payment_method_map VALUES
('card', 'Card'),
('credit card', 'Card'),
('debit card', 'Card'),
('cash', 'Cash'),
('cod', 'Cash'),
('cash on delivery', 'Cash');
```

Use the mapping table:

```sql
SELECT
    t.payment_method,
    COALESCE(m.clean_value, 'Unmapped') AS clean_payment_method
FROM transactions t
LEFT JOIN payment_method_map m
    ON LOWER(TRIM(t.payment_method)) = m.raw_value;
```

Find unmapped values:

```sql
SELECT
    LOWER(TRIM(t.payment_method)) AS unmapped_value,
    COUNT(*) AS total_rows
FROM transactions t
LEFT JOIN payment_method_map m
    ON LOWER(TRIM(t.payment_method)) = m.raw_value
WHERE m.clean_value IS NULL
GROUP BY LOWER(TRIM(t.payment_method))
ORDER BY total_rows DESC;
```

---

## Best Practices for Categorical Columns

1. Always profile unique values.
2. Create mapping tables for repeated cleaning.
3. Avoid long hardcoded `CASE` statements for large projects.
4. Track unmapped values.
5. Do not group unknown values into `Other` too early.
6. Document standard categories.
7. Keep raw and cleaned category values if possible.

---

# 14. ID / Key Columns

Examples:

```text
customer_id
order_id
employee_id
invoice_id
product_sku
transaction_id
```

## What ID Columns May Contain

```text
Duplicates
Missing IDs
Different formats
Extra spaces
Leading zeroes
Mixed prefixes
Wrong length
Case differences
IDs stored as numbers
```

Examples:

```text
'00123'
'123'
' ORD-001 '
'ord-001'
'ORD001'
NULL
''
```

---

## What to Look For

### Missing IDs

```sql
SELECT *
FROM table_name
WHERE id_column IS NULL
   OR TRIM(id_column) = '';
```

### Duplicate IDs

```sql
SELECT
    TRIM(id_column) AS clean_id,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY TRIM(id_column)
HAVING COUNT(*) > 1;
```

### Case-insensitive duplicate IDs

```sql
SELECT
    LOWER(TRIM(id_column)) AS normalized_id,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(id_column))
HAVING COUNT(*) > 1;
```

### Wrong length IDs

```sql
SELECT *
FROM table_name
WHERE CHAR_LENGTH(TRIM(id_column)) <> 10;
```

---

## Best Practices for ID Columns

1. Store IDs as text if leading zeroes matter.
2. Do not cast IDs to numbers unless you are sure.
3. Trim spaces.
4. Standardize casing if IDs are case-insensitive.
5. Check duplicates.
6. Check missing IDs.
7. Check format patterns.
8. Use primary keys only after validation.

Example ID pattern check:

```sql
SELECT *
FROM table_name
WHERE id_column NOT REGEXP '^ORD-[0-9]{5}$';
```

---

# 15. Address Columns

Examples:

```text
address
billing_address
shipping_address
street_address
```

## What Address Columns May Contain

```text
Extra spaces
Line breaks
Missing parts
Different spellings
Abbreviations
Special characters
PIN/ZIP codes mixed inside address
City mixed inside address
Country mixed inside address
```

---

## What to Look For

### Blank addresses

```sql
SELECT *
FROM table_name
WHERE address IS NULL
   OR TRIM(address) = '';
```

### Very short addresses

```sql
SELECT *
FROM table_name
WHERE CHAR_LENGTH(TRIM(address)) < 10;
```

### Line breaks

```sql
SELECT *
FROM table_name
WHERE address REGEXP '[\r\n]';
```

### Remove line breaks

```sql
SELECT
    REPLACE(REPLACE(address, CHAR(13), ' '), CHAR(10), ' ') AS clean_address
FROM table_name;
```

---

## Best Practices for Address Columns

1. Do not over-clean addresses automatically.
2. Keep original address.
3. Remove only obvious extra spaces and line breaks.
4. Separate city, state, postal code, and country if possible.
5. Use external address validation if accuracy is important.
6. Do not assume abbreviations are wrong.

---

# 16. Country, State, and City Columns

## What Location Columns May Contain

```text
Abbreviations
Spelling mistakes
Multiple languages
Uppercase/lowercase differences
Country codes
Old names
Extra spaces
```

Examples:

```text
'USA'
'US'
'United States'
'U.S.A.'
'PK'
'Pak'
'Pakistan'
'IN'
'India'
```

---

## What to Look For

### Frequency profile

```sql
SELECT
    LOWER(TRIM(country)) AS normalized_country,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(country))
ORDER BY total_rows DESC;
```

### Standardize with mapping table

```sql
CREATE TABLE country_map (
    raw_country VARCHAR(100),
    clean_country VARCHAR(100)
);
```

Example:

```sql
INSERT INTO country_map VALUES
('usa', 'United States'),
('us', 'United States'),
('u.s.a.', 'United States'),
('pk', 'Pakistan'),
('pak', 'Pakistan'),
('pakistan', 'Pakistan');
```

Use it:

```sql
SELECT
    t.country,
    COALESCE(m.clean_country, 'Unmapped') AS clean_country
FROM table_name t
LEFT JOIN country_map m
    ON LOWER(TRIM(t.country)) = m.raw_country;
```

---

## Best Practices for Location Columns

1. Use official country names or ISO codes.
2. Store country, state, city, and postal code separately.
3. Use mapping tables.
4. Avoid manually correcting every typo without review.
5. Track unmapped locations.
6. Be careful with cities that have the same name in different countries.

---

# 17. URL / Website Columns

Examples:

```text
website
profile_url
source_url
image_url
landing_page
```

## What URL Columns May Contain

```text
Missing protocol
Spaces
Invalid characters
Only domain
Tracking parameters
Uppercase letters
Broken URLs
```

Examples:

```text
'example.com'
'https://example.com'
'http://example.com'
' www.example.com '
'N/A'
```

---

## What to Look For

### Missing URLs

```sql
SELECT *
FROM table_name
WHERE url IS NULL
   OR TRIM(url) = '';
```

### Basic invalid URLs

```sql
SELECT *
FROM table_name
WHERE LOWER(TRIM(url)) NOT REGEXP '^(http://|https://)';
```

### Add protocol if missing

```sql
SELECT
    CASE
        WHEN LOWER(TRIM(url)) REGEXP '^(http://|https://)' THEN LOWER(TRIM(url))
        ELSE CONCAT('https://', LOWER(TRIM(url)))
    END AS clean_url
FROM table_name;
```

---

## Best Practices for URL Columns

1. Trim spaces.
2. Lowercase domain portion when needed.
3. Decide whether to keep or remove tracking parameters.
4. Do not assume all missing protocols should be `https`.
5. Validate with business rules if URLs are important.

---

# 18. JSON Columns

Examples:

```text
metadata
settings
event_payload
api_response
```

## What JSON Columns May Contain

```text
Invalid JSON
Missing keys
Null values
Inconsistent key names
Nested objects
Arrays
Mixed datatypes
```

---

## What to Look For

### Validate JSON

```sql
SELECT *
FROM table_name
WHERE JSON_VALID(json_column) = 0;
```

### Extract JSON value

```sql
SELECT JSON_EXTRACT(json_column, '$.key_name') AS extracted_value
FROM table_name;
```

### Extract unquoted value

```sql
SELECT JSON_UNQUOTE(JSON_EXTRACT(json_column, '$.key_name')) AS extracted_value
FROM table_name;
```

---

## Best Practices for JSON Columns

1. Validate JSON before extracting.
2. Extract important fields into normal columns for reporting.
3. Watch for missing keys.
4. Watch for inconsistent key names.
5. Avoid storing highly important relational data only inside JSON.
6. Document JSON structure.

---

# 19. Duplicate Detection

Duplicates are one of the most common data problems.

## Exact Duplicate Rows

If all columns are repeated:

```sql
SELECT
    column1,
    column2,
    column3,
    COUNT(*) AS duplicate_count
FROM table_name
GROUP BY column1, column2, column3
HAVING COUNT(*) > 1;
```

---

## Duplicate by ID

```sql
SELECT
    id_column,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY id_column
HAVING COUNT(*) > 1;
```

---

## Duplicate by Business Key

Example: same email and phone.

```sql
SELECT
    LOWER(TRIM(email)) AS clean_email,
    REGEXP_REPLACE(phone, '[^0-9]', '') AS clean_phone,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY
    LOWER(TRIM(email)),
    REGEXP_REPLACE(phone, '[^0-9]', '')
HAVING COUNT(*) > 1;
```

---

## Find Duplicate Rows Using ROW_NUMBER

This is useful when you want to keep one row and flag the rest.

```sql
WITH duplicate_check AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY LOWER(TRIM(email))
            ORDER BY created_at DESC
        ) AS row_num
    FROM table_name
)
SELECT *
FROM duplicate_check
WHERE row_num > 1;
```

---

## Best Practices for Duplicates

1. Define what “duplicate” means first.
2. Use different duplicate rules for different tables.
3. Do not delete duplicates immediately.
4. Use `ROW_NUMBER()` to rank duplicates.
5. Keep the most complete, latest, or most trusted record.
6. Create a duplicate-review table before deleting.
7. Document deduplication rules.

---

# 20. Outlier Detection

Outliers are unusual values. They are not always wrong.

Examples:

```text
Very high price
Very large quantity
Age = 150
Discount = 500%
Salary = 999999999
Future birth date
```

---

## Basic Outlier Checks

### Min, max, average

```sql
SELECT
    MIN(numeric_column) AS min_value,
    MAX(numeric_column) AS max_value,
    AVG(numeric_column) AS avg_value
FROM table_name;
```

### Values above business limit

```sql
SELECT *
FROM table_name
WHERE numeric_column > 100000;
```

### Values below business limit

```sql
SELECT *
FROM table_name
WHERE numeric_column < 0;
```

---

## Best Practices for Outliers

1. Do not remove outliers automatically.
2. Check whether the value is possible.
3. Use business rules.
4. Flag extreme values.
5. Ask domain experts if needed.
6. Keep original values.

---

# 21. Data Quality Flags

Instead of deleting bad rows, create flags.

Example:

```sql
SELECT
    *,
    CASE
        WHEN email IS NULL OR TRIM(email) = '' THEN 'Missing Email'
        WHEN email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$' THEN 'Invalid Email'
        ELSE 'Valid Email'
    END AS email_quality_status
FROM table_name;
```

Multiple flags:

```sql
SELECT
    *,
    CASE
        WHEN customer_name IS NULL OR TRIM(customer_name) = '' THEN 1
        ELSE 0
    END AS is_missing_name,

    CASE
        WHEN email IS NULL
          OR email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$' THEN 1
        ELSE 0
    END AS is_invalid_email,

    CASE
        WHEN quantity IS NULL
          OR quantity NOT REGEXP '^[0-9]+$'
          OR CAST(quantity AS SIGNED) <= 0 THEN 1
        ELSE 0
    END AS is_invalid_quantity
FROM table_name;
```

---

# 22. Rejected Records Table

A professional workflow often separates rejected rows.

```sql
CREATE TABLE rejected_records AS
SELECT *
FROM table_name
WHERE customer_name IS NULL
   OR TRIM(customer_name) = ''
   OR email IS NULL
   OR email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$';
```

Better version with reason:

```sql
CREATE TABLE rejected_records AS
SELECT
    *,
    CASE
        WHEN customer_name IS NULL OR TRIM(customer_name) = '' THEN 'Missing customer name'
        WHEN email IS NULL OR TRIM(email) = '' THEN 'Missing email'
        WHEN email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$' THEN 'Invalid email'
        ELSE 'Other issue'
    END AS rejection_reason
FROM table_name
WHERE customer_name IS NULL
   OR TRIM(customer_name) = ''
   OR email IS NULL
   OR TRIM(email) = ''
   OR email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$';
```

---

# 23. Clean Table Pattern

Instead of changing the raw table, create a clean table.

```sql
CREATE TABLE clean_table AS
SELECT
    TRIM(id_column) AS id_column,
    NULLIF(TRIM(name), '') AS name,
    LOWER(TRIM(email)) AS email,
    REGEXP_REPLACE(phone, '[^0-9]', '') AS phone,
    CAST(REGEXP_REPLACE(price, '[^0-9.]', '') AS DECIMAL(10,2)) AS price
FROM raw_table;
```

---

# 24. Better Clean Table Pattern With CTE

```sql
CREATE TABLE clean_table AS
WITH cleaned AS (
    SELECT
        TRIM(id_column) AS id_column,

        NULLIF(TRIM(name), '') AS clean_name,

        LOWER(TRIM(email)) AS clean_email,

        REGEXP_REPLACE(phone, '[^0-9]', '') AS clean_phone,

        CASE
            WHEN quantity REGEXP '^[0-9]+$'
            THEN CAST(quantity AS UNSIGNED)
            ELSE NULL
        END AS clean_quantity,

        CASE
            WHEN price IS NOT NULL
            THEN CAST(REGEXP_REPLACE(price, '[^0-9.]', '') AS DECIMAL(10,2))
            ELSE NULL
        END AS clean_price

    FROM raw_table
)
SELECT *
FROM cleaned;
```

---

# 25. Data Profiling Dashboard Queries

Use these queries before cleaning.

## Total rows

```sql
SELECT COUNT(*) AS total_rows
FROM table_name;
```

## Missing values per column

```sql
SELECT
    SUM(column1 IS NULL OR TRIM(column1) = '') AS missing_column1,
    SUM(column2 IS NULL OR TRIM(column2) = '') AS missing_column2,
    SUM(column3 IS NULL OR TRIM(column3) = '') AS missing_column3
FROM table_name;
```

## Distinct count per column

```sql
SELECT
    COUNT(DISTINCT column1) AS distinct_column1,
    COUNT(DISTINCT column2) AS distinct_column2,
    COUNT(DISTINCT column3) AS distinct_column3
FROM table_name;
```

## Most common values

```sql
SELECT
    LOWER(TRIM(column_name)) AS value_found,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(column_name))
ORDER BY total_rows DESC
LIMIT 20;
```

## Rare values

```sql
SELECT
    LOWER(TRIM(column_name)) AS value_found,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(column_name))
HAVING COUNT(*) <= 3
ORDER BY total_rows ASC;
```

---

# 26. Common Cleaning Shortcuts

| Task                        | Shortcut                                           |
| --------------------------- | -------------------------------------------------- |
| Remove spaces               | `TRIM(column)`                                     |
| Normalize text for matching | `LOWER(TRIM(column))`                              |
| Blank to NULL               | `NULLIF(TRIM(column), '')`                         |
| NULL to fallback            | `COALESCE(column, 'Unknown')`                      |
| Remove symbols from phone   | `REGEXP_REPLACE(phone, '[^0-9]', '')`              |
| Remove symbols from price   | `REGEXP_REPLACE(price, '[^0-9.]', '')`             |
| Convert to number           | `CAST(column AS DECIMAL(10,2))`                    |
| Convert to date             | `STR_TO_DATE(column, format)`                      |
| Validate pattern            | `column REGEXP 'pattern'`                          |
| Find duplicates             | `GROUP BY column HAVING COUNT(*) > 1`              |
| Rank duplicates             | `ROW_NUMBER() OVER(PARTITION BY ... ORDER BY ...)` |
| Standardize categories      | `CASE WHEN ... THEN ... END`                       |
| Use lookup mapping          | `LEFT JOIN mapping_table`                          |

---

# 27. Common Regex Patterns

| Use Case            | Regex                                                 |
| ------------------- | ----------------------------------------------------- |
| Contains number     | `'[0-9]'`                                             |
| Contains letters    | `'[A-Za-z]'`                                          |
| Only digits         | `'^[0-9]+$'`                                          |
| Signed integer      | `'^-?[0-9]+$'`                                        |
| Decimal number      | `'^-?[0-9]+(\\.[0-9]+)?$'`                            |
| Email basic         | `'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'` |
| Multiple spaces     | `' {2,}'`                                             |
| Starts with ORD-    | `'^ORD-'`                                             |
| Specific ID pattern | `'^ORD-[0-9]{5}$'`                                    |

---

# 28. Datatype-Specific Warning List

## Text Columns

Watch for:

```text
Spaces
Case differences
Typos
Fake values
Abbreviations
Symbols
Numbers
Encoding issues
```

Best practice:

```text
Trim
Normalize case for matching
Use mapping tables
Keep original values
```

---

## Number Columns

Watch for:

```text
Text values
Commas
Units
Negative values
Zero values
Outliers
Invalid ranges
```

Best practice:

```text
Validate before casting
Use DECIMAL for money
Apply business rules
Flag outliers
```

---

## Date Columns

Watch for:

```text
Mixed formats
Invalid dates
Future dates
Impossible old dates
Ambiguous day/month order
Timezone issues
```

Best practice:

```text
Use STR_TO_DATE
Store as DATE/DATETIME
Avoid text dates
Confirm source format
```

---

## Boolean Columns

Watch for:

```text
Yes/No
Y/N
True/False
1/0
Active/Inactive
Blank values
```

Best practice:

```text
Map to 1/0
Keep NULL for unknown
Do not treat blank as false automatically
```

---

## Category Columns

Watch for:

```text
Synonyms
Typos
Plural/singular differences
Abbreviations
Old labels
Rare categories
```

Best practice:

```text
Profile frequency
Use mapping tables
Track unmapped values
Document allowed categories
```

---

## ID Columns

Watch for:

```text
Duplicates
Missing IDs
Leading zeroes
Wrong format
Case differences
Spaces
```

Best practice:

```text
Store as text if leading zeroes matter
Check duplicates
Validate pattern
Do not cast blindly
```

---

## Email Columns

Watch for:

```text
Missing @
Invalid domain
Uppercase
Spaces
Fake emails
Duplicate emails
```

Best practice:

```text
Lowercase
Trim
Validate with regex
Use as duplicate clue, not always unique truth
```

---

## Phone Columns

Watch for:

```text
Country codes
Spaces
Dashes
Leading zeroes
Fake numbers
Wrong length
Letters
```

Best practice:

```text
Store as text
Remove formatting characters
Validate by country
Do not remove leading zeroes accidentally
```

---

# 29. Best Practices for Professional Data Cleaning

## 1. Keep the Raw Table Untouched

Do not directly overwrite raw data unless you have a backup.

Good structure:

```text
raw_table
clean_table
rejected_table
mapping_tables
quality_report
```

---

## 2. Clean in Layers

Layer 1:

```text
Trim spaces
Lowercase matching fields
Convert blanks to NULL
```

Layer 2:

```text
Standardize categories
Clean dates
Clean numbers
Validate emails and phones
```

Layer 3:

```text
Detect duplicates
Detect outliers
Create quality flags
Separate rejected rows
```

---

## 3. Use Mapping Tables

For categories, countries, statuses, departments, product names, and payment methods, mapping tables are better than very long `CASE` statements.

Example:

```text
raw_value              clean_value
------------------------------------
credit card            Card
debit card             Card
cc                     Card
cod                    Cash
cash on delivery       Cash
```

---

## 4. Document Every Rule

For every cleaning rule, record:

```text
Column name
Problem found
Cleaning logic
Reason for rule
Date added
Who approved it
```

Example:

```text
Column: payment_method
Problem: COD, Cash, Cash on Delivery used for same method
Rule: Map all to Cash
Reason: Business reporting needs one payment category
```

---

## 5. Separate Invalid Data Instead of Deleting

Bad practice:

```sql
DELETE FROM table_name
WHERE email IS NULL;
```

Better practice:

```sql
CREATE TABLE rejected_records AS
SELECT *
FROM table_name
WHERE email IS NULL;
```

---

## 6. Create Quality Flags

Flags help analysts understand trust level.

Example:

```text
is_missing_email
is_invalid_phone
is_duplicate_customer
is_invalid_date
is_outlier_amount
```

---

## 7. Validate After Cleaning

After creating the clean table, check:

```sql
SELECT COUNT(*) FROM raw_table;
SELECT COUNT(*) FROM clean_table;
SELECT COUNT(*) FROM rejected_table;
```

The numbers should make sense.

Example:

```text
raw rows = clean rows + rejected rows
```

---

## 8. Avoid Over-Cleaning

Do not change data just because it looks unusual.

Examples:

```text
A short name may be real.
A high order amount may be real.
A foreign phone number may have a different length.
A rare category may be a new product line.
```

Flag first. Change only after logic is confirmed.

---

## 9. Use Business Rules

Technical validation is not enough.

Example:

```text
Age = 150
```

Technically numeric, but probably invalid.

Example:

```text
Discount = 120%
```

Technically numeric, but business-wise suspicious.

Example:

```text
Order date in future
```

Technically valid date, but possibly incorrect.

---

## 10. Make Cleaning Repeatable

Avoid manual one-time fixes.

Good cleaning should be:

```text
Repeatable
Auditable
Documented
Reusable
Testable
```

Use views, CTEs, stored procedures, scripts, or ETL pipelines.

---

# 30. General Cleaning Template

Use this as a starting point.

```sql
WITH profiled AS (
    SELECT
        *,
        LOWER(TRIM(text_column)) AS normalized_text,
        NULLIF(TRIM(text_column), '') AS cleaned_text,
        REGEXP_REPLACE(phone_column, '[^0-9]', '') AS cleaned_phone,

        CASE
            WHEN numeric_column REGEXP '^-?[0-9]+(\\.[0-9]+)?$'
            THEN CAST(numeric_column AS DECIMAL(10,2))
            ELSE NULL
        END AS cleaned_number,

        CASE
            WHEN date_column REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
            THEN STR_TO_DATE(date_column, '%Y-%m-%d')
            ELSE NULL
        END AS cleaned_date

    FROM raw_table
),

quality_flags AS (
    SELECT
        *,
        CASE
            WHEN cleaned_text IS NULL THEN 1 ELSE 0
        END AS is_missing_text,

        CASE
            WHEN cleaned_number IS NULL THEN 1 ELSE 0
        END AS is_invalid_number,

        CASE
            WHEN cleaned_date IS NULL THEN 1 ELSE 0
        END AS is_invalid_date

    FROM profiled
)

SELECT *
FROM quality_flags;
```

---

# 31. Final Data Cleaning Checklist

Before cleaning:

```text
Understand columns
Check datatypes
Check row count
Check distinct values
Check missing values
Check duplicates
Check invalid formats
Check outliers
```

During cleaning:

```text
Trim text
Standardize case
Convert blanks to NULL
Clean numbers
Clean dates
Standardize categories
Validate emails
Validate phone numbers
Use mapping tables
Create quality flags
```

After cleaning:

```text
Compare row counts
Check rejected rows
Check duplicates again
Check summary statistics
Validate business rules
Document cleaning rules
Save clean table
Keep raw table safe
```

---

# 32. Most Important Things to Remember

```text
1. Do not assume bad values in advance.
2. Profile the data first.
3. Frequency counts reveal hidden problems.
4. Keep raw data unchanged.
5. Use TRIM, LOWER, REPLACE, REGEXP_REPLACE, CAST, STR_TO_DATE, CASE.
6. Use mapping tables for categories.
7. Use quality flags instead of deleting quickly.
8. Store rejected records separately.
9. Clean based on business rules, not just technical rules.
10. Document every cleaning decision.
```

The most useful MySQL cleaning expression is:

```sql
LOWER(TRIM(column_name))
```

The most useful profiling query is:

```sql
SELECT
    LOWER(TRIM(column_name)) AS value_found,
    COUNT(*) AS total_rows
FROM table_name
GROUP BY LOWER(TRIM(column_name))
ORDER BY total_rows DESC;
```

The most useful professional mindset is:

```text
Discover first.
Clean second.
Validate third.
Document always.
```
