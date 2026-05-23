# Matriks Invers

## Determinan
$$
\begin{equation*}
\det A=\sum_{j=1}^n(-1)^{1+j}a_{1j}\det A_{1  j}=a_{11}\det A_{11}-a_{12} A_{12}+\cdots +(-1)^{1+n}a_{1n}\det A_{1  n}\text{.}
\end{equation*}
$$

##Minor & Ekspansi baris/kolom
$$
\begin{equation*}
\sum_{k=1}^n(-1)^{k+j}a_{kj}M_{kj}
\end{equation*}
$$

## Rumus Invers

$$
A^{-1} = \frac{1}{\det(A)} \cdot \operatorname{adj}(A)
$$

## Rumus Adjoint
$$
\begin{equation*}
(adj A)_{ij}=(-1)^{i+j}M_{ji}\text{.}
\end{equation*}
$$

Jika, 

$$
A =
\begin{bmatrix}
1 & 1 & 1 & 1 \\
2 & -1 & 1 & -1 \\
1 & 2 & -1 & 1 \\
3 & -1 & 2 & 1
\end{bmatrix}
$$

Menghitung Determinan (ekspansi baris pertama)

$$
\det(A) = a_{11}M_{11} + a_{12}M_{12} + a_{13}M_{13} + a_{14}M_{14}
$$
$$
M_{ij} = (-1)^{i+j} M_{ij}
$$

$$
\begin{split}
\det(A)=
1
\left|
\begin{array}{ccc}
-1 & 1 & -1\\
2 & -1 & 1\\
-1 & 2 & 1
\end{array}
\right|
-
1
\left|
\begin{array}{ccc}
2 & 1 & -1\\
1 & -1 & 1\\
3 & 2 & 1
\end{array}
\right|
+
1
\left|
\begin{array}{ccc}
2 & -1 & -1\\
1 & 2 & 1\\
3 & -1 & 1
\end{array}
\right|
-
1
\left|
\begin{array}{ccc}
2 & -1 & 1\\
1 & 2 & -1\\
3 & -1 & 2
\end{array}
\right|
\end{split}
$$

Determinan, 

$$
\det(A)=13
$$

Invers Matriks,

$$
\begin{split}
A^{-1}=
\frac{1}{13}
\left[
\begin{array}{cccc}
-3 & 3 & 4 & 2\\
9 & 4 & 1 & -6\\
11 & 2 & -6 & -3\\
-4 & -9 & 1 & 7
\end{array}
\right]
\end{split}
$$

