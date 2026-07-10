# Basic to Intermediate: 




| Purpose | Chart Type | Matplotlib Function | Seaborn Function | Teaching Focus / Core Concept |
| --- | --- | --- | --- | --- |
| **Trends** | **Line Plot** | `plt.plot()` | `sns.lineplot()` | Tracking changes over time (intervals/dates). |
| **Comparisons** | **Standard Bar Chart** | `plt.bar()` | `sns.barplot()` | Comparing quantities across discrete categories. |
|  | **Count Plot** | *N/A (Requires manual manual counting via Pandas)* | `sns.countplot()` | Crucial beginner shortcut: automatically counts and plots categorical frequencies. |
| **Distributions** | **Histogram** | `plt.hist()` | `sns.histplot()` | Understanding data distribution, skewness, and frequency. |
|  | **KDE Plot** | *N/A* | `sns.kdeplot()` | Smooth, continuous probability density curve (great alternative to histogram). |
|  | **Box Plot** | `plt.boxplot()` | `sns.boxplot()` | Visualizing five-number summary and spotting outliers. |
|  | **Violin Plot** | `plt.violinplot()` | `sns.violinplot()` | Combining a box plot with a density plot for richer distribution views. |
| **Relationships** | **Scatter Plot** | `plt.scatter()` | `sns.scatterplot()` | Investigating correlation and patterns between two continuous variables. |
|  | **Regression Plot** | *N/A (Requires `numpy.polyfit` calculations)* | `sns.regplot()` | Automatically plots a scatter plot *plus* a linear regression trend line. |
| **Multivariate (EDA)** | **Heatmap** | `plt.imshow()` *(clunky for tabular data)* | `sns.heatmap()` | Best for visualizing correlation matrices (`df.corr()`) using color scales. |
|  | **Pair Plot** | *N/A* | `sns.pairplot()` | The ultimate EDA tool to view all pairwise relationships in a dataset at once. |

---

### 💡 Curriculum Design Tip for this Table:

* **The "N/A" rows are teaching goldmines:** When you get to charts like the **Count Plot**, **Regression Plot**, or **Pair Plot**, show students how many lines of code it takes to build them in Matplotlib versus just *one line* in Seaborn. It perfectly drives home *why* data analysts use Seaborn for fast data exploration.
* **Variations to mention, not teach separately:** You don't need new rows for Horizontal, Grouped, or Stacked bars. Just teach them as arguments (e.g., passing `orientation='h'` in Matplotlib or adding a `hue` parameter in Seaborn).

# A lil overkill: 

| Chart Type           | Matplotlib | Seaborn | Purpose                                        |
| -------------------- | ---------- | ------- | ---------------------------------------------- |
| Line Plot            | ✓          | ✓       | Show trends over time                          |
| Bar Chart            | ✓          | ✓       | Compare categories                             |
| Horizontal Bar Chart | ✓          | ✓       | Compare long category names                    |
| Grouped Bar Chart    | ✓          | ✓       | Compare multiple groups                        |
| Stacked Bar Chart    | ✓          | Limited | Show composition                               |
| Pie Chart            | ✓          | —       | Show proportions                               |
| Histogram            | ✓          | ✓       | Display frequency distribution                 |
| Box Plot             | ✓          | ✓       | Detect spread and outliers                     |
| Violin Plot          | —          | ✓       | Show distribution and density                  |
| Scatter Plot         | ✓          | ✓       | Show relationship between variables            |
| Bubble Chart         | ✓          | ✓       | Scatter plot with varying marker sizes         |
| Area Chart           | ✓          | —       | Show cumulative trends                         |
| Stacked Area Chart   | ✓          | —       | Compare changing compositions over time        |
| Heatmap              | Basic      | ✓       | Visualize matrices and correlations            |
| Pair Plot            | —          | ✓       | Explore relationships among multiple variables |
| Joint Plot           | —          | ✓       | Relationship plus distributions                |
| KDE (Density) Plot   | —          | ✓       | Estimate probability density                   |
| Rug Plot             | —          | ✓       | Display individual observations                |
| Strip Plot           | —          | ✓       | Show distribution of individual data points    |
| Swarm Plot           | —          | ✓       | Non-overlapping categorical scatter plot       |
| Count Plot           | —          | ✓       | Display counts of categories                   |
| ECDF Plot            | —          | ✓       | Empirical cumulative distribution              |
| Regression Plot      | —          | ✓       | Scatter plot with regression line              |
| Residual Plot        | —          | ✓       | Evaluate regression errors                     |
| Cluster Map          | —          | ✓       | Hierarchical clustering visualization          |
