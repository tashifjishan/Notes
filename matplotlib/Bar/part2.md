# Comprehensive Notes on Matplotlib Bar Charts

## 1. Introduction

A **bar chart** is a graph that represents **categorical data** using rectangular bars. The height (or length) of each bar represents the corresponding value.

Matplotlib provides two main functions for creating bar charts:

* `plt.bar()` → Vertical bar chart
* `plt.barh()` → Horizontal bar chart

Bar charts are useful for:

* Comparing categories
* Showing survey results
* Displaying sales data
* Comparing students' marks
* Population comparison
* Product analysis

---

# 2. Importing Matplotlib

```python
import matplotlib.pyplot as plt
```

If working with grouped bars:

```python
import numpy as np
```

---

# 3. Basic Syntax

## Vertical Bar Chart

```python
plt.bar(x, height)
```

### Parameters

| Parameter | Description             |
| --------- | ----------------------- |
| x         | Categories or positions |
| height    | Height of each bar      |
| width     | Width of bars           |
| color     | Fill color              |
| edgecolor | Border color            |
| linewidth | Border thickness        |
| align     | Alignment of bars       |
| alpha     | Transparency            |
| label     | Legend label            |
| bottom    | Starting point of bars  |
| hatch     | Pattern inside bars     |

---

## Horizontal Bar Chart

```python
plt.barh(y, width)
```

---

# 4. Creating a Simple Bar Chart

```python
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [82, 75, 95, 88]

plt.bar(students, marks)

plt.show()
```

Output:

```
|
|         █
|     █   █
| █   █   █
| █   █   █
+-------------
  A B C D
```

---

# 5. Bar Chart Components

A bar chart contains:

* Bars
* X-axis
* Y-axis
* Tick labels
* Title
* Legend (optional)
* Grid (optional)

---

# 6. Setting Title

```python
plt.title("Student Marks")
```

Example

```python
plt.bar(students, marks)
plt.title("Student Marks")
plt.show()
```

---

# 7. X-axis Label

```python
plt.xlabel("Students")
```

---

# 8. Y-axis Label

```python
plt.ylabel("Marks")
```

---

# 9. Complete Example

```python
plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
```

---

# 10. Changing Bar Color

Single color

```python
plt.bar(students, marks, color="red")
```

Common colors

```text
red
green
blue
yellow
orange
pink
purple
black
gray
brown
cyan
magenta
```

Hex color

```python
plt.bar(students, marks, color="#3498db")
```

RGB color

```python
plt.bar(students, marks,
        color=(0.2,0.6,0.8))
```

---

# 11. Multiple Colors

```python
colors = ["red","green","blue","orange"]

plt.bar(students,
        marks,
        color=colors)
```

Each bar gets a different color.

---

# 12. Width of Bars

Default width

```
0.8
```

Example

```python
plt.bar(students,
        marks,
        width=0.5)
```

Wider bars

```python
width=1
```

Narrow bars

```python
width=0.2
```

---

# 13. Edge Color

```python
plt.bar(students,
        marks,
        edgecolor="black")
```

---

# 14. Border Thickness

```python
plt.bar(students,
        marks,
        edgecolor="black",
        linewidth=2)
```

---

# 15. Transparency

Controlled using **alpha**.

```
0 = Invisible

1 = Fully visible
```

Example

```python
plt.bar(students,
        marks,
        alpha=0.5)
```

---

# 16. Aligning Bars

```python
plt.bar(x,
        y,
        align="center")
```

or

```python
align="edge"
```

---

# 17. Adding Grid

Horizontal grid

```python
plt.grid(axis="y")
```

Vertical grid

```python
plt.grid(axis="x")
```

Both

```python
plt.grid(True)
```

---

# 18. Changing Figure Size

```python
plt.figure(figsize=(8,5))
```

Width = 8 inches

Height = 5 inches

---

# 19. Horizontal Bar Chart

```python
plt.barh(students,
         marks)

plt.show()
```

Useful when category names are long.

---

# 20. Displaying Values on Bars

```python
bars = plt.bar(students,
               marks)

plt.bar_label(bars)

plt.show()
```

---

# 21. Formatting Labels

```python
bars = plt.bar(students, marks)

plt.bar_label(
    bars,
    fontsize=12,
    color="red"
)
```

---

# 22. Grouped (Multiple) Bar Chart

```python
import numpy as np

subjects=["Math","Science","English"]

boys=[78,82,90]
girls=[85,88,92]

x=np.arange(len(subjects))

width=0.35

plt.bar(x-width/2,
        boys,
        width,
        label="Boys")

plt.bar(x+width/2,
        girls,
        width,
        label="Girls")

plt.xticks(x,subjects)

plt.legend()

plt.show()
```

