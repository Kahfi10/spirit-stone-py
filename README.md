This programme will manage a stone that can store ‘energy’ and has hidden elemental ‘affinities’ (Fire, Water, Air).
# 💎 Proyek Batu Arwah (Spirit Stone)

Sebuah proyek sederhana untuk mendemonstrasikan konsep inti **Object-Oriented Programming (OOP)** dengan cara yang unik dan menarik. Bosan dengan contoh `Mobil` atau `Kucing`? Mari kita kelola *item magis*!

| 🐍 Bahasa | 📦 Konsep | 🎮 Tema |
| :--- | :--- | :--- |
| **Python 3.x** | **OOP Lengkap** | **Game / Fantasi** |

---

## 📜 Konsep Cerita

Setiap petualang hebat membutuhkan artefak magis. `BatuArwah` adalah artefak yang bisa menyerap energi dari lingkungan. Namun, batu ini rapuh dan memiliki rahasia.

* Setiap batu punya **nama** (public).
* Setiap batu menyimpan **energi** (protected), yang bisa diisi atau diatur.
* Setiap batu punya **afinitas elemen rahasia** (private) yang hanya terungkap jika energinya cukup.
* Jika batu diisi **energi berlebihan** (di atas 100), batu itu akan **retak** (status private) dan kehilangan semua energinya!

Proyek ini adalah simulasi sederhana untuk mengelola *state* (kondisi) dari batu tersebut menggunakan semua pilar OOP.

---

## 💡 Konsep OOP yang Didemonstrasikan

Program ini secara spesifik dirancang untuk menunjukkan:

1.  **Class & Objek**
    * `BatuArwah` adalah **Class** (cetak biru).
    * `batu_langit` atau `batu_gunung` adalah **Objek** (wujud nyata dari class).

2.  **Enkapsulasi (Access Modifiers)**
    * **Public (`self.nama`)**: Atribut yang bisa diakses dan diubah dari mana saja.
    * **Protected (`self._energi`)**: Atribut yang "sebaiknya" tidak diakses dari luar, ditandai dengan `_`. Kita berikan akses melalui Getter & Setter.
    * **Private (`self.__afinitas_elemen`, `self.__retak`)**: Atribut yang "tidak bisa" diakses dari luar, ditandai dengan `__`. Ini adalah rahasia internal batu!

3.  **Getter & Setter (Metode Tradisional)**
    * `get_energi_tersimpan()`: Sebuah **Getter** untuk mengambil nilai `_energi`.
    * `set_energi_tersimpan(nilai)`: Sebuah **Setter** yang berisi *logika validasi*. Di sinilah kita mengecek apakah `nilai` akan membuat batu retak atau tidak.

4.  **Property (Cara Pythonic)**
    * `@property def afinitas(self)`: Ini adalah **Getter versi Pythonic** yang canggih.
    * Bisa diakses seperti atribut (`batu.afinitas`), bukan metode (`batu.afinitas()`).
    * Memiliki logika: Hanya akan memberitahu afinitas elemen jika energi di atas 50.
    * Dibuat *read-only* (hanya-baca) karena kita tidak membuatkan `@afinitas.setter`.

5.  **Metode Public vs Private**
    * `serap_energi()` (Public) bisa dipanggil oleh siapa saja.
    * `__alami_keretakan()` (Private) adalah metode internal yang hanya bisa dipanggil oleh metode lain di dalam class itu sendiri (dalam kasus ini, dipanggil oleh `set_energi_tersimpan` atau `serap_energi` jika energi berlebih).

---

## 🚀 Quick Start

Salin kode `batu_arwah.py` ke proyek Anda, lalu impor dan gunakan class-nya.

```python
# --- main.py ---
from batu_arwah import BatuArwah

# 1. Ciptakan Objek BatuArwah
batu_pertama = BatuArwah(nama_batu="Batu Pijar", energi_awal=30)
batu_pertama.tampilkan_info()

print("---")

# 2. Cek 'Property' (Afinitas masih rahasia)
print(f"Afinitas: {batu_pertama.afinitas}") # Output: ??? (Energi tidak cukup...)

print("---")

# 3. Gunakan 'Setter' untuk menambah energi
print("Mengisi energi via Setter ke 80...")
batu_pertama.set_energi_tersimpan(80)

# 4. Cek 'Property' lagi (Sekarang terungkap!)
print(f"Afinitas: {batu_pertama.afinitas}") # Output: Api (atau Air/Udara/Tanah)

print("---")

# 5. Memicu kondisi 'Retak'
print("Mencoba menyerap energi berlebihan...")
batu_pertama.serap_energi(50) # Energi 80 + 50 = 130!
# Output: ENERGI BERLEBIHAN! Batu Pijar mengalami keretakan!

batu_pertama.tampilkan_info()
# Output:
# --- Info Batu: Batu Pijar ---
# Energi Tersimpan: 0
# Status: Retak
