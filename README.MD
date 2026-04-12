![Text Alt](Gambarappy.png) 
Tentu, kita buat bahasanya lebih profesional tapi tetap ringan dan mudah dimengerti ya. Ini penjelasan per nomor bagian kodenya:

*Nomor 1-3*
Bagian ini adalah tahap persiapan atau impor *library*. Kita memanggil **Flask** sebagai kerangka kerja web, **render_template_string** untuk memproses tampilan halaman, dan **request** untuk menangkap data yang diinput oleh pengguna. Baris `app = Flask(__name__)` berfungsi untuk menginisialisasi atau membuat objek aplikasi agar sistem web bisa mulai berjalan.

*Nomor 5-8*
Di sini kita menentukan alamat atau *route* website. Simbol `'/'` menandakan bahwa ini adalah halaman utama. Di dalam fungsi `home()`, kita menyiapkan dua variabel, yaitu `keuntungan` dan `persentase`, dengan nilai awal `None`. Hal ini dilakukan agar saat halaman pertama kali dibuka, sistem sudah memiliki wadah untuk menyimpan hasil perhitungan nantinya.

*Nomor 10-13*
Bagian ini bertugas memproses input saat pengguna menekan tombol hitung (metode `POST`). Program akan mengambil nilai yang dimasukkan ke dalam kolom 'modal', 'pendapatan', dan 'biaya'. Penggunaan fungsi `float()` sangat penting di sini untuk mengubah teks yang diketik pengguna menjadi angka desimal agar bisa diproses secara matematis oleh komputer.

*Nomor 15-20*
Ini adalah inti dari logika perhitungan ekonominya. Program akan menghitung selisih antara pendapatan dengan total biaya dan modal untuk mendapatkan angka keuntungan. Selain itu, terdapat pengecekan kondisi: jika modal lebih dari nol, sistem akan menghitung rasio persentase keuntungannya. Fungsi `round(..., 2)` digunakan agar hasilnya lebih rapi dengan membatasi hanya dua angka di belakang koma.

*Nomor 22*
Setelah perhitungan selesai, baris ini berfungsi untuk mengirimkan kembali hasil tersebut ke tampilan pengguna. Variabel `keuntungan` dan `persentase` yang sudah berisi angka hasil hitungan akan dimasukkan ke dalam struktur HTML sehingga bisa langsung dibaca oleh pengguna melalui *browser* mereka.

*Nomor 24-25*
Bagian terakhir ini berfungsi sebagai instruksi untuk menjalankan aplikasi. Perintah `app.run(debug=True)` akan mengaktifkan server lokal sehingga website bisa diakses. Fitur `debug=True` sangat membantu dalam proses pengembangan karena aplikasi akan memberikan laporan otomatis jika terdapat kesalahan pada kode yang perlu diperbaiki.

![Text Alt](GambarKalkulator.png) 
Tampilan pada gambar tersebut adalah antarmuka (UI) sederhana dari aplikasi **Kalkulator Keuntungan Usaha** yang saya buat menggunakan Flask. Berikut adalah penjelasan bagian-bagiannya:

---

*1. Judul Utama (Header)*
Di bagian atas terdapat tulisan **"Kalkulator Keuntungan Usaha"**. Ini berfungsi sebagai identitas halaman agar pengguna langsung tahu bahwa fungsi utama alat ini adalah untuk menghitung profit atau laba dari sebuah bisnis.

*2. Kolom Input (Data Masukan)*
Terdapat tiga kotak putih yang harus diisi oleh pengguna dengan angka:
*Modal Awal (Rp):*Tempat untuk memasukkan jumlah uang yang dikeluarkan di awal untuk memulai usaha atau stok barang.
*Pendapatan (Rp):* Tempat untuk memasukkan total uang yang diterima dari hasil penjualan.
*Biaya Operasional (Rp):* Tempat untuk memasukkan biaya tambahan lainnya, seperti ongkir, listrik, atau kemasan.

*3. Tombol Eksekusi (Hitung)*
Di bagian paling bawah ada tombol lebar bertuliskan *"Hitung"*. Ketika tombol ini diklik, data yang sudah diisi di kotak-kotak tadi akan dikirim ke mesin Flask (kode Python yang kita bahas sebelumnya) untuk diproses menggunakan rumus matematika.

*4. Desain dan Tampilan*
Tampilan ini menggunakan gaya yang bersih dengan kotak putih besar yang memiliki bayangan halus (*soft shadow*) di pinggirnya agar terlihat menonjol. Sudut-sudut kotaknya juga dibuat melengkung (*rounded*) agar terlihat lebih modern dan nyaman di mata, tidak kaku seperti aplikasi jadul.

---


