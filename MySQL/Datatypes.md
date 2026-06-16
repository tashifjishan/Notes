# MySQL Datatypes — Detailed Notes for Data Analysis

## 1. Introduction to MySQL Datatypes

In MySQL, a datatype defines what kind of value a column can store.

For example:

```sql
customer_name VARCHAR(100)
age INT
price DECIMAL(10,2)
order_date DATE
```

Each column must have a datatype. Choosing the correct datatype is important because it affects:

* Data accuracy
* Storage size
* Query speed
* Sorting behavior
* Filtering behavior
* Aggregation results
* Dashboard and reporting quality

For data analysis, wrong datatype selection can create serious problems. For example, storing dates as text makes monthly trend analysis difficult. Storing money as `FLOAT` can create rounding issues. Storing numeric IDs as text can slow down joins.

---

# 2. Main Categories of MySQL Datatypes

MySQL datatypes can be divided into the following main categories:

| Category                | Purpose                         | Examples                                        |
| ----------------------- | ------------------------------- | ----------------------------------------------- |
| Numeric Datatypes       | Store numbers                   | `INT`, `DECIMAL`, `FLOAT`, `DOUBLE`             |
| Date and Time Datatypes | Store dates and time values     | `DATE`, `DATETIME`, `TIMESTAMP`, `TIME`, `YEAR` |
| String Datatypes        | Store text and binary data      | `CHAR`, `VARCHAR`, `TEXT`, `BLOB`               |
| JSON Datatype           | Store JSON documents            | `JSON`                                          |
| Spatial Datatypes       | Store geographic/geometric data | `POINT`, `POLYGON`, `GEOMETRY`                  |

---

# 3. Numeric Datatypes

Numeric datatypes are used to store numbers. These are very important in data analysis because most business metrics are numeric.

Examples:

* Sales amount
* Quantity sold
* Product price
* Customer age
* Salary
* Discount percentage
* Rating
* Revenue
* Profit
* Tax amount

Numeric datatypes are divided into:

1. Integer types
2. Fixed-point types
3. Floating-point types
4. Bit type

---

## 3.1 Integer Datatypes

Integer datatypes store whole numbers without decimal points.

Examples:

```sql
10
250
-45
100000
```

Integer types are commonly used for:

* IDs
* Counts
* Quantities
* Age
* Number of orders
* Number of products
* Ranking values

---

## 3.2 Integer Type Range Table

| Datatype          | Storage |                    Signed Range |            Unsigned Range | Common Use                         |
| ----------------- | ------: | ------------------------------: | ------------------------: | ---------------------------------- |
| `TINYINT`         |  1 byte |                     -128 to 127 |                  0 to 255 | Status flags, small ratings        |
| `SMALLINT`        | 2 bytes |               -32,768 to 32,767 |               0 to 65,535 | Small counts                       |
| `MEDIUMINT`       | 3 bytes |         -8,388,608 to 8,388,607 |           0 to 16,777,215 | Medium-size IDs                    |
| `INT` / `INTEGER` | 4 bytes | -2,147,483,648 to 2,147,483,647 |        0 to 4,294,967,295 | IDs, counts, quantities            |
| `BIGINT`          | 8 bytes |                Very large range | Very large positive range | Large IDs, big transaction systems |

---

## 3.3 TINYINT

`TINYINT` stores very small whole numbers.

Example:

```sql
is_active TINYINT
rating TINYINT
```

Common use cases:

* Active or inactive status
* Yes or no values
* Small rating scale
* Tiny category codes

Example:

```sql
CREATE TABLE users (
    user_id INT,
    user_name VARCHAR(100),
    is_active TINYINT
);
```

Example data:

| user_id | user_name | is_active |
| ------: | --------- | --------: |
|       1 | Ali       |         1 |
|       2 | Ahmed     |         0 |

Here:

* `1` means active
* `0` means inactive

---

## 3.4 SMALLINT

`SMALLINT` stores small whole numbers.

Example:

```sql
total_items SMALLINT
employee_count SMALLINT
```

Common use cases:

* Number of employees in a small branch
* Number of items in a small order
* Small numeric codes

---

## 3.5 MEDIUMINT

`MEDIUMINT` stores medium-range whole numbers.

