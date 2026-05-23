# Sistem Persamaan Linier
 
## A. Pengertian

**Sistem persamaan linear** adalah kumpulan dua atau lebih persamaan linear yang memiliki variabel yang sama dan harus dipenuhi secara bersamaan.
Disebut linear karena setiap variabel berpangkat satu, tidak ada perkalian antar variabel, dan tidak ada variabel di dalam akar atau pangkat lebih dari satu.

**Contoh:**

$$\begin{cases}
2x + y = 5 \\
x - y = 1
\end{cases}$$


Artinya kita mencari nilai 𝑥 dan 𝑦 yang membuat kedua persamaan benar sekaligus.

## B. Bentuk Umum Sistem Linear

Bentuk umum sistem dengan 𝑚 persamaan dan 𝑛 variabel:

$$\begin{split}
\begin{eqnarray*}
a_{11}x_1 + a_{12}x_2 + \hspace{0.5cm} ... \hspace{0.5cm} + a_{1n}x_n & = & b_1 \\
a_{21}x_1 + a_{22}x_2 + \hspace{0.5cm} ... \hspace{0.5cm} + a_{2n}x_n & = & b_2 \\
\vdots \hspace{1.2cm} \vdots \hspace{3cm} \vdots \hspace{0.5cm}  & = & \vdots \\
a_{m1}x_1 + a_{m2}x_2 + \hspace{0.5cm} ... \hspace{0.5cm} +  a_{mn}x_n & = & b_m \\
\end{eqnarray*}
\end{split}$$

Dengan keterangan:
- 𝑥1,𝑥2,...,𝑥n adalah variabel,
- a adalah koefisien,
- b adalah konstanta.

## C. Metode Penyelesaian

**Metode Penyelesaian Sistem Persamaan Linear**

**1. Metode Substitusi:**
- Substitusi satu variabel ke persamaan lain.
- Cocok untuk sistem sederhana.

**2. Metode Eliminasi:**
- Hilangkan satu variabel dengan operasi penjumlahan/pengurangan persamaan.

**3. Metode Matriks (Eliminasi Gauss/Gauss-Jordan):**
- Ubah sistem ke bentuk matriks eselon baris/reduksi.

**4. Aturan Cramer:**
- Gunakan determinan matriks untuk mencari solusi.

**5. Metode Numerik (Iterasi):**
- Misalnya, metode Jacobi atau Gauss-Seidel.

## D. Eliminasi Gauss

Eliminasi Gaussian adalah algoritme untuk menyelesaikan sistem persamaan linier dengan melakukan transformasi pada sistem agar lebih mudah dipecahkan. Dalam praktiknya, kita bekerja dengan matriks augmented yang berisi koefisien dan konstanta dari sistem persamaan.

Tujuan eliminasi adalah mengubah sistem linier yang kompleks menjadi sistem yang berbentuk lebih sederhana (seperti segitiga atas), sehingga solusi variabel-variabelnya dapat ditemukan dengan mudah melalui substitusi balik.

Ada tiga operasi baris yang digunakan dalam eliminasi, yang tidak mengubah solusi sistem:
- Tukarkan posisi ke dua persamaan.
- Kalikan persamaan dengan bilangan apa pun yang bukan nol.
- Gantikan suatu persamaan dengan jumlah persamaan itu sendiri dan kelipatan peserta lainnya.

**Langkah-Langkah Proses**

1. Forward elimination
Bagian awal proses di mana kita menghilangkan variabel di bawah pivot sehingga menghasilkan matriks segitiga atas.

2. Pivoting
Jika elemen di posisi pivot (titik utama eliminasi) bernilai nol atau kecil, kita mungkin harus menukar baris agar proses berjalan dengan benar.

3. Back substitution
Setelah bentuk segitiga atas terbentuk, kita dapat menyelesaikan sistem mulai dari baris paling bawah (variabel terakhir), lalu substitusi kembali ke atas untuk menemukan semua variabel.

### Mentransformasi Sistem

$$
\begin{cases}
x_1 - x_2 + x_3 = 3 \\
2x_1 + x_2 + 8x_3 = 18 \\
4x_1 + 2x_2 - 3x_3 = -2
\end{cases}
$$

==

$$
\left[
\begin{array}{ccc|c}
1 & -1 & 1 & 3 \\
2 & 1 & 8 & 18 \\
4 & 2 & -3 & -2
\end{array}
\right]
$$

*Setelah eliminasi Gauss (bentuk tangga)*

