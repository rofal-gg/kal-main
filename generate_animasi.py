import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ==========================================
# OBJEK AWAL (ABCD) - Urutan memutar searah jarum jam
# ==========================================
objek = np.array([
    [2, 3],
    [2, 4],
    [3, 4],
    [3, 3],
    [2, 3]
])

# ==========================================
# TRANSFORMASI (Pencerminan terhadap Sumbu-X)
# ==========================================
R = np.array([
    [1,  0],
    [0, -1]
])

def T(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def ke_homogen(obj):
    return np.hstack((obj, np.ones((obj.shape[0], 1))))

def ke_cartesian(obj):
    return obj[:, :2]

# ==========================================
# LABEL KOORDINAT
# ==========================================
def gambar_label(points, warna, arah):
    if arah == 'atas':
        offsets = [
            (-0.8, -0.4),  # A
            (-0.8, 0.2),   # B
            (0.2, 0.2),    # C
            (0.2, -0.4)    # D
        ]
    else:  # Untuk bayangan di bawah sumbu-X
        offsets = [
            (-0.8, 0.2),
            (-0.8, -0.4),
            (0.2, -0.4),
            (0.2, 0.2)
        ]

    for i, (x, y) in enumerate(points[:-1]):
        dx, dy = offsets[i % 4]
        ax.plot(x, y, 'o', color=warna, markersize=3)
        ax.text(
            x + dx, y + dy,
            f"({x:.1f},{y:.1f})",
            fontsize=6,
            color=warna,
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='none')
        )

# ==========================================
# SETUP PLOT
# ==========================================
plt.rcParams['figure.dpi'] = 140
fig, ax = plt.subplots(figsize=(7, 7))

total_frames = 15
max_translation = -2.0  # Bergerak turun sejauh 2 satuan (dari y=3 ke y=1)

def update(frame):
    ax.clear()

    # Grid & Limit Canvas
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')

    # Sumbu utama
    ax.axhline(0, color='black', linewidth=1.2)
    ax.axvline(0, color='black', linewidth=1.2)

    # Grid rapat berurutan
    ax.set_xticks(np.arange(-5, 6, 1))
    ax.set_yticks(np.arange(-5, 6, 1))
    ax.grid(True, linewidth=0.5, linestyle=':')

    # PROSES GERAK (TRANSLASI & REFLEKSI)
    ty = (frame / (total_frames - 1)) * max_translation
    obj_h = ke_homogen(objek)

    # 1. Objek Asli: Turun Vertikal (ABCD -> EFGH)
    asli = (T(0, ty) @ obj_h.T).T
    asli = ke_cartesian(asli)

    # 2. Refleksi Awal di Sumbu-X
    refleksi_awal = (R @ objek.T).T
    refleksi_h = ke_homogen(refleksi_awal)

    # 3. Gerak Bayangan: Naik Vertikal (arahnya berlawanan)
    refleksi = (T(0, -ty) @ refleksi_h.T).T
    refleksi = ke_cartesian(refleksi)

    # Gambar Garis Objek & Bayangan
    ax.plot(asli[:, 0], asli[:, 1], 'b-', linewidth=2, label='Objek (ABCD -> EFGH)')
    ax.plot(refleksi[:, 0], refleksi[:, 1], 'r--', linewidth=2, label='Refleksi (Sumbu-X)')

    # Berikan Label Koordinat dinamis
    gambar_label(asli, 'blue', 'atas')
    gambar_label(refleksi, 'red', 'bawah')

    ax.legend(loc='upper right')
    ax.set_title(f"Pencerminan Sumbu-X | Step = {frame}")

# ==========================================
# PROSES GENERATE GIF
# ==========================================
print("Sedang memproses animasi menjadi GIF...")
anim = FuncAnimation(fig, update, frames=total_frames, interval=300, repeat=True)

output_filename = 'animasi.gif'
anim.save(output_filename, writer='pillow', fps=3)

print(f"Sukses! File '{output_filename}' telah dibuat.")