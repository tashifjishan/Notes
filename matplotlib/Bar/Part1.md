# `plt.bar()` Parameters – Comprehensive Reference

## Syntax

```python
plt.bar(
    x,
    height,
    width=0.8,
    bottom=None,
    align='center',
    *,
    color=None,
    edgecolor=None,
    linewidth=None,
    tick_label=None,
    xerr=None,
    yerr=None,
    ecolor=None,
    capsize=None,
    error_kw=None,
    label=None,
    hatch=None,
    alpha=None,
    zorder=None,
    log=False,
    **kwargs
)
```

---

# Complete Parameter Table

| Parameter      | Purpose (What)                                    | How It Works                                                              | Accepted Values                                              | Default                  | Example                         |
| -------------- | ------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------ | ------------------------------- |
| **x**          | Specifies the x-position or category of each bar. | Determines where bars are drawn on the x-axis.                            | List, tuple, NumPy array, Pandas Series, categorical strings | Required                 | `["A","B","C"]`, `[1,2,3]`      |
| **height**     | Specifies the height of each bar.                 | Controls the vertical size of every bar.                                  | List, tuple, array, Series, scalar                           | Required                 | `[20,35,40]`                    |
| **width**      | Sets the width of bars.                           | Larger values create wider bars; smaller values create thinner bars.      | Float, int, array-like                                       | `0.8`                    | `0.5`                           |
| **bottom**     | Sets the starting y-coordinate of bars.           | Bars begin from this value instead of zero. Used mainly for stacked bars. | Scalar, list, tuple, array                                   | `0`                      | `bottom=10`, `bottom=[5,10,15]` |
| **align**      | Controls horizontal alignment of bars.            | Determines whether x-values refer to the center or left edge of bars.     | `"center"`, `"edge"`                                         | `"center"`               | `align="edge"`                  |
| **color**      | Sets the fill color of bars.                      | One color for all bars or different colors for each bar.                  | Color name, hex code, RGB(A) tuple, list of colors           | Default Matplotlib color | `"red"`, `"#FF5733"`            |
| **edgecolor**  | Sets the border color.                            | Colors the outline of each bar.                                           | Color specification or list                                  | None                     | `"black"`                       |
| **linewidth**  | Sets border thickness.                            | Larger values produce thicker outlines.                                   | Float, int                                                   | Matplotlib default       | `2`                             |
| **tick_label** | Custom labels for x-axis ticks.                   | Overrides automatic tick labels.                                          | List of strings                                              | None                     | `["One","Two","Three"]`         |
| **xerr**       | Horizontal error bars.                            | Draws uncertainty in x-direction. Rarely used for vertical bars.          | Scalar, array-like                                           | None                     | `xerr=2`                        |
| **yerr**       | Vertical error bars.                              | Draws uncertainty in y-values.                                            | Scalar, list, array                                          | None                     | `yerr=[2,3,1]`                  |
| **ecolor**     | Error bar color.                                  | Changes color of error bars only.                                         | Color specification                                          | Default error bar color  | `"red"`                         |
| **capsize**    | Length of error bar caps.                         | Adds horizontal caps to error bars.                                       | Float, int                                                   | `0`                      | `5`                             |
| **error_kw**   | Additional error bar settings.                    | Dictionary passed to the error bar drawing routine.                       | Dictionary                                                   | `{}`                     | `{"elinewidth":2}`              |
| **label**      | Legend label.                                     | Used by `plt.legend()`.                                                   | String                                                       | None                     | `"Sales"`                       |
| **hatch**      | Fills bars with patterns.                         | Adds texture inside bars.                                                 | Pattern string                                               | None                     | `"//"`                          |
| **alpha**      | Transparency.                                     | 0 = transparent, 1 = opaque.                                              | Float (0–1)                                                  | `1`                      | `0.5`                           |
| **zorder**     | Drawing order.                                    | Higher values appear on top of lower values.                              | Integer, float                                               | Determined automatically | `5`                             |
| **log**        | Uses logarithmic y-axis.                          | Displays y-axis on a log scale.                                           | `True`, `False`                                              | `False`                  | `log=True`                      |
| **kwargs**     | Additional rectangle properties.                  | Passed to each bar (Rectangle object).                                    | Various keyword arguments                                    | None                     | `linestyle="--"`                |

---

# Detailed Explanation of Each Parameter

---

# 1. x

## Purpose

Determines the location of every bar.

```python
students = ["A", "B", "C"]
```

```python
plt.bar(students, [80,90,70])
```

Can also use numeric positions.

```python
plt.bar([1,2,3], [80,90,70])
```

Accepted values

* List
* Tuple
* NumPy array
* Pandas Series
* Strings
* Numeric values

---

# 2. height

Determines how tall each bar is.

```python
plt.bar(["A","B"], [10,20])
```

Bar heights

```
B → 20

A → 10
```

Accepted values

* List
* Tuple
* NumPy array
* Pandas Series
* Scalar

---

# 3. width

Controls bar thickness.

```python
plt.bar(x, y, width=0.4)
```

Examples

```
width=0.2   Very thin

width=0.5   Medium

width=0.8   Default

width=1.2   Wide
```

Can also be different for each bar.

```python
width=[0.2,0.4,0.6]
```

---

# 4. bottom

Changes where bars begin.

Normally

```
0
│
│████
│████
```

```python
bottom=20
```

Now

