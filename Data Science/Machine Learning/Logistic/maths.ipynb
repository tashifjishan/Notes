Definitely. In fact, I think this is the **best way** to understand logistic regression. We'll solve it exactly like we did with linear regression, except this time we'll use **gradient descent** because there is no closed-form solution.

We'll do **one complete iteration** by hand.

---

# Problem

Suppose we have this dataset:

| Hours Studied ($x$) | Passed ($y$) |
|---------------------|--------------|
| 1 | 0 |
| 2 | 0 |
| 3 | 1 |

We want to learn a model that predicts whether a student passes.

---

# Step 1: Initialize the Parameters

Let's start with:

```python
w = 0
b = 0
learning_rate = 0.1
```

---

# Step 2: Compute $z$

The linear part of logistic regression is

$$
z = wx + b
$$

For each student:

| $x$ | Calculation | $z$ |
|-----|-------------|-----|
| 1 | $0 \times 1 + 0$ | 0 |
| 2 | $0 \times 2 + 0$ | 0 |
| 3 | $0 \times 3 + 0$ | 0 |

---

# Step 3: Apply the Sigmoid Function

The prediction is given by the sigmoid function:

$$
p = \sigma(z) = \frac{1}{1 + e^{-z}}
$$

For $z = 0$,

$$
p = \frac{1}{1 + e^0}
= \frac{1}{2}
= 0.5
$$

So every prediction is:

| $x$ | Actual ($y$) | Prediction ($p$) |
|-----|--------------|------------------|
| 1 | 0 | 0.5 |
| 2 | 0 | 0.5 |
| 3 | 1 | 0.5 |

---

# Step 4: Compute the Cross-Entropy Loss

The loss for one sample is

$$
L = -\left(y \log(p) + (1-y)\log(1-p)\right)
$$

Let's compute the loss for each sample.

---

## Sample 1

Actual = 0

Prediction = 0.5

$$
L_1
=
-\left(0\log(0.5)+1\log(0.5)\right)
$$

$$
= -\log(0.5)
$$

$$
= 0.6931
$$

---

## Sample 2

Exactly the same.

$$
L_2 = 0.6931
$$

---

## Sample 3

Actual = 1

Prediction = 0.5

$$
L_3
=
-\left(1\log(0.5)\right)
$$

$$
= 0.6931
$$

---

The average loss is

$$
\frac{0.6931 + 0.6931 + 0.6931}{3}
=
0.6931
$$

This is our starting error.

---

# Step 5: Compute the Gradients

After differentiating the cost function (using the chain rule and the derivative of the sigmoid), the gradients simplify to

$$
\frac{\partial J}{\partial w}
=
\frac{1}{m}
\sum_{i=1}^{m}
(p_i-y_i)x_i
$$

and

$$
\frac{\partial J}{\partial b}
=
\frac{1}{m}
\sum_{i=1}^{m}
(p_i-y_i)
$$

Let's compute them.

---

## Gradient for $w$

| $x$ | $y$ | $p$ | $p-y$ | $(p-y)x$ |
|-----|-----|-----|--------|----------|
| 1 | 0 | 0.5 | 0.5 | 0.5 |
| 2 | 0 | 0.5 | 0.5 | 1.0 |
| 3 | 1 | 0.5 | -0.5 | -1.5 |

The sum is

$$
0.5 + 1 - 1.5 = 0
$$

Therefore,

$$
\frac{\partial J}{\partial w}
=
0
$$

Interesting! The positive and negative contributions cancel out.

---

## Gradient for $b$

| $p-y$ |
|--------|
| 0.5 |
| 0.5 |
| -0.5 |

The sum is

$$
0.5
$$

The average is

$$
\frac{0.5}{3}
=
0.1667
$$

Therefore,

$$
\frac{\partial J}{\partial b}
=
0.1667
$$

---

# Step 6: Update the Parameters

Gradient descent updates the parameters as follows:

$$
w
=
w
-
\alpha
\frac{\partial J}{\partial w}
$$

$$
b
=
b
-
\alpha
\frac{\partial J}{\partial b}
$$

where the learning rate is

$$
\alpha = 0.1
$$

### Update $w$

$$
w
=
0
-
0.1(0)
=
0
$$

### Update $b$

$$
b
=
0
-
0.1(0.1667)
=
-0.01667
$$

The new parameters are

```python
w = 0
b = -0.01667
```

---

# Step 7: Predict Again

Now,

$$
z = wx + b
$$

Since $w = 0$,

$$
z = -0.01667
$$

for every sample.

The new prediction becomes

$$
\sigma(-0.01667)
\approx
0.4958
$$

So every prediction shifts slightly from **0.5000** to **0.4958**, moving in the direction that reduces the loss for the two negative examples.

---

# Where Did Those Gradient Formulas Come From?

The overall cost function is

$$
J
=
-\frac{1}{m}
\sum_{i=1}^{m}
\left[
y_i\log(p_i)
+
(1-y_i)\log(1-p_i)
\right]
$$

where

$$
p = \sigma(z)
$$

and

$$
z = wx + b
$$

To compute the gradient with respect to $w$, we use the **chain rule**:

$$
\frac{\partial J}{\partial w}
=
\frac{\partial J}{\partial p}
\cdot
\frac{\partial p}{\partial z}
\cdot
\frac{\partial z}{\partial w}
$$

The three derivatives are:

- $\frac{\partial J}{\partial p}$ → derivative of the cross-entropy loss
- $\frac{\partial p}{\partial z} = p(1-p)$ → derivative of the sigmoid function
- $\frac{\partial z}{\partial w} = x$

After simplification, the $p(1-p)$ terms cancel beautifully, giving the elegant result

$$
\boxed{
\frac{\partial J}{\partial w}
=
\frac{1}{m}
\sum_{i=1}^{m}
(p_i-y_i)x_i
}
$$

Similarly,

$$
\boxed{
\frac{\partial J}{\partial b}
=
\frac{1}{m}
\sum_{i=1}^{m}
(p_i-y_i)
}
$$

These are exactly the gradients used by libraries like **scikit-learn**, **TensorFlow**, and **PyTorch** when training logistic regression using gradient descent or its variants.

---

# A Better Example for Teaching

This dataset happened to give

$$
\frac{\partial J}{\partial w}=0
$$

which is mathematically correct but not very illustrative.

A better teaching dataset is:

| $x$ | $y$ |
|-----|-----|
| 1 | 0 |
| 2 | 0 |
| 4 | 1 |
| 5 | 1 |

For this dataset, **both** gradients are non-zero, so students can clearly see **both** $w$ and $b$ changing after the first iteration, making it much easier to understand how logistic regression learns.