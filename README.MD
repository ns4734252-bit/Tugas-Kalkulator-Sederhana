![Text Alt](GambarApp.py.png) 

1.*Baris 1*: Bagian ini berfungsi untuk mengimpor (memanggil) alat-alat yang dibutuhkan dari *library* Flask. `Flask` adalah kerangka utama, `render_template` digunakan untuk menampilkan file HTML, dan `request` digunakan untuk mengambil data yang diinput oleh pengguna di halaman web.
2. *Baris 3*: Baris ini membuat sebuah "objek" aplikasi. Variabel `app` ini adalah pusat kendali yang akan mengatur semua jalannya program web Anda.
3.  *Baris 5*: Ini disebut sebagai *route* atau alamat. Simbol `'/'` artinya ini adalah halaman utama. Bagian `methods=['GET', 'POST']` mengizinkan halaman ini untuk dua hal: menampilkan formulir (GET) dan mengirimkan data angka yang diisi (POST).
4. *Baris 6*: Ini adalah awal dari fungsi utama bernama `home()`. Semua logika perhitungan yang Anda buat akan dijalankan di dalam fungsi ini.
5.  *Baris 7–8*: Di sini menyiapkan dua variabel, yaitu `keuntungan` dan `persentase`, dengan nilai awal `None` (kosong). Tujuannya agar saat web pertama kali dibuka, aplikasi tidak langsung memunculkan hasil perhitungan karena pengguna belum memasukkan angka apa pun.
6.  *Baris 10*: Baris ini melakukan pengecekan: "Apakah pengguna baru saja menekan tombol Hitung?". Jika iya (metode POST), maka kode di dalamnya (baris 11-21) akan dieksekusi.
7.  *Baris 12–14*: Bagian ini mengambil angka-angka yang diketik pengguna dari kolom 'modal', 'pendapatan', dan 'biaya' di web. Fungsi `.get(..., 0)` berfungsi sebagai pengaman; jika ada kolom yang lupa diisi, sistem otomatis menganggap nilainya 0 agar program tidak *error*.
8.  *Baris 16*: Ini adalah inti rumus ekonomi Anda. Program menghitung keuntungan dengan cara: *Pendapatan* dikurangi *Biaya*, lalu dikurangi lagi dengan *Modal awal*.
9.  *Baris 18–21*: Ini adalah logika untuk menghitung persentase. Baris 18 memastikan agar nilai `modal` tidak 0 (karena dalam matematika kita tidak bisa membagi angka dengan nol). Jika modal tersedia, baris 19 akan menghitung persentase dan membulatkannya menjadi 2 angka di belakang koma menggunakan fungsi `round()`.
10. *Baris 24*: Baris ini adalah perintah untuk menampilkan kembali halaman `keuntungan.html` sambil membawa hasil perhitungan (`keuntungan` dan `persentase`) agar bisa muncul di layar pengguna.
11. *Baris 26–27*: Ini adalah bagian penutup yang bertugas menyalakan server aplikasi. Dengan perintah `debug=True`, server akan otomatis mendeteksi jika Anda mengubah kodingan dan langsung memperbaruinya tanpa perlu mematikan program secara manual.

---
![Text Alt](KalkulatorPink.png)
http://127.0.0.1:5000

Berikut adalah penjelasan mengenai kalkulator tersebut:

*1. Fungsi Utama*
Kalkulator ini berfungsi untuk menghitung **keuntungan bersih** dan **persentase keuntungan** dari sebuah unit usaha atau proyek secara otomatis melalui antarmuka web.

*2. Komponen Input*
Terdapat tiga kolom utama yang harus diisi oleh pengguna:
* **Modal Awal:** Jumlah uang yang dikeluarkan pertama kali untuk memulai usaha.
* **Total Pendapatan:** Seluruh uang yang diterima dari penjualan atau jasa.
* **Total Biaya:** Pengeluaran operasional (seperti bahan baku, listrik, atau gaji) yang dikeluarkan selama proses berjalan.

*3. Cara Kerja Sistem*
Ketika tombol *"Hitung"* ditekan, aplikasi akan menjalankan logika di balik layar (menggunakan Python Flask) dengan alur sebagai berikut:

1.  *Pengumpulan Data:* Sistem mengambil angka yang di masukkan ke dalam kolom-kolom tersebut.
2.  *Perhitungan Laba:* Sistem menggunakan rumus ekonomi dasar:
    $$\text{Keuntungan} = \text{Pendapatan} - \text{Biaya} - \text{Modal}$$
3.  *Perhitungan Rasio:* Sistem juga menghitung efektivitas modal dengan rumus:
    $$\text{Persentase} = \left( \frac{\text{Keuntungan}}{\text{Modal}} \right) \times 100$$
4.  *Tampilan Hasil:* Angka hasil perhitungan akan muncul kembali di layar tanpa perlu memuat ulang halaman secara manual (jika menggunakan logika *template rendering*).

 *4. Desain Visual (Antarmuka)*
Secara estetika, kalkulator ini menggunakan gaya desain *Card-based UI* dengan sudut yang membulat (*rounded corners*), yang membuatnya terlihat ramah pengguna (user-friendly). Warna gradasi pada latar belakang memberikan kesan yang tenang dan profesional, sangat cocok untuk presentasi tugas akhir atau demonstrasi aplikasi sederhana.

