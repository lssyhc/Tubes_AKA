import matplotlib.pyplot as plt

# Data dari tabel
jumlah_data = [10, 20, 50, 100, 250, 500, 750, 998]
waktu_iteratif = [0.0086, 0.0090, 0.0142, 0.0139, 0.0166, 0.0271, 0.0480, 0.0799]
waktu_rekursif = [0.0063, 0.0079, 0.0190, 0.0409, 0.0704, 0.1954, 0.2817, 0.2758]

# Membuat grafik
plt.figure(figsize=(10, 6))
plt.plot(jumlah_data, waktu_iteratif, label="Iteratif", marker='o', color='blue')
plt.plot(jumlah_data, waktu_rekursif, label="Rekursif", marker='o', color='green')

# Menambahkan judul dan label
plt.title("Perbandingan Running Time: Iteratif vs Rekursif")
plt.xlabel("Jumlah Data")
plt.ylabel("Waktu Eksekusi (milidetik)")
plt.legend()
plt.grid(True)

# Menampilkan grafik
plt.show()
