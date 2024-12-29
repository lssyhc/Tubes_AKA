import time
import random

# Daftar karakter
karakter = [
    "Akai", "Atlas", "Balmond", "Barats", "Baxia", "Belerick", "Esmeralda", "Franco", "Gatotkaca", "Gloo", "Grock", "Hilda", "Hylos", "Johnson", 
    "Khufra", "Lolita", "Minotaur", "Ruby", "Tigreal", "Uranus", "Edith", "Phylax", "Aldous", "Alpha", "Alucard", "Argus", "Badang", "Bane", "Chou", 
    "Dyrroth", "Freya", "Guinevere", "Jawhead", "Kaja", "Lapu-Lapu", "Leomord", "Martis", "Masha", "Roger", "Silvanna", "Sun", "Thamuz", "Terizla", 
    "X.Borg", "Yu Zhong", "Aulus", "Yin", "Julian", "Fredrinn", "Arlott", "Cici", "Benedetta", "Fanny", "Gusion", "Hanzo", "Harley", "Hayabusa", 
    "Helcurt", "Kadita", "Karina", "Lancelot", "Lesley", "Ling", "Natalia", "Saber", "Selena", "Yi Sun-shin", "Aamon", "Alice", "Aurora", "Cecilion", 
    "Chang'e", "Cyclops", "Eudora", "Faramis", "Gord", "Harith", "Kagura", "Kimmy"
]

# Membuat daftar karakter dinamis
def buat_daftar_karakter(jumlah):
    return {
        f"{karakter[i % len(karakter)]}_{i + 1}": {"Nama": karakter[i % len(karakter)], "Penggunaan": random.randint(1, 100)}
        for i in range(jumlah)
    }

# Mencari karakter dengan penggunaan tertinggi (iteratif)
def cari_penggunaan_maks_iteratif(data):
    karakter_maks = None
    penggunaan_maks = float('-inf')
    for karakter, detail in data.items():
        if detail["Penggunaan"] > penggunaan_maks:
            karakter_maks = karakter
            penggunaan_maks = detail["Penggunaan"]
    return karakter_maks, penggunaan_maks

# Mencari karakter dengan penggunaan tertinggi (rekursif)
def cari_penggunaan_maks_rekursif(data, kunci=None, indeks=0, karakter_maks=None, penggunaan_maks=float('-inf')):
    if kunci is None:
        kunci = list(data.keys())
    if indeks == len(kunci):
        return karakter_maks, penggunaan_maks

    karakter_saat_ini = kunci[indeks]
    penggunaan_saat_ini = data[karakter_saat_ini]["Penggunaan"]

    if penggunaan_saat_ini > penggunaan_maks:
        karakter_maks = karakter_saat_ini
        penggunaan_maks = penggunaan_saat_ini

    return cari_penggunaan_maks_rekursif(data, kunci, indeks + 1, karakter_maks, penggunaan_maks)

# Program utama
try:
    jumlah_karakter = int(input("Masukkan jumlah karakter: "))
    if jumlah_karakter <= 0:
        print("Jumlah karakter harus lebih dari 0.")
    else:
        data_karakter = buat_daftar_karakter(jumlah_karakter)

        # Metode iteratif
        mulai = time.perf_counter()
        hasil_iteratif = cari_penggunaan_maks_iteratif(data_karakter)
        waktu_iteratif = (time.perf_counter() - mulai) * 1000

        # Metode rekursif
        mulai = time.perf_counter()
        hasil_rekursif = cari_penggunaan_maks_rekursif(data_karakter)
        waktu_rekursif = (time.perf_counter() - mulai) * 1000

        # Hasil
        print(f"\nJumlah data: {len(data_karakter)}")
        print(f"Iteratif - Nama: {hasil_iteratif[0]}, Penggunaan: {hasil_iteratif[1]}, Waktu: {waktu_iteratif:.6f} ms")
        print(f"Rekursif - Nama: {hasil_rekursif[0]}, Penggunaan: {hasil_rekursif[1]}, Waktu: {waktu_rekursif:.6f} ms")
        
        # Perbandingan kinerja
        perbedaan = abs(waktu_iteratif - waktu_rekursif)
        if waktu_iteratif < waktu_rekursif:
            print(f"Metode iteratif lebih cepat ({perbedaan:.6f} ms lebih cepat).")
        elif waktu_rekursif < waktu_iteratif:
            print(f"Metode rekursif lebih cepat ({perbedaan:.6f} ms lebih cepat).")
        else:
            print("Kedua metode memiliki kecepatan yang sama.")

        # Menampilkan detail data
        print("\n=== Detail data karakter ===")
        for nama, detail in data_karakter.items():
            print(f"{nama}: Penggunaan = {detail['Penggunaan']}")
except ValueError:
    print("Input tidak valid. Harap masukkan angka yang benar.")
