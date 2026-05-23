# Tugas transformasi

Buat matrik tranformasi dari:
<iframe src="https://www.geogebra.org/calculator/jxrvcyu6?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>


Dari gambar, koordinat titik:
- A = (2, 3)
- B = (2, 1)
- C = (4, 1)

---

Diketahui:
A = (2,3)

---

## 1. Transformasi A ke B

Perpindahan:
(2,3) → (2,1)

$$
\begin{bmatrix}
1 & 0 \\
2 & -1
\end{bmatrix}
\begin{bmatrix}
2 \\
3
\end{bmatrix}
=
\begin{bmatrix}
(1 \cdot 2 + 0 \cdot 3) \\
(2 \cdot 2 + (-1) \cdot 3)
\end{bmatrix}
=
\begin{bmatrix}
2 \\
1
\end{bmatrix}
$$

---

## 2. Transformasi B ke C

Perpindahan:
(2,1) → (4,1)

$$
\begin{bmatrix}
2 & 0 \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
2 \\
1
\end{bmatrix}
=
\begin{bmatrix}
(2 \cdot 2 + 0 \cdot 1) \\
(0 \cdot 2 + 1 \cdot 1)
\end{bmatrix}
=
\begin{bmatrix}
4 \\
1
\end{bmatrix}
$$

---

## 3. Transformasi A ke C

Perpindahan:
(2,3) → (4,1)

$$
\begin{bmatrix}
2 & 0 \\
2 & -1
\end{bmatrix}
\begin{bmatrix}
2 \\
3
\end{bmatrix}
=
\begin{bmatrix}
(2 \cdot 2 + 0 \cdot 3) \\
(2 \cdot 2 + (-1) \cdot 3)
\end{bmatrix}
=
\begin{bmatrix}
4 \\
1
\end{bmatrix}
$$

Diketahui:
D = (2,4)

---

Dari gambar, koordinat titik:
- D = (2, 4)
- E = (2, 0)
- F = (4, 0)

## 1. Transformasi D ke E

Perpindahan:
(2,4) → (2,0)

$$
\begin{bmatrix}
1 & 0 \\
2 & -1
\end{bmatrix}
\begin{bmatrix}
2 \\
4
\end{bmatrix}
=
\begin{bmatrix}
(1 \cdot 2 + 0 \cdot 4) \\
(2 \cdot 2 + (-1) \cdot 4)
\end{bmatrix}
=
\begin{bmatrix}
2 \\
0
\end{bmatrix}
$$

---

## 2. Transformasi E ke F

Perpindahan:
(2,0) → (4,0)

$$
\begin{bmatrix}
2 & 0 \\
0 & 1
\end{bmatrix}
\begin{bmatrix}
2 \\
0
\end{bmatrix}
=
\begin{bmatrix}
(2 \cdot 2 + 0 \cdot 0) \\
(0 \cdot 2 + 1 \cdot 0)
\end{bmatrix}
=
\begin{bmatrix}
4 \\
0
\end{bmatrix}
$$

---

## 3. Transformasi D ke F

Perpindahan:
(2,4) → (4,0)

$$
\begin{bmatrix}
2 & 0 \\
2 & -1
\end{bmatrix}
\begin{bmatrix}
2 \\
4
\end{bmatrix}
=
\begin{bmatrix}
(2 \cdot 2 + 0 \cdot 4) \\
(2 \cdot 2 + (-1) \cdot 4)
\end{bmatrix}
=
\begin{bmatrix}
4 \\
0
\end{bmatrix}
$$