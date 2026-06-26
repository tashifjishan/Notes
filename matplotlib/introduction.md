# Introduction to Matplotlib

**Matplotlib** is an open-source Python library used to create data visualizations such as charts and graphs. It is easy to learn, highly flexible, and capable of creating almost any type of visualization by adjusting its various properties.

In this lecture series, we will study Matplotlib from the perspective of a **Data Analyst**. The focus will be on the concepts and features that are most useful for data analysis, while avoiding advanced topics that are generally unnecessary for everyday analytical work.

## Common Terms in Matplotlib

Before creating visualizations, it is important to understand these key terms:

### 1. Figure

A **Figure** is the entire canvas or blank page on which all visualizations are drawn. It serves as the top-level container for all plot elements.

### 2. Axes

An **Axes** is the area within a figure where the actual chart or graph is plotted. A single figure can contain one or multiple axes, allowing you to display multiple plots in the same figure.

### 3. Axis

An **Axis** refers to the horizontal (**X-axis**) or vertical (**Y-axis**) scale of an axes. It defines how data is measured and displayed.

### 4. Artists

**Artists** are all the visible elements in a Matplotlib figure. These include:

* Axes
* Axis labels
* Tick marks
* Lines
* Bars
* Text
* Legends
* Titles
* Markers

In short, almost everything you can see in a Matplotlib figure is considered an **Artist**.

---

### Visual Hierarchy

```
Figure
│
├── Axes (Plot Area)
│   ├── X-Axis
│   ├── Y-Axis
│   ├── Lines/Bars
│   ├── Titles
│   ├── Labels
│   └── Other Artists
│
└── Another Axes (Optional)
    ├── X-Axis
    ├── Y-Axis
    └── Artists
```

**Key Points to Remember**

* **Figure** = Complete canvas or window.
* **Axes** = The plotting area where graphs are drawn.
* **Axis** = The X-axis or Y-axis of a plot.
* **Artists** =In Matplotlib, every object that is rendered on a Figure is an Artist.
