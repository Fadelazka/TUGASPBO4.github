from abc import ABC, abstractmethod

# Parent class
class Kendaraan(ABC):
    def __init__(self, nama, kecepatan=0):
        self.nama = nama
        self.kecepatan = kecepatan

    @abstractmethod
    def berjalan(self):
        pass

# Child classes
class Mobil(Kendaraan):
    def berjalan(self):
        return f"{self.nama} berjalan di jalan aspal dengan kecepatan {self.kecepatan} km/jam."

class Motor(Kendaraan):
    def berjalan(self):
        return f"{self.nama} melesat di antara mobil dengan kecepatan {self.kecepatan} km/jam."

class Pesawat(Kendaraan):
    def berjalan(self):
        return f"{self.nama} terbang di udara dengan kecepatan {self.kecepatan} km/jam."

# Tambahan class Kapal
class Kapal(Kendaraan):
    def berjalan(self):
        return f"{self.nama} berlayar di laut dengan kecepatan {self.kecepatan} knot."

# Membuat list objek (Polimorfisme)
daftar_kendaraan = [
    Mobil("Toyota Avanza", 120),
    Motor("Honda Beat", 80),
    Pesawat("Garuda Indonesia", 900),
    Kapal("Titanic", 40)
]

# Looping untuk memanggil method yang sama
for k in daftar_kendaraan:
    print(k.berjalan())