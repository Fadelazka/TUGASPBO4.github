from datetime import datetime

class Barang:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def info(self):
        return f"{self.nama} - Harga: Rp{self.harga}"

    def to_dict(self):
        return {
            "tipe": self.__class__.__name__,  # identitas kelas asal
            "nama": self.nama,
            "harga": self.harga
        }

class BarangElektronik(Barang):
    def __init__(self, nama, harga, masa_garansi):
        super().__init__(nama, harga)
        self.masa_garansi = masa_garansi  # dalam bulan

    def info(self):
        return f"{super().info()}, Garansi: {self.masa_garansi} bulan"

    def to_dict(self):
        data = super().to_dict()
        data["masa_garansi"] = self.masa_garansi
        return data

class BarangKonsumsi(Barang):
    def __init__(self, nama, harga, tgl_kadaluarsa):
        super().__init__(nama, harga)
        self.tgl_kadaluarsa = tgl_kadaluarsa  # string format YYYY-MM-DD

    def info(self): 
        # Tugas Praktikum: validasi tanggal kadaluarsa
        today = datetime.now().date()
        exp_date = datetime.strptime(self.tgl_kadaluarsa, "%Y-%m-%d").date()
        if exp_date < today:
            status = " (EXPIRED - sudah kadaluarsa!)"
        else:
            sisa = (exp_date - today).days
            status = f" (masih berlaku, sisa {sisa} hari)"
        return f"{super().info()}, Kadaluarsa: {self.tgl_kadaluarsa}{status}"

    def to_dict(self):
        data = super().to_dict()
        data["tgl_kadaluarsa"] = self.tgl_kadaluarsa
        return data