import json
from barang import BarangElektronik, BarangKonsumsi

class GudangManager:
    def __init__(self, file_json="gudang.json"):
        self.file_json = file_json
        self.daftar_barang = []

    def simpan_data(self):
        data = [b.to_dict() for b in self.daftar_barang]
        with open(self.file_json, "w") as f:
            json.dump(data, f, indent=4)

    def muat_data(self):
        try:
            with open(self.file_json, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            self.daftar_barang = []
            return

        self.daftar_barang = []
        for item in data:
            tipe = item.get("tipe")
            if tipe == "BarangElektronik":
                barang = BarangElektronik(
                    item["nama"],
                    item["harga"],
                    item["masa_garansi"]
                )
            elif tipe == "BarangKonsumsi":
                barang = BarangKonsumsi(
                    item["nama"],
                    item["harga"],
                    item["tgl_kadaluarsa"]
                )
            else:
                continue  # skip jika tipe tidak dikenal
            self.daftar_barang.append(barang)

    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)
        self.simpan_data()

    def tampilkan_semua(self):
        print("\n=== Daftar Barang di Gudang ===")
        for b in self.daftar_barang:
            print(b.info())  # POLIMORFISME: otomatis pilih info() yang tepat