from barang import BarangElektronik, BarangKonsumsi
from gudang_manager import GudangManager

# Inisialisasi manager
manager = GudangManager("gudang.json")

# Tambah beberapa barang contoh
manager.tambah_barang(BarangElektronik("Laptop", 8_000_000, 12))
manager.tambah_barang(BarangKonsumsi("Susu", 20_000, "2025-12-31"))
manager.tambah_barang(BarangKonsumsi("Roti", 15_000, "2023-01-01"))  # sudah expired

# Muat data (untuk membuktikan penyimpanan dan pemuatan cerdas)
manager.muat_data()
manager.tampilkan_semua()