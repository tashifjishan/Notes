# Bar Chart Notes (Matplotlib) – Data Analysis Course

These notes cover **everything a beginner to intermediate data analysis student should know** about bar charts in Matplotlib. Topics that are mainly used in research or advanced visualization (such as hatching, logarithmic scales, asymmetric error bars, etc.) are intentionally omitted.

---

# 1. What is a Bar Chart?

A **bar chart** is a graph used to compare values across different **categories**.

Each category is represented by a **rectangular bar**, and the **height (or length)** of the bar represents the corresponding value.

### Example

| Product | Sales |
| ------- | ----: |
| Laptop  |   120 |
| Mobile  |   180 |
| Tablet  |    90 |
| Watch   |   140 |

A bar chart helps answer questions like:

* Which product sold the most?
* Which product sold the least?
* How much difference exists between products?

---

# 2. When Should You Use a Bar Chart?

Use a bar chart when:

* Comparing categories
* Comparing counts
* Comparing averages
* Comparing totals

### Examples

* Student marks
* Monthly sales by product
* Population of cities
* Number of employees in departments
* Average salary by profession

---

# 3. When NOT to Use a Bar Chart

Avoid a bar chart when:

* Showing trends over time (use a Line Chart)
* Showing relationships between two numerical variables (use a Scatter Plot)
* Showing distributions (use a Histogram)

---

# 4. Basic Syntax

```python
plt.bar(x, height)
```

where

* `x` → Categories
* `height` → Values

Example

```python
import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet"]
sales = [120, 180, 90]

plt.bar(products, sales)

plt.show()
```

---

# 5. Understanding the Parameters

## (1) x

Specifies the category names or x-axis positions.

```python
products = ["A", "B", "C"]

plt.bar(products, sales)
```

Output

```
A   B   C
```

---

## (2) height

Specifies the value of each bar.

```python
sales = [120, 150, 90]
```

Bar heights become

```
120
150
90
```

---

## (3) width

Controls the width of each bar.

Default

```python
width=0.8
```

Narrow bars

```python
plt.bar(products, sales, width=0.4)
```

Wide bars

```python
plt.bar(products, sales, width=0.9)
```

---

## (4) color

Changes the fill color.

Single color

```python
plt.bar(products, sales, color="steelblue")
```

Different colors

```python
colors = ["red", "green", "blue"]

plt.bar(products, sales, color=colors)
```

---

## (5) edgecolor

Adds borders around bars.

```python
plt.bar(
    products,
    sales,
    edgecolor="black"
)
```

---

## (6) linewidth

Changes border thickness.

```python
plt.bar(
    products,
    sales,
    edgecolor="black",
    linewidth=2
)
```

---

## (7) alpha

Controls transparency.

Range

```
0 → Invisible

1 → Fully visible
```

Example

```python
plt.bar(
    products,
    sales,
    alpha=0.7
)
```

---

## (8) label

Used for legends.

```python
plt.bar(
    products,
    sales,
    label="Sales"
)

plt.legend()
```

---

# 6. Adding Titles and Labels

Title

```python
plt.title("Product Sales")
```

X-axis

```python
plt.xlabel("Products")
```

Y-axis

```python
plt.ylabel("Sales")
```

Example

```python
plt.title("Monthly Sales")
plt.xlabel("Products")
plt.ylabel("Units Sold")
```

---

# 7. Changing Figure Size

```python
plt.figure(figsize=(8,5))
```

Width = 8 inches

Height = 5 inches

---

# 8. Adding Grid

```python
plt.grid(axis="y")
```

Dashed grid

```python
plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)
```

---

# 9. Adding Values on Bars

Very useful in reports.

```python
bars = plt.bar(products, sales)

for bar in bars:

    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),

        bar.get_height(),

        ha="center",
        va="bottom"
    )
```

Result

```
      180
       █
120 █  █
```

---

# 10. Horizontal Bar Chart

Instead of

```python
plt.bar()
```

use

```python
plt.barh()
```

Example

```python
students = ["Alice", "Bob", "Charlie"]

marks = [78, 90, 68]

plt.barh(
    students,
    marks
)
```

Useful when category names are long.

---

# 11. Error Bars (Basic)

Sometimes the value shown is an average of multiple observations.

Example

| Student | Average | SD |
| ------- | ------: | -: |
| Alice   |      80 |  2 |
| Bob     |      90 |  3 |
| Charlie |      70 |  1 |

Error bars show the variability.

```python
means = [80,90,70]

std = [2,3,1]

plt.bar(
    ["Alice","Bob","Charlie"],
    means,

    yerr=std,

    capsize=5,

    ecolor="red"
)
```

Useful parameters

```python
yerr
```

Size of error

```python
capsize
```

Width of cap

```python
ecolor
```

Color of error bar

---

# 12. Complete Example

```python
import matplotlib.pyplot as plt

products = ["Laptop", "Mobile", "Tablet", "Watch"]

sales = [120, 180, 90, 140]

plt.figure(figsize=(8,5))

bars = plt.bar(
    products,
    sales,

    color="skyblue",

    edgecolor="black",

    linewidth=1.5,

    alpha=0.8,

    width=0.6,

    label="Sales"
)

for bar in bars:

    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),

        f"{bar.get_height()}",

        ha="center",
        va="bottom"
    )

plt.title("Product Sales")

plt.xlabel("Products")

plt.ylabel("Units Sold")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.legend()

plt.show()
```

---

# 13. Commonly Used `plt.bar()` Parameters

| Parameter   | Purpose                 |
| ----------- | ----------------------- |
| `x`         | Categories on x-axis    |
| `height`    | Height of each bar      |
| `width`     | Width of bars           |
| `color`     | Fill color              |
| `edgecolor` | Border color            |
| `linewidth` | Border thickness        |
| `alpha`     | Transparency            |
| `label`     | Legend label            |
| `yerr`      | Error bars              |
| `capsize`   | Width of error bar caps |
| `ecolor`    | Error bar color         |

---

# 14. Best Practices

* Give every chart a meaningful title.
* Label both axes clearly.
* Use colors consistently.
* Do not use too many bright colors in one chart.
* Add value labels when presenting data.
* Keep the chart simple and uncluttered.
* Use horizontal bar charts (`barh`) for long category names.
* Use error bars only when the values represent averages or estimates.

---

# 15. Practice Exercises

1. Create a bar chart showing the marks of five students.
2. Change the bar color to green.
3. Add black borders with a thickness of 2.
4. Reduce the bar width to 0.5.
5. Add chart title and axis labels.
6. Display the marks above each bar.
7. Add a legend.
8. Draw a horizontal bar chart for the same data.
9. Create a bar chart with error bars using average marks and standard deviations.
10. Combine all of the above into one polished visualization.

