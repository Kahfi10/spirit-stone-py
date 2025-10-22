import random

class BatuArwah:
    """
    Sebuah Class untuk merepresentasikan Batu Arwah.
    Batu ini menyimpan energi dan memiliki afinitas elemen rahasia.
    """
    
    def __init__(self, nama_batu, energi_awal):
        # 1. ATRIBUT PUBLIC
        # Bisa diakses dan diubah dari mana saja.
        self.nama = nama_batu
        
        # 2. ATRIBUT PROTECTED (Konvensi Python: diawali 1 underscore)
        # Sebaiknya hanya diakses oleh class ini dan turunannya.
        self._energi = energi_awal
        
        # 3. ATRIBUT PRIVATE (Konvensi Python: diawali 2 underscore)
        # Hanya bisa diakses di dalam class ini.
        # Python akan melakukan 'name mangling' agar sulit diakses dari luar.
        self.__afinitas_elemen = random.choice(["Api", "Air", "Udara", "Tanah"])
        self.__retak = False # Status internal batu

    # --- Metode Public ---
    
    def serap_energi(self, jumlah):
        """Metode public untuk menambah energi batu."""
        if self.__retak:
            print(f"{self.nama} sudah retak dan tidak bisa menyerap energi.")
            return
            
        self._energi += jumlah
        print(f"{self.nama} menyerap {jumlah} energi. Total energi: {self._energi}")
        
        # Metode public bisa memanggil metode private
        if self._energi > 100:
            self.__alami_keretakan()

    def tampilkan_info(self):
        """Metode public untuk menampilkan info dasar."""
        print(f"--- Info Batu: {self.nama} ---")
        print(f"Energi Tersimpan: {self._energi}")
        print(f"Status: {'Retak' if self.__retak else 'Stabil'}")

    # --- Metode Private ---
    
    def __alami_keretakan(self):
        """
        Metode private yang hanya bisa dipanggil dari dalam class.
        Dipicu jika energi melebihi batas.
        """
        print(f"ENERGI BERLEBIHAN! {self.nama} mengalami keretakan!")
        self.__retak = True
        self._energi = 0 # Energi hilang saat retak

    # --- 4. GETTER & 5. SETTER (Cara Tradisional) ---
    
    def get_energi_tersimpan(self):
        """
        GETTER: Metode untuk 'mendapatkan' nilai atribut protected.
        """
        return self._energi

    def set_energi_tersimpan(self, nilai_baru):
        """
        SETTER: Metode untuk 'mengatur' nilai atribut protected.
        Kita bisa menambahkan validasi di sini.
        """
        if nilai_baru < 0:
            print("Energi tidak bisa negatif. Diatur ke 0.")
            self._energi = 0
        elif nilai_baru > 100:
            print("Energi melebihi batas. Batu akan retak.")
            self._energi = nilai_baru
            self.__alami_keretakan()
        else:
            self._energi = nilai_baru

    # --- 6. PROPERTY (Cara Pythonic untuk Getter & Setter) ---
    
    @property
    def afinitas(self):
        """
        PROPERTY (GETTER): Ini adalah getter untuk atribut private __afinitas_elemen.
        Cara aksesnya seperti atribut: 'batu.afinitas', bukan 'batu.afinitas()'
        """
        if self._energi < 50:
            return "??? (Energi tidak cukup untuk melihat afinitas)"
        
        # Jika energi cukup, tunjukkan afinitas rahasianya
        return self.__afinitas_elemen
        
    # Kita tidak membuat @afinitas.setter, 
    # artinya properti ini bersifat 'read-only' (hanya bisa dibaca).


# --- DEMONSTRASI PENGGUNAAN ---

print("--- 1. Membuat OBJEK ---")
# 'batu_langit' adalah sebuah OBJEK (instance) dari CLASS 'BatuArwah'
batu_langit = BatuArwah(nama_batu="Batu Langit", energi_awal=10)

print("\n--- 2. Akses Atribut PUBLIC ---")
print(f"Nama batu: {batu_langit.nama}")
# Atribut public bisa diubah langsung
batu_langit.nama = "Batu Langit Kuno"
print(f"Nama batu diubah: {batu_langit.nama}")

print("\n--- 3. Akses Atribut PROTECTED (Tidak Disarankan) ---")
# Bisa, tapi sebaiknya jangan dilakukan langsung
print(f"Energi (akses langsung): {batu_langit._energi}")

print("\n--- 4. Akses Atribut PRIVATE (Akan Gagal) ---")
try:
    print(batu_langit.__afinitas_elemen)
except AttributeError as e:
    print(f"Gagal akses private: {e}")

print("\n--- 5. Menggunakan GETTER & SETTER Tradisional ---")
# Menggunakan getter
print(f"Energi (via getter): {batu_langit.get_energi_tersimpan()}")
# Menggunakan setter
print("Mengatur energi ke 80 via setter...")
batu_langit.set_energi_tersimpan(80)
print(f"Energi (via getter): {batu_langit.get_energi_tersimpan()}")

print("\n--- 6. Menggunakan PROPERTY (Getter Pythonic) ---")
# Energi masih 10 (belum cukup)
batu_langit.set_energi_tersimpan(30)
print(f"Afinitas saat energi {batu_langit.get_energi_tersimpan()}: {batu_langit.afinitas}")

# Coba naikkan energi
batu_langit.set_energi_tersimpan(70)
print(f"Afinitas saat energi {batu_langit.get_energi_tersimpan()}: {batu_langit.afinitas}")

print("\n--- 7. Menggunakan Metode Public (Memanggil Private) ---")
batu_langit.tampilkan_info()
print("Menyerap energi hingga retak...")
batu_langit.serap_energi(40) # 70 + 40 = 110 (melebihi batas)

# Info setelah retak
batu_langit.tampilkan_info()
print(f"Energi (via getter): {batu_langit.get_energi_tersimpan()}")