Output

```
██ ██
██ ██
██ ██
---------
Math
```

---

# 23. Stacked Bar Chart

```python
boys=[30,40,35]

girls=[20,25,30]

subjects=["Math","Science","English"]

plt.bar(subjects,boys)

plt.bar(subjects,
        girls,
        bottom=boys)

plt.show()
```

Second bars start from the top of the first bars.

---

# 24. Custom Tick Labels

```python
plt.xticks(rotation=45)
```

Rotate labels

```python
plt.xticks(rotation=90)
```

---

# 25. Tick Font Size

```python
plt.xticks(fontsize=12)

plt.yticks(fontsize=12)
```

---

# 26. Legend

```python
plt.legend()
```

Custom location

```python
plt.legend(loc="upper left")
```

Locations

```
upper right

upper left

lower left

lower right

center

best
```

---

# 27. Changing Axis Limits

Y-axis

```python
plt.ylim(0,100)
```

X-axis

```python
plt.xlim(-1,5)
```

---

# 28. Bar Patterns (Hatching)

```python
plt.bar(students,
        marks,
        hatch="//")
```

Patterns

```
/

//

\\

x

+

o

*

.
```

---

# 29. Error Bars

```python
errors=[2,3,4,2]

plt.bar(students,
        marks,
        yerr=errors)
```

---

# 30. Logarithmic Scale

```python
plt.yscale("log")
```

---

# 31. Saving the Figure

```python
plt.savefig("chart.png")
```

PDF

```python
plt.savefig("chart.pdf")
```

High quality

```python
plt.savefig("chart.png",
            dpi=300)
```

---

# 32. Complete Example

```python
import matplotlib.pyplot as plt

students=["A","B","C","D","E"]

marks=[80,75,92,88,79]

bars=plt.bar(
    students,
    marks,
    color="skyblue",
    edgecolor="black",
    linewidth=2
)

plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")

plt.grid(axis="y")

plt.bar_label(bars)

plt.show()
```

---

# 33. Important Bar Chart Parameters

| Parameter | Meaning          | Example     |
| --------- | ---------------- | ----------- |
| x         | Categories       | `["A","B"]` |
| height    | Values           | `[10,20]`   |
| width     | Bar width        | `0.5`       |
| color     | Fill color       | `"red"`     |
| edgecolor | Border           | `"black"`   |
| linewidth | Border thickness | `2`         |
| alpha     | Transparency     | `0.5`       |
| align     | Alignment        | `"center"`  |
| bottom    | Starting point   | `[10,20]`   |
| label     | Legend text      | `"Sales"`   |
| hatch     | Pattern          | `"//"`      |
| yerr      | Error bars       | `[2,3]`     |

---

# 34. Common Matplotlib Functions Used with Bar Charts

| Function          | Purpose                |
| ----------------- | ---------------------- |
| `plt.bar()`       | Vertical bar chart     |
| `plt.barh()`      | Horizontal bar chart   |
| `plt.title()`     | Add title              |
| `plt.xlabel()`    | Label x-axis           |
| `plt.ylabel()`    | Label y-axis           |
| `plt.legend()`    | Display legend         |
| `plt.grid()`      | Add grid               |
| `plt.xticks()`    | Customize x-axis ticks |
| `plt.yticks()`    | Customize y-axis ticks |
| `plt.bar_label()` | Add values to bars     |
| `plt.figure()`    | Set figure size        |
| `plt.savefig()`   | Save chart             |
| `plt.show()`      | Display chart          |

---

# 35. Advantages of Bar Charts

* Easy to understand.
* Effective for comparing categories.
* Supports vertical and horizontal layouts.
* Can display grouped and stacked data.
* Highly customizable (colors, labels, patterns, transparency, etc.).
* Suitable for business reports, dashboards, and presentations.

---

# 36. Limitations of Bar Charts

* Not ideal for continuous data (line charts or histograms are better).
* Too many categories can make the chart cluttered.
* Long category labels may overlap unless rotated or displayed in a horizontal chart.

---

# 37. Best Practices

* Keep category labels short and readable.
* Start the y-axis at zero for fair comparisons.
* Use contrasting colors that are easy to distinguish.
* Add axis labels, a title, and a legend when appropriate.
* Use `plt.bar_label()` to display exact values if helpful.
* Avoid excessive decorative effects that reduce readability.
* Use horizontal bar charts (`plt.barh()`) for long category names.
* Save figures with a high DPI (e.g., `dpi=300`) for reports and presentations.

These notes cover the essential concepts and most commonly used features for creating and customizing bar charts in Matplotlib, from basic plots to grouped, stacked, and fully styled visualizations.
