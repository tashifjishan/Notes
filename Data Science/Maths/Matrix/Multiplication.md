# Detailed Notes on Matrix Multiplication

## 1. Introduction to Matrices

A **matrix** is a rectangular arrangement of numbers, symbols, or expressions in rows and columns.

Example:

[
A=
\begin{bmatrix}
2 & 3\
4 & 5
\end{bmatrix}
]

This matrix has:

* **2 rows**
* **2 columns**
* Order (or dimension): **2 × 2**

A general matrix with (m) rows and (n) columns is called an (m \times n) matrix.

---

# 2. What is Matrix Multiplication?

Matrix multiplication is an operation where two matrices are combined to produce a third matrix.

If:

[
A \times B = C
]

then each element of matrix (C) is found by multiplying a **row of A** with a **column of B** and adding the results.

genui{"linear_algebra_optimization_learning_block":{"type_id":"MATRIX_MULTIPLICATION_ROW_COLUMN_RULE","locale_override":"en-GB"}}

---

# 3. Condition for Matrix Multiplication

Two matrices can be multiplied only when:

[
\text{Number of columns in first matrix} = \text{Number of rows in second matrix}
]

If:

[
A_{m\times n} \times B_{n\times p}
]

then the result will be:

[
C_{m\times p}
]

### Example:

[
A=
\begin{bmatrix}
1&2&3\
4&5&6
\end{bmatrix}
]

Order: (2 \times 3)

[
B=
\begin{bmatrix}
7&8\
9&10\
11&12
\end{bmatrix}
]

Order: (3 \times 2)

Since the inner numbers match:

[
(2\times3)(3\times2)
]

the multiplication is possible, and the answer will be:

[
2\times2
]

---

# 4. Steps for Matrix Multiplication

Consider:

[
A=
\begin{bmatrix}
a&b\
c&d
\end{bmatrix}
]

and

[
B=
\begin{bmatrix}
e&f\
g&h
\end{bmatrix}
]

The product (AB) is:

[
AB=
\begin{bmatrix}
ae+bg & af+bh\
ce+dg & cf+dh
\end{bmatrix}
]

### Explanation:

* First row × first column:

[
ae+bg
]

* First row × second column:

[
af+bh
]

* Second row × first column:

[
ce+dg
]

* Second row × second column:

[
cf+dh
]

---

# 5. Numerical Example

Multiply:

[
A=
\begin{bmatrix}
2&3\
4&5
\end{bmatrix}
]

[
B=
\begin{bmatrix}
1&6\
7&8
\end{bmatrix}
]

### First element:

[
(2\times1)+(3\times7)
]

[
=2+21=23
]

### Second element:

[
(2\times6)+(3\times8)
]

[
=12+24=36
]

### Third element:

[
(4\times1)+(5\times7)
]

[
=4+35=39
]

### Fourth element:

[
(4\times6)+(5\times8)
]

[
=24+40=64
]

Therefore:

[
AB=
\begin{bmatrix}
23&36\
39&64
\end{bmatrix}
]

---

# 6. Important Properties of Matrix Multiplication

## 1. Not Commutative

Matrix multiplication usually does **not** follow:

[
AB=BA
]

In general:

[
AB\neq BA
]

Example:

[
A\times B
]

may give a different answer from:

[
B\times A
]

---

## 2. Associative Property

Matrix multiplication is associative:

[
(AB)C=A(BC)
]

The grouping can change, but the result remains the same.

---

## 3. Distributive Property

Matrix multiplication distributes over addition:

[
A(B+C)=AB+AC
]

and:

[
(A+B)C=AC+BC
]

---

## 4. Identity Matrix Property

The identity matrix acts like the number 1.

For a (2\times2) identity matrix:

[
I=
\begin{bmatrix}
1&0\
0&1
\end{bmatrix}
]

Then:

[
AI=A
]

and:

[
IA=A
]

---

## 5. Zero Matrix Property

Any matrix multiplied by a zero matrix gives a zero matrix:

[
A \times 0=0
]

---

# 7. Matrix Multiplication Using Dot Product

Each entry in the product matrix is obtained using the dot product:

[
\text{Row of first matrix}\cdot\text{Column of second matrix}
]

Example:

[
\begin{bmatrix}
1&2&3
\end{bmatrix}
\cdot
\begin{bmatrix}
4\
5\
6
\end{bmatrix}
]

[
=(1\times4)+(2\times5)+(3\times6)
]

[
=4+10+18=32
]

---

# 8. Types of Matrix Multiplication

### 1. Square Matrix Multiplication

Both matrices have the same number of rows and columns.

Example:

[
2\times2 \text{ multiplied by } 2\times2
]

---

### 2. Rectangular Matrix Multiplication

Matrices have different dimensions.

Example:

[
2\times3 \text{ multiplied by } 3\times4
]

Result:

[
2\times4
]

---

### 3. Scalar Multiplication

A matrix is multiplied by a single number.

Example:

[
3
\begin{bmatrix}
2&4\
1&5
\end{bmatrix}
]

Multiply every element by 3:

# [

\begin{bmatrix}
6&12\
3&15
\end{bmatrix}
]

---

# 9. Applications of Matrix Multiplication

Matrix multiplication is widely used in:

* **Computer graphics** (rotation, scaling, and movement of images)
* **Artificial intelligence and machine learning**
* **Physics and engineering calculations**
* **Economics and statistics**
* **Cryptography**
* **Robotics**
* **Network analysis**

---

# 10. Common Mistakes

1. **Multiplying corresponding elements directly**

Incorrect:

[
\begin{bmatrix}1&2\end{bmatrix}
\times
\begin{bmatrix}3&4\end{bmatrix}
]

Matrix multiplication is not element-by-element multiplication.

---

2. **Ignoring dimension rules**

Always check:

[
(m\times n)(n\times p)
]

The middle dimensions must be equal.

---

3. **Changing the order**

Remember:

[
AB \neq BA
]

in most cases.

---

# 11. Summary

* Matrix multiplication combines two matrices using **row-by-column multiplication**.
* The number of columns of the first matrix must equal the number of rows of the second.
* The order of the resulting matrix is determined by the outside dimensions.
* Matrix multiplication is generally **not commutative**.
* It is associative and distributive.
* It is an essential tool in mathematics, science, computing, and engineering.
