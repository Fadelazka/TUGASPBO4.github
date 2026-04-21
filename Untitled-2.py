class Karyawan:
    def __init__(self, nama):
        self.nama = nama

    def hitung_gaji(self):
        pass

    def gaji_bersih(self):
        gaji_kotor = self.hitung_gaji()
        return gaji_kotor  # akan di-override di child jika perlu

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji_bulanan):
        super().__init__(nama)
        self.gaji_bulanan = gaji_bulanan

    def hitung_gaji(self):
        # Bonus 10% jika gaji > 5 juta
        if self.gaji_bulanan > 5_000_000:
            bonus = self.gaji_bulanan * 0.1
        else:
            bonus = 0
        return self.gaji_bulanan + bonus

    def gaji_bersih(self):
        gaji_kotor = self.hitung_gaji()
        # Pajak 5% jika gaji kotor > 5 juta
        if gaji_kotor > 5_000_000:
            pajak = gaji_kotor * 0.05
        else:
            pajak = 0
        return gaji_kotor - pajak

class KaryawanFreelance(Karyawan):
    def __init__(self, nama, jam_kerja, tarif_per_jam):
        super().__init__(nama)
        self.jam_kerja = jam_kerja
        self.tarif_per_jam = tarif_per_jam

    def hitung_gaji(self):
        return self.jam_kerja * self.tarif_per_jam

    def gaji_bersih(self):
        return self.hitung_gaji()  # freelance tidak kena potongan di soal

# Demonstrasi polimorfisme
karyawan_list = [
    KaryawanTetap("Andi", 6_000_000),
    KaryawanTetap("Budi", 4_000_000),
    KaryawanFreelance("Citra", 100, 50_000)
]

print("=== Sistem Penggajian ===")
for k in karyawan_list:
    print(f"Nama: {k.nama}")
    print(f"Gaji Kotor: Rp{k.hitung_gaji():,.0f}")
    print(f"Gaji Bersih: Rp{k.gaji_bersih():,.0f}")
    print("-" * 30)