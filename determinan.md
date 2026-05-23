# Evaluasi Determinan dan Matriks

## A. Hitunglah determinan matriks berikut dengan menggunakan rumus ekspansi baris

## Rumus Determinan (Ekspansi Baris)

$$
\det(A) = \sum_{k=1}^{n} (-1)^{i+k} \, a_{ik} \, M_{ik}
$$

---

### 1. Matriks 2x2

$$
A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}
$$

Langkah:

$$
\det(A) = (-7)(4) - (-5)(1)
$$

$$
= -28 + 5 = -23
$$

---

### 2. Matriks 3x3 (Ekspansi Baris ke-1)

$$
A =
\begin{pmatrix}
0 & 2 & -3 \\
1 & -2 & -1 \\
0 & 0 & 1
\end{pmatrix}
$$

Gunakan rumus:

$$
\det(A) = \sum_{k=1}^{3} (-1)^{1+k} a_{1k} M_{1k}
$$

Langkah:

$$
= (-1)^{1+1}(0)M_{11} + (-1)^{1+2}(2)M_{12} + (-1)^{1+3}(-3)M_{13}
$$

Hitung minor:

$$
M_{12} =
\begin{vmatrix}
1 & -1 \\
0 & 1
\end{vmatrix}
= 1
$$

$$
M_{13} =
\begin{vmatrix}
1 & -2 \\
0 & 0
\end{vmatrix}
= 0
$$

Substitusi:

$$
\det(A) = (0) + (-1)(2)(1) + (1)(-3)(0)
$$

$$
= -2
$$

---

### 3. Matriks 4x4 (Ekspansi Baris ke-1)

$$
A =
\begin{pmatrix}
1 & -3 & 1 & 1 \\
-3 & 1 & 1 & 1 \\
1 & 1 & -3 & 1 \\
1 & 1 & 1 & -3
\end{pmatrix}
$$

Gunakan:

$$
\det(A) = \sum_{k=1}^{4} (-1)^{1+k} a_{1k} M_{1k}
$$

Langkah ekspansi:

$$
= 1\cdot M_{11} - (-3)\cdot M_{12} + 1\cdot M_{13} - 1\cdot M_{14}
$$

Hasil akhir:

$$
\det(A) = -256
$$

---

## B. Gunakan rumus adjoin untuk mencari invers matriks

$$
(adj\,A)_{ij} = (-1)^{i+j} M_{ji}
$$

$$
A^{-1} = \frac{1}{\det(A)} \, adj(A)
$$

---

### 4. Matriks 2×2

$$
A = \begin{pmatrix} -7 & -5 \\ 1 & 4 \end{pmatrix}
$$

Determinan:

$$
\det(A) = -23
$$

Adjoin:

$$
adj(A) =
\begin{pmatrix}
4 & 5 \\
-1 & -7
\end{pmatrix}
$$

Invers:

$$
A^{-1} = \frac{1}{-23}
\begin{pmatrix}
4 & 5 \\
-1 & -7
\end{pmatrix}
$$

---

### 5. Matriks 3×3

$$
A =
\begin{pmatrix}
0 & 2 & -3 \\
1 & -2 & -1 \\
0 & 0 & 1
\end{pmatrix}
$$

Determinan:

$$
\det(A) = -2
$$

Matriks kofaktor:

$$
C =
\begin{pmatrix}
-2 & -1 & 0 \\
-2 & 0 & 0 \\
-8 & 3 & -2
\end{pmatrix}
$$

Adjoin:

$$
adj(A) =
\begin{pmatrix}
-2 & -2 & -8 \\
-1 & 0 & 3 \\
0 & 0 & -2
\end{pmatrix}
$$

Invers:

$$
A^{-1} = \frac{1}{-2} adj(A)
$$

---

### 6. Matriks 4×4

$$
A =
\begin{pmatrix}
1 & -3 & 1 & 1 \\
-3 & 1 & 1 & 1 \\
1 & 1 & -3 & 1 \\
1 & 1 & 1 & -3
\end{pmatrix}
$$

Determinan:

$$
\det(A) = -256
$$

Adjoin:

$$
adj(A) =
\begin{pmatrix}
16 & -16 & 16 & -16 \\
-16 & 16 & -16 & 16 \\
16 & -16 & 16 & -16 \\
-16 & 16 & -16 & 16
\end{pmatrix}
$$

Invers:

$$
A^{-1} = \frac{1}{-256} adj(A)
$$