It is not used as commonly as `INT`, but it can be useful when the value range is bigger than `SMALLINT` but smaller than `INT`.

Example:

```sql
city_population MEDIUMINT
```

---

## 3.6 INT / INTEGER

`INT` is one of the most commonly used numeric datatypes in MySQL.

Example:

```sql
customer_id INT
order_id INT
quantity INT
```

Common use cases:

* Primary keys
* Foreign keys
* Product quantity
* Number of orders
* Count values

Example:

```sql
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    quantity INT
);
```

---

## 3.7 BIGINT

`BIGINT` stores very large whole numbers.

Common use cases:

* Very large IDs
* Large transaction numbers
* Big data systems
* Analytics tables with millions or billions of rows

Example:

```sql
transaction_id BIGINT
```

Use `BIGINT` only when needed. Do not use it blindly for every ID because it uses more storage than `INT`.

---

# 4. Signed and Unsigned Integers

By default, integer datatypes are signed.

Signed means the column can store both negative and positive values.

Example:

```sql
temperature INT
```

This can store:

```sql
-10
0
25
```

Unsigned means the column stores only zero and positive values.

Example:

```sql
quantity INT UNSIGNED
```

This can store:

```sql
0
1
100
500
```

It cannot store:

```sql
-5
```

---

## 4.1 When to Use UNSIGNED

Use `UNSIGNED` when negative values are impossible.

Good examples:

```sql
age TINYINT UNSIGNED
quantity INT UNSIGNED
total_orders INT UNSIGNED
customer_id INT UNSIGNED
```

Bad example:

```sql
profit INT UNSIGNED
```

Profit can be negative, so `UNSIGNED` is not suitable.

---

# 5. AUTO_INCREMENT

`AUTO_INCREMENT` automatically generates a new number for each new row.

It is commonly used for primary keys.

Example:

```sql
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100)
);
```

When a new customer is inserted, MySQL automatically assigns the next ID.

Example:

```sql
INSERT INTO customers (customer_name)
VALUES ('Ali');
```

Result:

| customer_id | customer_name |
| ----------: | ------------- |
|           1 | Ali           |

---

# 6. BOOLEAN Datatype

MySQL supports `BOOLEAN`, but internally it behaves like `TINYINT(1)`.

Example:

```sql
is_paid BOOLEAN
```

This usually stores:

| Value | Meaning |
| ----: | ------- |
|     1 | True    |
|     0 | False   |

Example:

```sql
CREATE TABLE payments (
    payment_id INT,
    is_paid BOOLEAN
);
```

For analysis, Boolean fields are useful for filtering.

Example:

```sql
SELECT *
FROM payments
WHERE is_paid = 1;
```

---

# 7. Fixed-Point Datatypes

Fixed-point datatypes store exact decimal values.

The main fixed-point datatype in MySQL is:

```sql
DECIMAL
```

`DECIMAL` is also known as an exact numeric type.

---

## 7.1 DECIMAL

`DECIMAL` is used when exact precision is required.

Common use cases:

* Price
* Revenue
* Salary
* Tax
* Discount
* Profit
* Financial values

Syntax:

```sql
DECIMAL(M, D)
```

Where:

* `M` = total number of digits
* `D` = number of digits after the decimal point

Example:

```sql
price DECIMAL(10,2)
```

This means:

* Total digits allowed: 10
* Digits after decimal point: 2

Example values:

```sql
99999999.99
1500.50
25.75
```

---

## 7.2 DECIMAL Example

```sql
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);
```

Example data:

| product_id | product_name |    price |
| ---------: | ------------ | -------: |
|          1 | Laptop       | 75000.00 |
|          2 | Mouse        |   850.50 |
|          3 | Keyboard     |  1500.75 |

---

## 7.3 Why DECIMAL Is Better for Money

For financial analysis, use `DECIMAL`, not `FLOAT`.

Good:

```sql
sales_amount DECIMAL(12,2)
```

Avoid:

```sql
sales_amount FLOAT
```

Reason:

`DECIMAL` stores exact values. `FLOAT` and `DOUBLE` store approximate values, which can create rounding issues.

For data analysis, small rounding errors can create wrong totals in financial reports.

---

# 8. Floating-Point Datatypes

Floating-point datatypes store approximate decimal values.

Main types:

```sql
FLOAT
DOUBLE
```

---