```
20
│████
│████
```

Useful for stacked bars.

```python
plt.bar(months, online)

plt.bar(months,
        offline,
        bottom=online)
```

Accepted values

* Scalar
* List
* NumPy array

Length must equal the number of bars when using a sequence.

---

# 5. align

Two choices.

### center

```
      x

   █████
```

```python
align="center"
```

Default.

---

### edge

```
x█████
```

```python
align="edge"
```

---

# 6. color

Changes fill color.

Single color

```python
color="red"
```

Different colors

```python
color=["red","green","blue"]
```

Accepted formats

```
Named colors

"red"

"blue"

"green"

Hex

"#3498db"

RGB

(0.3,0.6,0.8)

RGBA

(0.3,0.6,0.8,0.5)
```

---

# 7. edgecolor

Border color.

```python
edgecolor="black"
```

Different border colors

```python
edgecolor=["red","blue","green"]
```

---

# 8. linewidth

Border thickness.

```python
linewidth=3
```

```
0.5 Thin

1 Normal

3 Thick

6 Very Thick
```

---

# 9. tick_label

Changes displayed category labels.

Without

```
0 1 2
```

With

```python
tick_label=["Math","Science","English"]
```

Displays

```
Math

Science

English
```

---

# 10. xerr

Horizontal error bars.

Mostly useful for horizontal bar charts.

```python
xerr=2
```

or

```python
xerr=[2,3,1]
```

---

# 11. yerr

Vertical error bars.

```python
yerr=[3,2,4]
```

Produces

```
|
|
████
 |
```

---

# 12. ecolor

Changes only error bar color.

```python
ecolor="red"
```

---

# 13. capsize

Controls cap length.

```
|

```

vs.

```
----
 |

----
```

Example

```python
capsize=5
```

---

# 14. error_kw

Dictionary of extra error bar options.

```python
error_kw={
    "elinewidth":3,
    "capthick":2
}
```

Common keys include:

| Key          | Meaning                 |
| ------------ | ----------------------- |
| `elinewidth` | Width of error bar line |
| `capthick`   | Thickness of cap        |
| `alpha`      | Transparency            |
| `ecolor`     | Error bar color         |

---

# 15. label

Legend text.

```python
plt.bar(x,
        y,
        label="Sales")
```

Then

```python
plt.legend()
```

---

# 16. hatch

Pattern inside the bar.

Common values

```
"/"

"//"

"\\"

"x"

"+"

"*"

"."

"o"

"O"

"-"

"|"
```

Example

```python
hatch="//"
```

---

# 17. alpha

Transparency.

```
0 Invisible

0.2 Very transparent

0.5 Semi-transparent

1 Fully visible
```

Example

```python
alpha=0.7
```

---

# 18. zorder

Determines drawing order.

Higher values appear above lower values.

```python
zorder=5
```

Useful when bars overlap with grids, lines, or annotations.

---

# 19. log

Uses a logarithmic y-axis.

```python
log=True
```

Useful when values differ by several orders of magnitude, for example:

```
10

100

1000

10000
```

instead of a linear scale.

---

# 20. **kwargs (Rectangle Properties)

Each bar is a `Rectangle` object, so you can pass additional rectangle styling options.

Some commonly used properties are:

| Property      | Description                                  | Example                 |
| ------------- | -------------------------------------------- | ----------------------- |
| `linestyle`   | Border style                                 | `"--"`                  |
| `fill`        | Fill the rectangle or not                    | `False`                 |
| `joinstyle`   | Corner style                                 | `"round"`               |
| `antialiased` | Smooth edges                                 | `True`                  |
| `visible`     | Show or hide bars                            | `False`                 |
| `gid`         | Graphic ID                                   | `"bar1"`                |
| `picker`      | Enable picking (interactive plots)           | `True`                  |
| `url`         | Associate a URL (supported by some backends) | `"https://example.com"` |

Example:

```python
plt.bar(
    x,
    y,
    edgecolor="black",
    linestyle="--",
    fill=True
)
```

---

# Quick Summary Table

| Parameter    | Required | Most Common Values      |
| ------------ | -------- | ----------------------- |
| `x`          | ✅        | Categories or positions |
| `height`     | ✅        | Heights of bars         |
| `width`      | ❌        | `0.8`, `0.5`            |
| `bottom`     | ❌        | `0`, list, array        |
| `align`      | ❌        | `"center"`, `"edge"`    |
| `color`      | ❌        | `"red"`, `"#3498db"`    |
| `edgecolor`  | ❌        | `"black"`               |
| `linewidth`  | ❌        | `1`, `2`, `3`           |
| `tick_label` | ❌        | List of strings         |
| `xerr`       | ❌        | Number or list          |
| `yerr`       | ❌        | Number or list          |
| `ecolor`     | ❌        | Color                   |
| `capsize`    | ❌        | `5`, `10`               |
| `error_kw`   | ❌        | Dictionary              |
| `label`      | ❌        | String                  |
| `hatch`      | ❌        | `"//"`, `"x"`, `"*"`    |
| `alpha`      | ❌        | `0`–`1`                 |
| `zorder`     | ❌        | Integer                 |
| `log`        | ❌        | `True`, `False`         |
| `**kwargs`   | ❌        | Rectangle properties    |

This table covers the full public API of `plt.bar()` along with the purpose, behavior, accepted values, defaults, and practical examples for each parameter.
