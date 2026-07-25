Detailed Notes on Matrix Multiplication
1. Introduction to Matrices
A matrix is a rectangular arrangement of numbers, symbols, or expressions in rows and columns.
Example:
A=[2345]A =
\begin{bmatrix}
2 & 3\\
4 & 5
\end{bmatrix}
A=[24​35​]
This matrix has:

2 rows
2 columns
Order (or dimension): 2×22 \times 22×2

A general matrix with mmm rows and nnn columns is called an m×nm \times nm×n matrix.

2. What is Matrix Multiplication?
Matrix multiplication is an operation where two matrices are combined to produce a third matrix.
If:
A×B=CA \times B = C
A×B=C
then each element of matrix CCC is found by multiplying a row of AAA with a column of BBB and adding the results.
The rule is:
(AB)ij=∑kaikbkj(AB)_{ij}=\sum_{k}a_{ik}b_{kj}
(AB)ij​=k∑​aik​bkj​
This means the element in row iii and column jjj of the product matrix is obtained by taking the dot product of row iii of AAA and column jjj of BBB.

3. Condition for Matrix Multiplication
Two matrices can be multiplied only when:
Number of columns in first matrix=Number of rows in second matrix\text{Number of columns in first matrix}
=
\text{Number of rows in second matrix}
Number of columns in first matrix=Number of rows in second matrix
If:
Am×n×Bn×pA_{m \times n} \times B_{n \times p}
Am×n​×Bn×p​
then the result will have dimensions:
Cm×pC_{m \times p}
Cm×p​
Example
Matrix AAA:
A=[123456]A=
\begin{bmatrix}
1&2&3\\
4&5&6
\end{bmatrix}
A=[14​25​36​]
Order:
2×32 \times 3
2×3
Matrix BBB:
B=[789101112]B=
\begin{bmatrix}
7&8\\
9&10\\
11&12
\end{bmatrix}
B=​7911​81012​​
Order:
3×23 \times 2
3×2
Since:
(2×3)(3×2)(2 \times 3)(3 \times 2)
(2×3)(3×2)
has matching inner dimensions, multiplication is possible.
The resulting matrix will have order:
2×22 \times 2
2×2

4. Steps for Matrix Multiplication
Consider:
A=[abcd]A=
\begin{bmatrix}
a&b\\
c&d
\end{bmatrix}
A=[ac​bd​]
and:
B=[efgh]B=
\begin{bmatrix}
e&f\\
g&h
\end{bmatrix}
B=[eg​fh​]
The product ABABAB is:
AB=[ae+bgaf+bhce+dgcf+dh]AB=
\begin{bmatrix}
ae+bg & af+bh\\
ce+dg & cf+dh
\end{bmatrix}
AB=[ae+bgce+dg​af+bhcf+dh​]
Explanation
First element:
(1,1)=ae+bg(1,1)=ae+bg
(1,1)=ae+bg
First row of AAA multiplied by first column of BBB.
Second element:
(1,2)=af+bh(1,2)=af+bh
(1,2)=af+bh
First row of AAA multiplied by second column of BBB.
Third element:
(2,1)=ce+dg(2,1)=ce+dg
(2,1)=ce+dg
Second row of AAA multiplied by first column of BBB.
Fourth element:
(2,2)=cf+dh(2,2)=cf+dh
(2,2)=cf+dh
Second row of AAA multiplied by second column of BBB.

5. Numerical Example
Multiply:
A=[2345]A=
\begin{bmatrix}
2&3\\
4&5
\end{bmatrix}
A=[24​35​]
and:
B=[1678]B=
\begin{bmatrix}
1&6\\
7&8
\end{bmatrix}
B=[17​68​]
Step 1: First element
(2×1)+(3×7)(2 \times 1)+(3 \times 7)
(2×1)+(3×7)
=2+21=23=2+21=23
=2+21=23
Step 2: Second element
(2×6)+(3×8)(2 \times 6)+(3 \times 8)
(2×6)+(3×8)
=12+24=36=12+24=36
=12+24=36
Step 3: Third element
(4×1)+(5×7)(4 \times 1)+(5 \times 7)
(4×1)+(5×7)
=4+35=39=4+35=39
=4+35=39
Step 4: Fourth element
(4×6)+(5×8)(4 \times 6)+(5 \times 8)
(4×6)+(5×8)
=24+40=64=24+40=64
=24+40=64
Therefore:
AB=[23363964]AB=
\begin{bmatrix}
23&36\\
39&64
\end{bmatrix}
AB=[2339​3664​]