## 8.1 FLOAT

`FLOAT` stores approximate decimal numbers with less precision than `DOUBLE`.

Common use cases:

* Scientific values
* Sensor readings
* Approximate measurements
* Machine learning features
* Percentage values where exact precision is not critical

Example:

```sql
temperature FLOAT
```

---

## 8.2 DOUBLE

`DOUBLE` stores approximate decimal numbers with more precision than `FLOAT`.

Example:

```sql
latitude DOUBLE
longitude DOUBLE
```

Common use cases:

* Scientific calculations
* Large decimal measurements
* Geolocation values
* Statistical calculations

---

## 8.3 FLOAT vs DOUBLE vs DECIMAL

| Datatype  | Type        | Precision | Best For                              |
| --------- | ----------- | --------- | ------------------------------------- |
| `FLOAT`   | Approximate | Lower     | Sensor data, approximate measurements |
| `DOUBLE`  | Approximate | Higher    | Scientific values, coordinates        |
| `DECIMAL` | Exact       | Fixed     | Money, revenue, salary, price         |

---

# 9. BIT Datatype

`BIT` stores bit values.

Syntax:

```sql
BIT(M)
```

Where `M` is the number of bits.

Example:

```sql
permission_flags BIT(4)
```

Common use cases:

* Binary flags
* Compact status storage
* Permission settings

For normal data analysis work, `BIT` is not used very often. Analysts usually work more with `TINYINT`, `BOOLEAN`, or clear category columns.

---

# 10. Date and Time Datatypes

Date and time datatypes are used to store temporal values.

These are critical for data analysis because many business questions are time-based.

Examples:

* Monthly revenue
* Daily orders
* Customer signup date
* Delivery time
* Payment date
* Yearly growth
* User activity trend

Main MySQL date and time datatypes:

| Datatype    | Stores                                          | Example               |
| ----------- | ----------------------------------------------- | --------------------- |
| `DATE`      | Date only                                       | `2026-06-16`          |
| `TIME`      | Time only                                       | `14:30:00`            |
| `DATETIME`  | Date and time                                   | `2026-06-16 14:30:00` |
| `TIMESTAMP` | Date and time with timezone conversion behavior | `2026-06-16 14:30:00` |
| `YEAR`      | Year only                                       | `2026`                |

---

## 10.1 DATE

`DATE` stores only the date.

Format:

```sql
YYYY-MM-DD
```

Example:

```sql
birth_date DATE
order_date DATE
```

Example:

```sql
CREATE TABLE customers (
    customer_id INT,
    customer_name VARCHAR(100),
    signup_date DATE
);
```

Good for:

* Birth date
* Order date
* Signup date
* Attendance date
* Invoice date

Example query:

```sql
SELECT *
FROM customers
WHERE signup_date = '2026-06-16';
```

---

## 10.2 TIME

`TIME` stores time values.

Format:

```sql
HH:MM:SS
```

Example:

```sql
login_time TIME
opening_time TIME
closing_time TIME
```

Good for:

* Store opening time
* Login time
* Shift start time
* Shift end time
* Duration values

Example:

```sql
CREATE TABLE employee_shifts (
    employee_id INT,
    shift_start TIME,
    shift_end TIME
);
```

---

## 10.3 DATETIME

`DATETIME` stores both date and time.

Format:

```sql
YYYY-MM-DD HH:MM:SS
```

Example:

```sql
order_created_at DATETIME
payment_completed_at DATETIME
```

Good for:

* Order creation time
* Payment time
* Login timestamp
* Event timestamp
* Appointment time

Example:

```sql
CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    order_created_at DATETIME
);
```

Example query:

```sql
SELECT *
FROM orders
WHERE order_created_at >= '2026-01-01 00:00:00';
```

---

## 10.4 TIMESTAMP

`TIMESTAMP` also stores date and time, but it is commonly used for tracking row creation and update times.

Example:

```sql
created_at TIMESTAMP
updated_at TIMESTAMP
```

Common use cases:

* Created time
* Updated time
* Last login time
* System event time

Example:

