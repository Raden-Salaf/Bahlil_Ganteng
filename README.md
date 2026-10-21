# Analisis Citra Digital dengan Python

Proyek sederhana untuk tugas mata kuliah **Citra Digital**. Program ini menunjukkan bahwa gambar digital direpresentasikan sebagai nilai numerik pada piksel dan membaca metadata yang tersedia pada file gambar.

## Tujuan

1. Menunjukkan representasi citra sebagai matriks angka.
2. Menampilkan contoh nilai piksel grayscale.
3. Mengekstrak metadata dasar dan metadata EXIF jika tersedia.
4. Menyimpan hasil analisis ke file teks.

## Teknologi

- Python 3
- Pillow: membaca file gambar dan metadata EXIF.
- NumPy: mengubah citra menjadi matriks numerik.
- Matplotlib: menampilkan gambar dan visualisasi nilai piksel.

## Struktur proyek

```text
analisis-citra-digital/
├── main.py
├── requirements.txt
├── README.md
├── gambar_sampel.jpg       # tambahkan gambar milikmu sendiri
├── hasil_analisis.txt      # dibuat otomatis setelah program dijalankan
└── matriks_piksel.txt      # dibuat otomatis setelah program dijalankan
```

## Persiapan di Ubuntu dan VS Code

### 1. Pastikan Python dan pip tersedia

Buka Terminal, lalu jalankan:

```bash
python3 --version
```

Jika Python tersedia, terminal akan menampilkan versi Python. Jika belum tersedia, jalankan:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### 2. Buka folder proyek di VS Code

Buat folder bernama `analisis-citra-digital`, lalu buka folder tersebut di VS Code melalui **File > Open Folder**.

Salin `main.py`, `requirements.txt`, dan `README.md` ke dalam folder itu.

### 3. Buat virtual environment

Buka terminal di VS Code melalui **Terminal > New Terminal**, pastikan terminal berada di folder proyek, lalu jalankan:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Jika perintah `venv` gagal, pasang paket `python3-venv` seperti pada langkah pertama lalu ulangi.

### 4. Instal pustaka yang diperlukan

Dengan virtual environment masih aktif, jalankan:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Tambahkan gambar

Salin satu gambar milikmu ke folder proyek. Contohnya, beri nama `gambar_sampel.jpg`.

Format yang umum digunakan antara lain JPG/JPEG dan PNG. Gunakan gambar yang memang boleh kamu gunakan untuk tugas. Metadata EXIF mungkin tidak ada, terutama pada gambar yang sudah diedit, diunduh dari media sosial, atau disimpan ulang.

### 6. Jalankan program

Di terminal VS Code:

```bash
python main.py
```

Saat diminta nama file, ketik:

```text
gambar_sampel.jpg
```

Jika nama file berbeda, masukkan nama file yang sesuai, termasuk ekstensinya. Program akan menampilkan informasi citra, mencetak contoh matriks angka, dan membuka visualisasi.

## Cara membaca hasil

### A. Membuktikan gambar terdiri dari angka

Program mengubah gambar menjadi grayscale. Setiap piksel grayscale memiliki nilai intensitas dari **0 sampai 255**:

- `0` berarti hitam.
- `255` berarti putih.
- Nilai di antaranya menunjukkan tingkat abu-abu.

Misalnya, jika ukuran gambar adalah 640 × 480 piksel, jumlah pikselnya:

`640 × 480 = 307.200 piksel`

Setelah dikonversi menjadi grayscale, citra direpresentasikan oleh matriks dengan 480 baris dan 640 kolom. Setiap elemen matriks merupakan angka intensitas piksel.

**Catatan:** gambar berwarna biasanya memiliki beberapa kanal, misalnya RGB (merah, hijau, dan biru). Program ini menggunakan citra grayscale untuk membuat contoh matriks lebih mudah dipahami; gambar asli tetap ditampilkan pada visualisasi.

### B. Mengekstrak metadata

Program mencoba membaca informasi berikut:

- Nama dan format file.
- Lebar dan tinggi gambar.
- Mode warna.
- Ukuran file dalam byte.
- Metadata EXIF, apabila tersedia, seperti informasi kamera atau tanggal pengambilan gambar.

Tidak semua gambar mempunyai metadata EXIF. Pesan bahwa EXIF tidak ditemukan bukan berarti program gagal; artinya informasi tersebut memang tidak tersedia atau tidak dapat dibaca dari file itu.

## File hasil keluaran

Setelah program berhasil dijalankan, dua file akan dibuat pada folder proyek:

- **`hasil_analisis.txt`** — ringkasan informasi gambar, bukti numerik, contoh matriks, dan metadata EXIF yang ditemukan.
- **`matriks_piksel.txt`** — matriks intensitas grayscale lengkap, satu baris teks untuk setiap baris piksel.

Visualisasi yang muncul berisi gambar asli, citra grayscale, dan contoh 10 × 10 piksel beserta angka intensitasnya.

## Contoh hasil (ilustrasi)

Angka di bawah hanya ilustrasi. Hasil sebenarnya bergantung pada gambar yang kamu analisis.

```text
Format          : JPEG
Dimensi         : 640 x 480 piksel
Mode warna      : RGB
Bentuk matriks  : (480, 640)
Jumlah piksel   : 307200
Nilai minimum   : 0
Nilai maksimum  : 255
```

Contoh matriks:

```text
[[ 12  15  18  22]
 [ 14  17  20  25]
 [ 19  21  26  31]
 [ 23  27  32  36]]
```

Nilai contoh tersebut tidak mewakili gambar tertentu. Matriks hasil program bisa berbeda.

## Kesimpulan

Gambar digital dapat direpresentasikan sebagai data numerik. Pada citra grayscale, setiap piksel memiliki nilai intensitas 0–255. Program membuktikannya dengan mengubah gambar menjadi matriks NumPy, menampilkan sebagian nilai piksel, dan menyimpan matriks lengkap ke file teks. Program juga membaca metadata dasar serta EXIF apabila tersedia.

## Deskripsi singkat untuk repositori GitHub

> Program Python untuk analisis citra digital yang menampilkan representasi gambar sebagai matriks angka piksel, memvisualisasikan citra grayscale, dan mengekstrak metadata dasar serta EXIF menggunakan Pillow, NumPy, dan Matplotlib. Dibuat untuk pembelajaran mata kuliah Citra Digital.

## Catatan

Jangan mengunggah gambar pribadi atau gambar yang memiliki metadata sensitif ke repositori publik. Kamu bisa menambahkan `gambar_sampel.jpg` ke `.gitignore` jika tidak ingin mengunggah gambar tersebut.
