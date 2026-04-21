Cara kerja kode praktikum 1: transportasi
Jadi gini, pertama saya bikin class induk namanya Kendaraan. Di dalamnya ada method berjalan() yang sengaja saya kosongin (abstract). Terus saya buat anak-anaknya: Mobil, Motor, Pesawat, dan Kapal. Masing-masing saya kasih method berjalan() dengan isi yang beda. Misal mobil tulisnya "berjalan di aspal", pesawat "terbang di udara". Saya juga masukin atribut kecepatan biar outputnya lebih hidup.

Langkah selanjutnya, saya buat satu list besar. Isinya objek-objek dari keempat class tadi, lengkap dengan nama dan kecepatan masing-masing. Nah, waktu saya loop list itu dan panggil berjalan(), Python otomatis nyari method berjalan() sesuai dengan jenis objek aslinya. Saya tidak perlu nulis if isinstance(mobil, Mobil) atau semacamnya. Ini yang dinamakan polimorfisme. Kodenya jadi pendek dan rapi.

Cara kerja kode praktikum 2: penggajian
Di sini saya buat class Karyawan sebagai bapaknya. Anaknya ada dua: KaryawanTetap dan KaryawanFreelance. Masing-masing punya cara hitung gaji yang beda.

Untuk yang tetap, saya kasih aturan: kalau gaji bulanan di atas 5 juta, dapat bonus 10%. Terus setelah dapat bonus, kalau totalnya masih di atas 5 juta, dipotong pajak 5%. Saya buat dua method: hitung_gaji() buat ngasih gaji kotor (sudah sama bonus), dan gaji_bersih() buat ngurangin pajak.

Untuk freelance, method hitung_gaji() cuma mengalikan jam kerja dengan tarif, dan gaji_bersih() sama nilainya karena tidak ada potongan.

Pas di main program, saya masukin beberapa karyawan ke satu list, lalu saya loop. Saya panggil hitung_gaji() dan gaji_bersih() untuk setiap karyawan. Hasilnya beda-beda sesuai aturan masing-masing. Di sini polimorfismenya kelihatan banget karena saya pakai method yang sama tapi eksekusinya beda tergantung objeknya.

Cara kerja kode praktikum 3: sistem gudang
Ini yang paling panjang dan agak rumit. Saya buat class Barang sebagai dasar. Lalu BarangElektronik (punya garansi) dan BarangKonsumsi (punya tanggal kadaluarsa). Setiap class saya kasih method info() buat nampilin data, dan to_dict() buat nyiapin data sebelum disimpan ke file JSON.

Yang bikin khas di sini: pas nyimpan, saya masukin key "tipe" yang isinya nama class asli, misal "BarangElektronik". Kenapa? Karena pas nanti saya buka file JSON-nya lagi, program harus tahu barang itu termasuk jenis apa. Kalau cuma nyimpen nama dan harga, nanti bingung.

Pas load data, saya baca file JSON, lalu untuk setiap item saya cek nilai "tipe". Kalau elektronik, saya bikin objek BarangElektronik. Kalau konsumsi, bikin BarangKonsumsi. Kalau tidak ada tipe, saya anggap barang biasa.

Kemudian di bagian laporan, saya tinggal loop semua barang dan panggil info(). Tanpa if-else, barang elektronik otomatis nampilin garansi, barang konsumsi nampilin kadaluarsa. Ini polimorfisme yang paling berguna menurut saya.

Cara kerja validasi tanggal kadaluarsa (tugas praktikum)
Perintahnya: buat fitur cek kadaluarsa. Saya kerjain di class BarangKonsumsi, tepatnya di method info().

Pertama, saya ambil tanggal hari ini dari sistem pakai datetime.now().date(). Lalu saya ubah string tanggal kadaluarsa (format YYYY-MM-DD) jadi bentuk tanggal juga. Saya bandingkan: kalau kadaluarsa lebih kecil dari hari ini, berarti sudah expired, status saya kasih "EXPIRED". Kalau masih lebih besar, saya hitung selisihnya berapa hari, terus saya kasih tulisan "masih berlaku, sisa X hari".

Saya juga bungkus dengan try-except untuk jaga-jaga kalau format tanggal yang dimasukkan salah. Misal nulis "2025/12/31" pakai garis miring, nanti programnya tidak error tapi kasih peringatan.

Hasilnya, waktu saya tampilkan daftar barang, untuk Roti yang kadaluarsa tahun 2023, muncul tulisan "EXPIRED". Untuk Susu yang masih lama, muncul sisa harinya.