6. Important Properties of Matrix Multiplication
1. Non-Commutative Property
Matrix multiplication generally does not follow the commutative law.
AB≠BAAB \neq BA
AB=BA
The order of multiplication matters.

2. Associative Property
Matrix multiplication is associative:
(AB)C=A(BC)(AB)C=A(BC)
(AB)C=A(BC)
Changing the grouping does not change the result.

3. Distributive Property
Matrix multiplication distributes over addition:
A(B+C)=AB+ACA(B+C)=AB+AC
A(B+C)=AB+AC
and:
(A+B)C=AC+BC(A+B)C=AC+BC
(A+B)C=AC+BC

4. Identity Matrix Property
The identity matrix behaves like the number 1.
For a 2×22 \times 22×2 identity matrix:
I=[1001]I=
\begin{bmatrix}
1&0\\
0&1
\end{bmatrix}
I=[10​01​]
Then:
AI=AAI=A
AI=A
and:
IA=AIA=A
IA=A

5. Zero Matrix Property
Any matrix multiplied by a zero matrix gives a zero matrix:
A×0=0A \times 0=0
A×0=0

7. Matrix Multiplication Using Dot Product
Each element of the product matrix is calculated using a dot product.
Example:
[123]⋅[456]\begin{bmatrix}
1&2&3
\end{bmatrix}
\cdot
\begin{bmatrix}
4\\
5\\
6
\end{bmatrix}
[1​2​3​]⋅​456​​
Multiply corresponding entries:
=(1×4)+(2×5)+(3×6)=(1 \times 4)+(2 \times 5)+(3 \times 6)
=(1×4)+(2×5)+(3×6)
=4+10+18=32=4+10+18=32
=4+10+18=32

8. Types of Matrix Multiplication
1. Square Matrix Multiplication
Both matrices have equal numbers of rows and columns.
Example:
2×2 multiplied by 2×22 \times 2 \text{ multiplied by } 2 \times 2
2×2 multiplied by 2×2

2. Rectangular Matrix Multiplication
Matrices have different dimensions.
Example:
(2×3)(3×4)(2 \times 3)(3 \times 4)
(2×3)(3×4)
Result:
2×42 \times 4
2×4

3. Scalar Multiplication
A matrix is multiplied by a single number.
Example:
3[2415]3
\begin{bmatrix}
2&4\\
1&5
\end{bmatrix}
3[21​45​]
Multiply every element by 3:
=[612315]=
\begin{bmatrix}
6&12\\
3&15
\end{bmatrix}
=[63​1215​]

9. Applications of Matrix Multiplication
Matrix multiplication is used in:

Computer graphics — rotation, scaling, and transformation of images
Artificial intelligence and machine learning — neural network calculations
Physics and engineering — modelling systems and transformations
Economics — input-output models
Cryptography — encoding and decoding information
Robotics — position and movement calculations
Statistics — data analysis


10. Common Mistakes
Mistake 1: Multiplying corresponding elements
Incorrect:
[12]×[34]\begin{bmatrix}
1&2
\end{bmatrix}
\times
\begin{bmatrix}
3&4
\end{bmatrix}
[1​2​]×[3​4​]
Matrix multiplication is not the same as multiplying matching positions.

Mistake 2: Ignoring dimension rules
Always check:
(m×n)(n×p)(m \times n)(n \times p)
(m×n)(n×p)
The two middle dimensions must be equal.

Mistake 3: Assuming the order can be changed
Remember:
AB≠BAAB \neq BA
AB=BA
for most matrices.

11. Summary

Matrix multiplication combines matrices using the row-by-column rule.
The number of columns in the first matrix must equal the number of rows in the second matrix.
The resulting matrix size is determined by the outer dimensions.
Matrix multiplication is generally not commutative.
It is associative and distributive.
Matrix multiplication is a fundamental concept used in mathematics, computing, engineering, and science.