$$
\begin{cases}
x_1 - x_2 + x_3 = 3 \\
x_2 + 2x_3 = 4 \\
x_3 = 2
\end{cases}
$$

$$
\left[
\begin{array}{ccc|c}
1 & -1 & 1 & 3 \\
0 & 1 & 2 & 4 \\
0 & 0 & 1 & 2
\end{array}
\right]
$$

## E. Solusi Sistem Persamaan Linear

### 1. Solusi Tunggal
- Hanya ada satu pasangan nilai variabel yang memenuhi semua persamaan.
- Sistem disebut konsisten independen.
- Secara grafik (2 variabel): Dua garis berpotong di satu titik.

**Contoh**

$$\begin{aligned}
-x + y &= 1 \\
2x - y &= 0
\end{aligned}$$

**Matriks:**

$$\left[
\begin{array}{cc|c}
-1 & 1 & 1 \\
2 & -1 & 0
\end{array}
\right]$$

    import numpy as np

    # Membuat matriks
    A = np.array([
        [-1, 1, 1],
        [2, -1, 0]
    ])

    # Menampilkan matriks
    print("Matriks A:")
    print(A)

**Langkah OBE**

Hilangkan salah satu variabel. 

Gunakan: 

$$2R1 = \begin{pmatrix}
-2 & 2 \mid 2
\end{pmatrix}$$

Tambah ke baris kedua:

$$\begin{pmatrix}
2 & -1 \mid 0
\end{pmatrix}
+
\begin{pmatrix}
-2 & 2 \mid 2
\end{pmatrix}
=
\begin{pmatrix}
0 & 1 \mid 2
\end{pmatrix}$$

$$\left[
\begin{array}{cc|c}
-1 & 1 & 1 \\
0 & 1 & 2
\end{array}
\right]$$

Eliminasi variabel y pada baris pertama

Gunakan:

$$\begin{pmatrix}
-1 & 1 \mid 1
\end{pmatrix}
-
\begin{pmatrix}
0 & 1 \mid 2
\end{pmatrix}
=
\begin{pmatrix}
-1 & 0 \mid -1
\end{pmatrix}$$

$$\left[
\begin{array}{cc|c}
-1 & 0 & -1 \\
0 & 1 & 2
\end{array}
\right]$$

Ubah koefisien utama jadi 1

$$\begin{pmatrix}
1 & 0 \mid 1
\end{pmatrix}$$

$$\left[
\begin{array}{cc|c}
1 & 0 & 1 \\
0 & 1 & 2
\end{array}
\right]$$

**Hasil Akhir**

$$\boxed{x = 1 \quad , \quad y = 2}$$

Jadi:

$$(x,y) = (1,2)$$

**Code Python**

```python
import numpy as np

# Matriks awal (augmented matrix)
A = np.array([
[-1,  1,  1],
[ 2, -1,  0]
], dtype=float)

print("Matriks Awal:")
print(A)

# Langkah 1: R2 = R2 + 2R1
A[1] = A[1] + 2 * A[0]
print("\nSetelah R2 = R2 + 2R1:")
print(A)

# Langkah 2: R1 = R1 - R2
A[0] = A[0] - A[1]
print("\nSetelah R1 = R1 - R2:")
print(A)

# Langkah 3: R1 = -1 * R1 (agar koefisien utama jadi 1)
A[0] = -1 * A[0]
print("\nSetelah R1 dikali -1:")
print(A)

# Hasil akhir
x = A[0, 2]
y = A[1, 2]

print("\nHasil Akhir:")
print("x =", int(x))
print("y =", int(y))
```

### 2. Tidak Ada Solusi
- Tidak ada nilai variabel yang memenuhi semua persamaan.
- Sistem disebut inkonsisten
- Secara grafik: Dua garis sejajar(tidak berpotongan).

**Contoh**

$$\begin{cases}
x + y = 2 \\
2x + 2y = 5
\end{cases}$$

**Matriks**

$$\left[
\begin{array}{cc|c}
1 & 1 & 2 \\
2 & 2 & 5
\end{array}
\right]$$

```python
    import numpy as np

    # Membuat matriks augmented
    A = np.array([
        [1, 1, 2],
        [0, 0, 1]
    ])

    print("Matriks Augmented:")
    print(A)
```

**Langkah OBE**

Hilangkan elemen di bawah pivot pertama.

