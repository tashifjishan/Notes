Perfect. Let's use a **real-world problem** that companies actually solve.

---

# Practical Example: Predicting House Prices

Suppose you're building a model for a real estate website.

Instead of using only the house area, you use multiple features.

| House | Area (sq ft) | Bedrooms | Age (years) | Distance to City (km) | Price ($1000s) |
| ----- | -----------: | -------: | ----------: | --------------------: | -------------: |
| 1     |         1200 |        2 |          10 |                    15 |            250 |
| 2     |         1500 |        3 |           5 |                    10 |            340 |
| 3     |         1800 |        4 |           2 |                     8 |            420 |
| 4     |         1000 |        2 |          20 |                    25 |            180 |

Notice that **price depends on several things at once**.

---

# Step 1: Write the Model

Instead of

[
y = wx + b
]

we now have

[
\hat y =
w_1(\text{Area})
+
w_2(\text{Bedrooms})
+
w_3(\text{Age})
+
w_4(\text{Distance})
+
b
]

For example,

```
Predicted Price =
w₁ × Area
+ w₂ × Bedrooms
+ w₃ × Age
+ w₄ × Distance
+ b
```

Each weight tells us how much that feature contributes.

---

# Step 2: Represent the Data as a Matrix

Instead of storing every feature separately, we put everything into one matrix.

[
X=
\begin{bmatrix}
1200 & 2 & 10 & 15\
1500 & 3 & 5 & 10\
1800 & 4 & 2 & 8\
1000 & 2 & 20 & 25
\end{bmatrix}
]

Each **row** is one house.

Each **column** is one feature.

Think of it like a spreadsheet:

```
            Features
        A     B     C     D
House1 1200   2    10    15
House2 1500   3     5    10
House3 1800   4     2     8
House4 1000   2    20    25
```

---

# Step 3: The Weight Vector

Instead of one weight, we now have one weight per feature.

[
w=
\begin{bmatrix}
0.15\
20\
-1.5\
-3
\end{bmatrix}
]

Interpretation:

* Area contributes **+$0.15k** per square foot.
* Each extra bedroom adds **$20k**.
* Every additional year of age reduces value by **$1.5k**.
* Every extra kilometer from the city reduces value by **$3k**.

---

# Step 4: Predict Every House at Once

Instead of computing each prediction separately:

```text
House 1
1200*w1 + 2*w2 + ...

House 2
1500*w1 + 3*w2 + ...

House 3
...
```

we do **one matrix multiplication**:

[
\hat y = Xw + b
]

This produces predictions for every house simultaneously.

Let's compute the first house manually:

```
Area contribution
1200 × 0.15 = 180

Bedrooms
2 × 20 = 40

Age
10 × (-1.5) = -15

Distance
15 × (-3) = -45

Bias
+100
```

Suppose the bias is **100**.

Then

```
180
+40
-15
-45
+100
-------
260
```

Predicted price:

```
$260,000
```

The computer performs the same calculation for every row of (X).

---

# Step 5: The Actual Prices

[
y=
\begin{bmatrix}
250\
340\
420\
180
\end{bmatrix}
]

---

# Step 6: The Closed-Form Solution

To find the best weights, we solve

[
\theta=(X^TX)^{-1}X^Ty
]

Here's what each part means.

### (X)

The original data:

```
4 houses × 4 features
```

---

### (X^T)

Transpose the matrix.

Rows become columns.

```
Features × Houses
```

---

### (X^TX)

Now something interesting happens.

The result is **not predictions**.

Instead, it's a matrix that summarizes how the features relate to each other.

For our example, its shape is:

```
4 × 4
```

It contains quantities like:

* Area × Area
* Area × Bedrooms
* Area × Age
* Bedrooms × Distance

This captures the relationships among the input features.

---

### Why Do We Invert It?

Suppose:

* Bigger houses usually have more bedrooms.
* Houses farther from the city tend to be older.

These feature relationships mean we can't estimate each weight independently. The inverse helps disentangle their combined effects so that each weight reflects the contribution of its own feature while accounting for the others.

Finally,

[
(X^TX)^{-1}X^Ty
]

produces the weight vector

[
\theta=
\begin{bmatrix}
w_1\
w_2\
w_3\
w_4
\end{bmatrix}
]

---

# What Happens with 100 Features?

Now imagine Zillow has:

* Area
* Bedrooms
* Bathrooms
* Lot size
* School rating
* Crime rate
* Nearby parks
* Garage size
* Energy rating
* Property tax
* ...

Suppose there are **100 features**.

Then:

```
X
=
1,000,000 houses
×
100 features
```

The matrix dimensions are:

```
X       = 1,000,000 × 100
Xᵀ      =       100 × 1,000,000
XᵀX     =       100 × 100
```

A **100 × 100** inverse is still quite manageable on modern computers.

---

# So when does the matrix inverse become a problem?

The bottleneck isn't usually the **number of houses**. It's the **number of features**.

Imagine a text-classification model where each unique word is a feature.

```
Vocabulary size = 500,000 words
```

Now:

```
X
=
5,000,000 documents
×
500,000 features
```

The normal equation requires

```
XᵀX
=
500,000 × 500,000
```

That matrix has:

```
500,000 × 500,000
=
250,000,000,000
```

entries (250 **billion**).

Just storing that matrix would require an enormous amount of memory, and inverting it is computationally very expensive.

Gradient descent avoids ever forming or inverting (X^TX). Instead, it repeatedly adjusts the weights based on the prediction errors, making it practical for very high-dimensional problems.

---

## Key takeaway

The normal equation is an excellent choice when:

* The model is **linear regression**.
* The number of features is relatively small (tens or a few hundreds).

Gradient descent becomes the practical choice when:

* There are **thousands or millions of features**.
* The model is **not linear** (e.g., logistic regression, neural networks).
* The dataset is too large or complex for a direct matrix solution.

This distinction is why you'll still see the normal equation taught in statistics and introductory machine learning, while modern machine learning systems almost always rely on gradient-based optimization.
