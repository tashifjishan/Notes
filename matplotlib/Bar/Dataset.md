Here are several sample datasets you can use to practice **Matplotlib bar charts**.

---

# Dataset 1: Student Marks

```python
students = ["A", "B", "C", "D", "E", "F"]
marks = [85, 72, 90, 68, 95, 80]
```

| Student | Marks |
| ------- | ----: |
| A       |    85 |
| B       |    72 |
| C       |    90 |
| D       |    68 |
| E       |    95 |
| F       |    80 |

---

# Dataset 2: Monthly Sales

```python
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [25000, 30000, 28000, 35000, 40000, 38000]
```

| Month | Sales |
| ----- | ----: |
| Jan   | 25000 |
| Feb   | 30000 |
| Mar   | 28000 |
| Apr   | 35000 |
| May   | 40000 |
| Jun   | 38000 |

---

# Dataset 3: Product Sales

```python
products = ["Laptop", "Phone", "Tablet", "Printer", "Monitor"]
quantity = [120, 250, 95, 60, 140]
```

| Product | Quantity |
| ------- | -------: |
| Laptop  |      120 |
| Phone   |      250 |
| Tablet  |       95 |
| Printer |       60 |
| Monitor |      140 |

---

# Dataset 4: Population of Cities (in Lakhs)

```python
cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru"]
population = [320, 205, 150, 115, 140]
```

| City      | Population |
| --------- | ---------: |
| Delhi     |        320 |
| Mumbai    |        205 |
| Kolkata   |        150 |
| Chennai   |        115 |
| Bengaluru |        140 |

---

# Dataset 5: Company Revenue (Million ₹)

```python
companies = ["TCS", "Infosys", "Wipro", "HCL", "Tech Mahindra"]
revenue = [210, 165, 135, 170, 110]
```

| Company       | Revenue |
| ------------- | ------: |
| TCS           |     210 |
| Infosys       |     165 |
| Wipro         |     135 |
| HCL           |     170 |
| Tech Mahindra |     110 |

---

# Dataset 6: Subject-wise Average Marks

```python
subjects = ["Math", "Science", "English", "Computer", "History"]
average_marks = [84, 79, 88, 91, 76]
```

| Subject  | Average Marks |
| -------- | ------------: |
| Math     |            84 |
| Science  |            79 |
| English  |            88 |
| Computer |            91 |
| History  |            76 |

---

# Dataset 7: Employee Salary (₹)

```python
employees = ["Rahul", "Priya", "Amit", "Neha", "Karan"]
salary = [45000, 52000, 47000, 58000, 50000]
```

| Employee | Salary |
| -------- | -----: |
| Rahul    |  45000 |
| Priya    |  52000 |
| Amit     |  47000 |
| Neha     |  58000 |
| Karan    |  50000 |

---

# Dataset 8: Mobile Brand Sales

```python
brands = ["Samsung", "Apple", "Xiaomi", "OnePlus", "Vivo"]
sales = [350, 290, 260, 180, 220]
```

| Brand   | Units Sold |
| ------- | ---------: |
| Samsung |        350 |
| Apple   |        290 |
| Xiaomi  |        260 |
| OnePlus |        180 |
| Vivo    |        220 |

---

# Dataset 9: Daily Website Visitors

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
visitors = [550, 620, 700, 650, 800, 950, 900]
```

| Day | Visitors |
| --- | -------: |
| Mon |      550 |
| Tue |      620 |
| Wed |      700 |
| Thu |      650 |
| Fri |      800 |
| Sat |      950 |
| Sun |      900 |

---

# Dataset 10: Olympic Medals

```python
countries = ["USA", "China", "Japan", "India", "Australia"]
medals = [126, 91, 58, 18, 53]
```

| Country   | Medals |
| --------- | -----: |
| USA       |    126 |
| China     |     91 |
| Japan     |     58 |
| India     |     18 |
| Australia |     53 |

---

# Dataset 11: Grouped Bar Chart Dataset

```python
subjects = ["Math", "Science", "English", "Computer"]

boys = [78, 85, 82, 90]
girls = [84, 88, 87, 94]
```

| Subject  | Boys | Girls |
| -------- | ---: | ----: |
| Math     |   78 |    84 |
| Science  |   85 |    88 |
| English  |   82 |    87 |
| Computer |   90 |    94 |

---

# Dataset 12: Stacked Bar Chart Dataset

```python
months = ["Jan", "Feb", "Mar", "Apr"]

online_sales = [120, 150, 180, 200]
offline_sales = [90, 100, 120, 130]
```

| Month | Online | Offline |
| ----- | -----: | ------: |
| Jan   |    120 |      90 |
| Feb   |    150 |     100 |
| Mar   |    180 |     120 |
| Apr   |    200 |     130 |

---

## Complete Example Using Dataset

```python
import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Tablet", "Printer", "Monitor"]
quantity = [120, 250, 95, 60, 140]

plt.figure(figsize=(8,5))

plt.bar(
    products,
    quantity,
    color="skyblue",
    edgecolor="black"
)

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Units Sold")
plt.grid(axis="y")

plt.show()
```

These datasets cover common practice scenarios for **basic**, **horizontal**, **grouped**, and **stacked** bar charts.