```sql
CREATE TABLE users (
    user_id INT,
    user_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Example with update tracking:

```sql
CREATE TABLE users (
    user_id INT,
    user_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

---

## 10.5 DATETIME vs TIMESTAMP

| Feature           | DATETIME                         | TIMESTAMP                              |
| ----------------- | -------------------------------- | -------------------------------------- |
| Stores            | Date and time                    | Date and time                          |
| Timezone behavior | No automatic timezone conversion | Can be affected by timezone conversion |
| Common use        | Business dates and events        | System-created and updated times       |
| Range             | Wider                            | More limited                           |
| Example           | Appointment date                 | Row created time                       |

Simple rule:

Use `DATETIME` for business event times.

Use `TIMESTAMP` for system tracking columns such as `created_at` and `updated_at`.

---

## 10.6 YEAR

`YEAR` stores only year values.

Example:

```sql
manufacture_year YEAR
graduation_year YEAR
```

Common use cases:

* Manufacturing year
* Model year
* Graduation year
* Financial year label

Example:

```sql
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(100),
    manufacture_year YEAR
);
```

---

# 11. Date and Time Analysis Examples

## 11.1 Extract Year

```sql
SELECT YEAR(order_date) AS order_year
FROM orders;
```

## 11.2 Extract Month

```sql
SELECT MONTH(order_date) AS order_month
FROM orders;
```

## 11.3 Monthly Sales

```sql
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS order_month,
    SUM(total_amount) AS monthly_revenue
FROM orders
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY order_month;
```

## 11.4 Find Orders from Current Year

```sql
SELECT *
FROM orders
WHERE YEAR(order_date) = YEAR(CURRENT_DATE);
```

## 11.5 Calculate Delivery Days

```sql
SELECT 
    order_id,
    DATEDIFF(delivery_date, order_date) AS delivery_days
FROM orders;
```

---

# 12. String Datatypes

String datatypes store text or binary data.

Common examples:

* Customer name
* Email
* Phone number
* Address
* Product name
* Category
* Description
* Status
* City
* Country

Main string datatypes:

| Datatype    | Purpose                                |
| ----------- | -------------------------------------- |
| `CHAR`      | Fixed-length text                      |
| `VARCHAR`   | Variable-length text                   |
| `TEXT`      | Long text                              |
| `BINARY`    | Fixed-length binary data               |
| `VARBINARY` | Variable-length binary data            |
| `BLOB`      | Large binary objects                   |
| `ENUM`      | One value from a predefined list       |
| `SET`       | Multiple values from a predefined list |

---

# 13. CHAR

`CHAR` stores fixed-length text.

Syntax:

```sql
CHAR(length)
```

Example:

```sql
country_code CHAR(2)
gender CHAR(1)
```

Good use cases:

* Country code: `PK`, `IN`, `US`
* Gender code: `M`, `F`
* Fixed status code
* Fixed-length short values

Example:

```sql
CREATE TABLE countries (
    country_code CHAR(2),
    country_name VARCHAR(100)
);
```

Important point:

If you store `'A'` in `CHAR(5)`, MySQL may pad it with spaces internally.

Use `CHAR` only when the length is always fixed.

---

# 14. VARCHAR

`VARCHAR` stores variable-length text.

Syntax:

```sql
VARCHAR(length)
```

Example:

```sql
customer_name VARCHAR(100)
email VARCHAR(255)
city VARCHAR(100)
```

Good use cases:

* Names
* Emails
* Phone numbers
* Cities
* Product names
* Categories
* Short descriptions

Example:

```sql
CREATE TABLE customers (
    customer_id INT,
    customer_name VARCHAR(100),
    email VARCHAR(255),
    city VARCHAR(100)
);
```

`VARCHAR` is one of the most commonly used datatypes in MySQL.

---

## 14.1 CHAR vs VARCHAR

| Feature  | CHAR                       | VARCHAR                                 |
| -------- | -------------------------- | --------------------------------------- |
| Length   | Fixed                      | Variable                                |
| Storage  | Uses fixed space           | Uses only needed space plus length info |
| Best for | Fixed codes                | Names, emails, descriptions             |
| Example  | `CHAR(2)` for country code | `VARCHAR(100)` for name                 |

Simple rule:

Use `CHAR` for fixed-length codes.

Use `VARCHAR` for normal text.

---

# 15. TEXT Datatypes

`TEXT` is used for long text values.

Examples:

* Product description
* Blog content
* User comments
* Reviews
* Support tickets
* Long notes

Types of `TEXT`:

| Datatype     |        Maximum Size | Use Case               |
| ------------ | ------------------: | ---------------------- |
| `TINYTEXT`   |           255 bytes | Short notes            |
| `TEXT`       |        65,535 bytes | Descriptions, comments |
| `MEDIUMTEXT` |    16,777,215 bytes | Long articles          |
| `LONGTEXT`   | 4,294,967,295 bytes | Very large documents   |

Example:

```sql
CREATE TABLE products (
    product_id INT,
    product_name VARCHAR(100),
    description TEXT
);
```

---

## 15.1 VARCHAR vs TEXT

| Feature                | VARCHAR              | TEXT                         |
| ---------------------- | -------------------- | ---------------------------- |
| Best for               | Short to medium text | Long text                    |
| Can have default value | Usually yes          | More restricted              |
| Common use             | Name, email, city    | Description, review, article |
| Indexing               | Easier               | May require prefix indexing  |

Simple rule:

Use `VARCHAR` when you know the maximum length is reasonable.

Use `TEXT` when the content can be long.

---

# 16. BINARY and VARBINARY

`BINARY` and `VARBINARY` store binary strings.

They are similar to `CHAR` and `VARCHAR`, but they store bytes instead of characters.

Examples:

```sql
hash_value BINARY(32)
encrypted_token VARBINARY(255)
```

Common use cases:

* Hashes
* Encrypted values
* Binary tokens
* Raw byte data

For normal data analysis, these are less common.

---

# 17. BLOB Datatypes

`BLOB` stands for Binary Large Object.

It stores large binary data such as:

* Images
* Audio files
* Video files
* PDF files
* Documents

Types of BLOB:

| Datatype     |        Maximum Size |
| ------------ | ------------------: |
| `TINYBLOB`   |           255 bytes |
| `BLOB`       |        65,535 bytes |
| `MEDIUMBLOB` |    16,777,215 bytes |
| `LONGBLOB`   | 4,294,967,295 bytes |

Example:

```sql
CREATE TABLE documents (
    document_id INT,
    file_name VARCHAR(255),
    file_data LONGBLOB
);
```

Important analysis note:

For analytics systems, it is usually better to store file paths or URLs in the database instead of storing large files directly in a `BLOB` column.

Better:

```sql
file_url VARCHAR(500)
```

Instead of:

```sql
file_data LONGBLOB
```

---

# 18. ENUM Datatype

`ENUM` stores one value from a predefined list.

Example:

```sql
status ENUM('Pending', 'Processing', 'Completed', 'Cancelled')
```

This means the column can only store one of those values.

Example:

```sql
CREATE TABLE orders (
    order_id INT,
    order_status ENUM('Pending', 'Processing', 'Completed', 'Cancelled')
);
```

Valid:

```sql
'Pending'
'Completed'
```

Invalid:

```sql
'Returned'
```

Unless `'Returned'` is added to the list.

---

## 18.1 Good Use Cases for ENUM

Use `ENUM` when the possible values are small and stable.

Good examples:

```sql
payment_status ENUM('Paid', 'Unpaid', 'Refunded')
order_status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled')
user_role ENUM('Admin', 'Manager', 'Customer')
```

Bad example:

```sql
city ENUM('Delhi', 'Mumbai', 'Karachi', 'Lahore', ...)
```

Cities can grow and change. Use a separate `cities` table instead.

---

## 18.2 ENUM for Analysis

`ENUM` can make data cleaner because it prevents random spelling variations.

Without `ENUM`, users may enter:

```sql
Completed
complete
COMPLETED
Complted
```

With `ENUM`, only approved values are allowed.

This improves grouping and reporting.

Example:

```sql
SELECT order_status, COUNT(*) AS total_orders
FROM orders
GROUP BY order_status;
```

---

# 19. SET Datatype

`SET` stores zero or more values from a predefined list.

Example:

```sql
skills SET('Excel', 'SQL', 'Python', 'Power BI')
```

One row can store:

```sql
'Excel,SQL'
```

Another row can store:

```sql
'Python,Power BI'
```

Example:

```sql
CREATE TABLE employees (
    employee_id INT,
    employee_name VARCHAR(100),
    skills SET('Excel', 'SQL', 'Python', 'Power BI')
);
```

---

## 19.1 Problem with SET in Analysis

`SET` can make analysis harder because multiple values are stored in one column.

Example:

| employee_id | skills         |
| ----------: | -------------- |
|           1 | Excel,SQL      |
|           2 | SQL,Python     |
|           3 | Excel,Power BI |

This is harder to analyze than a normalized table.

Better structure:

```sql
employees
employee_skills
skills
```

For serious data analysis, avoid storing multiple values in one column.

---

# 20. JSON Datatype

`JSON` stores JSON documents.

Example JSON value:

```json
{
  "name": "Ali",
  "age": 25,
  "city": "Lahore"
}
```

Example table:

```sql
CREATE TABLE user_profiles (
    user_id INT,
    profile_data JSON
);
```

Insert example:

```sql
INSERT INTO user_profiles (user_id, profile_data)
VALUES (
    1,
    '{"name": "Ali", "age": 25, "city": "Lahore"}'
);
```

---

## 20.1 When to Use JSON

Use `JSON` when the data structure is flexible or semi-structured.

Good use cases:

* API response data
* User preferences
* Product attributes that vary by category
* Event metadata
* Form responses
* Logs

Example:

```sql
product_attributes JSON
```

A laptop may have:

```json
{
  "ram": "16GB",
  "storage": "512GB SSD",
  "processor": "i5"
}
```

A shirt may have:

```json
{
  "size": "M",
  "color": "Blue",
  "fabric": "Cotton"
}
```

Both products have different attributes, so JSON can be useful.

---

## 20.2 When Not to Use JSON

Do not use JSON for important fields that you frequently filter, join, or group by.

Bad design:

```sql
customer_data JSON
```

Containing:

```json
{
  "customer_id": 1,
  "country": "Pakistan",
  "city": "Lahore"
}
```

Better design:

```sql
customer_id INT
country VARCHAR(100)
city VARCHAR(100)
```

Reason:

Normal columns are easier to index, filter, join, and analyze.

---

## 20.3 JSON Query Example

```sql
SELECT 
    user_id,
    JSON_EXTRACT(profile_data, '$.city') AS city
FROM user_profiles;
```

Alternative syntax:

```sql
SELECT 
    user_id,
    profile_data->'$.city' AS city
FROM user_profiles;
```

To return the value without JSON quotes:

```sql
SELECT 
    user_id,
    profile_data->>'$.city' AS city
FROM user_profiles;
```

---

# 21. Spatial Datatypes

Spatial datatypes store geometric or geographic data.

Common spatial datatypes:

| Datatype             | Meaning                       |
| -------------------- | ----------------------------- |
| `GEOMETRY`           | Any geometry value            |
| `POINT`              | A single location point       |
| `LINESTRING`         | A line                        |
| `POLYGON`            | A shape/area                  |
| `MULTIPOINT`         | Multiple points               |
| `MULTILINESTRING`    | Multiple lines                |
| `MULTIPOLYGON`       | Multiple polygons             |
| `GEOMETRYCOLLECTION` | Collection of geometry values |

---

## 21.1 POINT

`POINT` stores a single geographic point.

Example:

```sql
location POINT
```

Common use cases:

* Store location coordinates
* Store delivery address coordinates
* Store shop location
* Store customer location
* Store map points

Example:

```sql
CREATE TABLE stores (
    store_id INT,
    store_name VARCHAR(100),
    location POINT
);
```

---

## 21.2 Spatial Datatypes in Data Analysis

Spatial datatypes are useful for:

* Store location analysis
* Delivery route analysis
* Customer distance analysis
* Regional sales mapping
* Heatmaps
* Geographic segmentation

For beginner-level data analysis, latitude and longitude are often stored as `DECIMAL` or `DOUBLE`.

Example:

```sql
latitude DECIMAL(10,7)
longitude DECIMAL(10,7)
```

This is simpler for basic analysis.

---

# 22. Choosing the Right Datatype

Choosing the right datatype is not about memorizing syntax. It is about understanding the data.

Ask these questions before choosing a datatype:

1. Is the value a number, text, date, JSON, or location?
2. Can the value contain decimals?
3. Does the value need exact precision?
4. Can the value be negative?
5. How large can the value become?
6. Will this column be used in joins?
7. Will this column be used in filters?
8. Will this column be used in grouping?
9. Will this column be indexed?
10. Can the values change in future?

---

# 23. Practical Datatype Selection Table

| Data                 | Recommended Datatype        | Reason                                |
| -------------------- | --------------------------- | ------------------------------------- |
| Customer ID          | `INT UNSIGNED`              | Positive whole number                 |
| Large transaction ID | `BIGINT UNSIGNED`           | Very large number                     |
| Customer name        | `VARCHAR(100)`              | Variable text                         |
| Email                | `VARCHAR(255)`              | Variable text                         |
| Phone number         | `VARCHAR(20)`               | May contain `+`, spaces, leading zero |
| Age                  | `TINYINT UNSIGNED`          | Small positive number                 |
| Quantity             | `INT UNSIGNED`              | Positive whole number                 |
| Product price        | `DECIMAL(10,2)`             | Exact money value                     |
| Revenue              | `DECIMAL(12,2)`             | Exact financial value                 |
| Discount percentage  | `DECIMAL(5,2)`              | Exact percentage                      |
| Rating from 1 to 5   | `TINYINT UNSIGNED`          | Small whole number                    |
| Order date           | `DATE`                      | Date only                             |
| Order created time   | `DATETIME`                  | Date and time                         |
| Created at           | `TIMESTAMP`                 | System timestamp                      |
| Updated at           | `TIMESTAMP`                 | Auto-updated system timestamp         |
| Product description  | `TEXT`                      | Long text                             |
| Status               | `ENUM` or `VARCHAR`         | Depends on stability of values        |
| Is active            | `BOOLEAN`                   | True/false                            |
| JSON attributes      | `JSON`                      | Flexible structure                    |
| Latitude             | `DECIMAL(10,7)` or `DOUBLE` | Location value                        |
| Longitude            | `DECIMAL(10,7)` or `DOUBLE` | Location value                        |

---

# 24. Common Mistakes with MySQL Datatypes

## Mistake 1: Storing Dates as Text

Bad:

```sql
order_date VARCHAR(20)
```

Good:

```sql
order_date DATE
```

Why?

With `DATE`, you can easily perform:

```sql
YEAR(order_date)
MONTH(order_date)
DATEDIFF()
ORDER BY order_date
```

---

## Mistake 2: Storing Money as FLOAT

Bad:

```sql
price FLOAT
```

Good:

```sql
price DECIMAL(10,2)
```

Why?

Money needs exact precision.

---

## Mistake 3: Storing Phone Numbers as INT

Bad:

```sql
phone_number BIGINT
```

Good:

```sql
phone_number VARCHAR(20)
```

Why?

Phone numbers are not used for mathematical calculations. They may also contain:

* Country code
* Leading zero
* Spaces
* Plus sign
* Hyphens

Example:

```sql
+92 320 1234567
```

---

## Mistake 4: Using TEXT for Everything

Bad:

```sql
customer_name TEXT
email TEXT
city TEXT
```

Good:

```sql
customer_name VARCHAR(100)
email VARCHAR(255)
city VARCHAR(100)
```

Why?

`VARCHAR` is usually better for short and searchable text fields.

---

## Mistake 5: Using BIGINT for Every ID

Bad:

```sql
category_id BIGINT
```

Good:

```sql
category_id INT UNSIGNED
```

Why?

If the table will never have billions of categories, `BIGINT` is unnecessary.

---

## Mistake 6: Using ENUM for Values That Change Often

Bad:

```sql
city ENUM('Lahore', 'Karachi', 'Islamabad')
```

Good:

```sql
city_id INT
```

With a separate cities table:

```sql
CREATE TABLE cities (
    city_id INT,
    city_name VARCHAR(100)
);
```

Why?

Cities, departments, product categories, and similar lists can grow. A separate lookup table is more flexible.

---

# 25. Example: Good Table Design

```sql
CREATE TABLE customers (
    customer_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    phone_number VARCHAR(20),
    city VARCHAR(100),
    country VARCHAR(100),
    signup_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Why this is good:

* `customer_id` is numeric and auto-generated.
* `customer_name` uses `VARCHAR`.
* `email` uses `VARCHAR(255)`.
* `phone_number` uses `VARCHAR`, not number.
* `signup_date` uses `DATE`.
* `is_active` uses `BOOLEAN`.
* `created_at` uses `TIMESTAMP`.

---

# 26. Example: Sales Table for Data Analysis

```sql
CREATE TABLE sales (
    sale_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    customer_id INT UNSIGNED,
    product_id INT UNSIGNED,
    sale_date DATE,
    quantity INT UNSIGNED,
    unit_price DECIMAL(10,2),
    discount_amount DECIMAL(10,2),
    total_amount DECIMAL(12,2),
    payment_status ENUM('Paid', 'Pending', 'Refunded'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

This table is useful for analysis because:

* `sale_date` supports date analysis.
* `quantity` supports aggregation.
* `unit_price`, `discount_amount`, and `total_amount` use `DECIMAL`.
* `payment_status` keeps clean status values.
* `customer_id` and `product_id` can be used for joins.

---

# 27. Datatypes and Data Analysis Impact

## 27.1 Impact on Filtering

Correct datatype:

```sql
WHERE order_date >= '2026-01-01'
```

Wrong datatype:

```sql
WHERE order_date_text >= '01-01-2026'
```

Text dates can produce incorrect filtering.

---

## 27.2 Impact on Sorting

Correct numeric sorting:

```sql
1
2
10
20
```

Wrong text sorting:

```sql
1
10
2
20
```

If numbers are stored as text, sorting may become incorrect.

---

## 27.3 Impact on Grouping

Clean status values:

```sql
Paid
Pending
Refunded
```

Messy status values:

```sql
paid
Paid
PAID
payed
```

Wrong datatype or missing constraints can create messy grouping results.

---

## 27.4 Impact on Joins

Good:

```sql
customers.customer_id INT
orders.customer_id INT
```

Bad:

```sql
customers.customer_id INT
orders.customer_id VARCHAR(20)
```

Joining different datatypes can slow down queries and create matching issues.

---

# 28. Best Practices for MySQL Datatypes

1. Use `INT` for normal IDs.
2. Use `BIGINT` only for very large tables.
3. Use `DECIMAL` for money.
4. Use `DATE` for date-only values.
5. Use `DATETIME` for business date and time.
6. Use `TIMESTAMP` for created and updated tracking.
7. Use `VARCHAR` for normal text.
8. Use `TEXT` only for long descriptions.
9. Use `BOOLEAN` for true/false values.
10. Use `ENUM` only when values are fixed and stable.
11. Avoid `SET` for serious analytical structures.
12. Use `JSON` only for flexible or semi-structured data.
13. Do not store phone numbers as numbers.
14. Do not store dates as text.
15. Do not store money as `FLOAT`.
16. Keep join columns the same datatype.
17. Choose the smallest datatype that safely fits the data.
18. Avoid overusing large datatypes.
19. Think about future growth.
20. Think about reporting before designing columns.

---

# 29. Quick Revision Table

| Requirement                | Best Datatype           |
| -------------------------- | ----------------------- |
| Whole number               | `INT`                   |
| Very large whole number    | `BIGINT`                |
| Small number               | `TINYINT` or `SMALLINT` |
| Money                      | `DECIMAL`               |
| Approximate decimal        | `FLOAT` or `DOUBLE`     |
| Date only                  | `DATE`                  |
| Time only                  | `TIME`                  |
| Date and time              | `DATETIME`              |
| Created/updated timestamp  | `TIMESTAMP`             |
| Short text                 | `VARCHAR`               |
| Fixed-length code          | `CHAR`                  |
| Long text                  | `TEXT`                  |
| True/false                 | `BOOLEAN`               |
| Fixed status list          | `ENUM`                  |
| Multiple predefined values | `SET`                   |
| JSON document              | `JSON`                  |
| File/binary data           | `BLOB`                  |
| Location point             | `POINT`                 |

---

# 30. Final Summary

MySQL datatypes are the foundation of good database design and accurate data analysis.

A beginner may think datatypes are just technical details, but a serious analyst knows they directly affect:

* Accuracy of reports
* Speed of queries
* Cleanliness of data
* Correctness of joins
* Quality of dashboards
* Reliability of business decisions

The strongest rule is simple:

Choose the datatype based on how the data will be stored, filtered, grouped, joined, calculated, and reported.

Good datatype selection prevents future problems. Bad datatype selection creates messy analysis, wrong numbers, and wasted time.