$$\left[
\begin{array}{cc|c}
1 & 1 & 2 \\
0 & 0 & 1
\end{array}
\right]$$
```python
    import numpy as np

    # Membuat matriks augmented
    A = np.array([
        [1, 1, 2],
        [0, 0, 1]
    ])

    print("Matriks Augmented:")
    print(A)
```

Baris kedua menyatakan:

$$0x + 0y = 1$$

$$0 = 1$$

**Kesimpulan**

Karena muncul persamaan yang tidak mungkin benar (0 = 1), maka sistem tersebut disebut tidak memiliki solusi atau inkonsisten.

### 3. Solusi Tak Terhingga
- Memiliki banyak (tak terhingga) solusi.
- Sistem disebut konsisten dependen.
- Secara grafik: garis berimpit.

**Contoh**

$$\begin{cases}
x + y + z = 3 \\
2x + 2y + 2z = 6 \\
x + y + z = 3
\end{cases}$$

**Matriks**

$$\begin{bmatrix}
1 & 1 & 1 & 3 \\
2 & 2 & 2 & 6 \\
1 & 1 & 1 & 3
\end{bmatrix}$$

```python
    import numpy as np

    A = np.array([
        [1, 1, 1, 3],
        [2, 2, 2, 6],
        [1, 1, 1, 3]
    ])

    print("Matriks A:")
    print(A)
```

**Langkah OBE**

Baris 2 dikurangi 2 x Baris 1

Baris 3 dikurangi Baris 1

Hasil:

$$\begin{bmatrix}
1 & 1 & 1 & 3 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}$$

```python
    import numpy as np

    # Membuat matriks
    A = np.array([
        [1, 1, 1, 3],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ])

    # Menampilkan matriks
    print("Matriks A:")
    print(A)
```

**Solusi Umum:**

Misalkan:

$$y = s, \quad z = t$$

Maka:

$$x = 3 - s - t$$

**Hasil Akhir**

$$(x,y,z) = (3 - s - t,\; s,\; t)$$

$$s,t \in \mathbb{R}$$

Karena terdapat variabel bebas, maka SPL memiliki solusi tak terhingga atau banyak solusi.

## F. Visualisasi Geometri menggunakan Geogebra

### 1. Solusi Tunggal

Disebut Solusi Tunggal apabila terdapat tepat satu himpunan nilai variabel yang memenuhi semua persamaan secara bersamaan. Kondisi ini terjadi ketika setiap variabel dapat ditentukan secara pasti melalui proses penyelesaian, misalnya dengan substitusi, eliminasi, atau Operasi Baris Elementer (OBE). Secara aljabar, hal ini berarti sistem memiliki cukup persamaan yang saling independen untuk menentukan semua variabel. Secara geometri, pada sistem dua variabel, solusi tunggal terjadi ketika dua garis berpotongan di satu titik. Pada tiga variabel, hal ini terjadi ketika tiga bidang berpotongan tepat di satu titik.

<iframe src="https://www.geogebra.org/calculator/dgzusbnp?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

### 2. Tidak Ada Solusi

Disebut Tidak Ada Solusi apabila terdapat banyak kemungkinan nilai variabel yang memenuhi semua persamaan. Ini biasanya terjadi karena ada persamaan yang sebenarnya merupakan kelipatan atau kombinasi dari persamaan lainnya, sehingga sistem tidak memberikan informasi baru yang cukup untuk menentukan semua variabel secara unik. Dalam proses OBE, kondisi ini ditandai dengan munculnya baris nol atau adanya variabel bebas. Secara geometri, pada dua variabel, kondisi ini terjadi ketika dua garis berimpit (menjadi garis yang sama). Pada tiga variabel, solusi dapat berupa sebuah garis atau bidang yang merupakan irisan bersama.

<iframe src="https://www.geogebra.org/calculator/gba5twg4?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

### 3. Solusi Tak Terhingga

Disebut Solusi Tak terhingga apabila tidak ada satu pun nilai variabel yang dapat memenuhi semua persamaan secara bersamaan. Hal ini terjadi ketika terdapat pertentangan antar persamaan. Dalam penyelesaian menggunakan OBE, kondisi ini biasanya ditandai dengan munculnya pernyataan yang tidak mungkin benar, seperti 0 = 5. Secara geometri, pada dua variabel, keadaan ini digambarkan sebagai dua garis sejajar yang tidak pernah berpotongan. Pada tiga variabel, dapat berupa bidang-bidang yang tidak memiliki titik persekutuan.

<iframe src="https://www.geogebra.org/calculator/ghjnamqe?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>
