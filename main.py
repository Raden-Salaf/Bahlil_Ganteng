from pathlib import Path
from PIL import Image, ExifTags
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=" * 60)
    print("PROGRAM ANALISIS CITRA DIGITAL")
    print("1. Membuktikan bahwa citra direpresentasikan dengan angka")
    print("2. Mengekstrak metadata gambar")
    print("=" * 60)

    nama_file = input(
        "\nMasukkan nama file gambar (contoh: gambar_sampel.jpg): "
    ).strip()

    if not nama_file:
        nama_file = "bahlil_ganteng.jpg"

    path_gambar = Path(nama_file)

    if not path_gambar.exists():
        print(f"\nFile '{path_gambar}' tidak ditemukan.")
        print("Letakkan gambar di folder proyek yang sama dengan main.py,")
        print("lalu jalankan program lagi dengan nama file yang benar.")
        return

    try:
        with Image.open(path_gambar) as gambar:
            gambar.load()

            print("\n--- HASIL ANALISIS CITRA ---")
            print(f"Nama file       : {path_gambar.name}")
            print(f"Format          : {gambar.format}")
            print(f"Dimensi         : {gambar.width} x {gambar.height} piksel")
            print(f"Mode warna      : {gambar.mode}")
            print(f"Ukuran file     : {path_gambar.stat().st_size:,} byte")

            # Mengubah citra menjadi grayscale agar setiap piksel
            # diwakili satu angka intensitas 0 sampai 255.
            gambar_gray = gambar.convert("L")
            matriks = np.array(gambar_gray)

            print("\n--- BUKTI CITRA BERUPA ANGKA ---")
            print(f"Bentuk matriks  : {matriks.shape}")
            print(f"Jumlah piksel   : {matriks.size:,}")
            print(f"Nilai minimum   : {matriks.min()}")
            print(f"Nilai maksimum  : {matriks.max()}")
            print("\nContoh matriks piksel grayscale (maksimal 10 x 10):")
            print(matriks[:10, :10])

            # Simpan metadata dan contoh matriks ke file teks.
            hasil = []
            hasil.append("HASIL ANALISIS CITRA DIGITAL")
            hasil.append("=" * 40)
            hasil.append(f"Nama file: {path_gambar.name}")
            hasil.append(f"Format: {gambar.format}")
            hasil.append(f"Dimensi: {gambar.width} x {gambar.height} piksel")
            hasil.append(f"Mode warna asli: {gambar.mode}")
            hasil.append(f"Ukuran file: {path_gambar.stat().st_size:,} byte")
            hasil.append("")
            hasil.append("BUKTI NUMERIK")
            hasil.append(f"Bentuk matriks grayscale: {matriks.shape}")
            hasil.append(f"Jumlah piksel: {matriks.size:,}")
            hasil.append(f"Nilai minimum: {matriks.min()}")
            hasil.append(f"Nilai maksimum: {matriks.max()}")
            hasil.append("Contoh matriks piksel (maksimal 10 x 10):")
            hasil.append(np.array2string(matriks[:10, :10]))

            # Baca metadata EXIF jika tersedia.
            exif_data = gambar.getexif()
            hasil.append("")
            hasil.append("METADATA EXIF")
            if exif_data:
                nama_tag = {tag_id: nama for nama, tag_id in ExifTags.TAGS.items()}
                ada_metadata = False
                for tag_id, nilai in exif_data.items():
                    nama = nama_tag.get(tag_id, str(tag_id))
                    hasil.append(f"{nama}: {nilai}")
                    ada_metadata = True
                if not ada_metadata:
                    hasil.append("Tidak ada metadata EXIF yang dapat dibaca.")
            else:
                hasil.append("Tidak ditemukan metadata EXIF pada gambar ini.")

            Path("hasil_analisis.txt").write_text(
                "\n".join(hasil), encoding="utf-8"
            )
            print("\nMetadata dan ringkasan hasil disimpan ke: hasil_analisis.txt")

            # Simpan matriks grayscale lengkap agar angka-angka piksel
            # bisa diperiksa secara terpisah.
            np.savetxt("matriks_piksel.txt", matriks, fmt="%d")
            print("Matriks piksel lengkap disimpan ke: matriks_piksel.txt")

            # Tampilkan citra asli, citra grayscale, dan contoh nilai piksel.
            gambar_rgb = gambar.convert("RGB")
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))
            axes[0].imshow(gambar_rgb)
            axes[0].set_title("Gambar Asli")
            axes[0].axis("off")

            axes[1].imshow(matriks, cmap="gray", vmin=0, vmax=255)
            axes[1].set_title("Citra Grayscale")
            axes[1].axis("off")

            contoh = matriks[:10, :10]
            axes[2].imshow(contoh, cmap="gray", vmin=0, vmax=255)
            axes[2].set_title("Contoh 10 x 10 Piksel")
            for baris in range(contoh.shape[0]):
                for kolom in range(contoh.shape[1]):
                    warna_teks = "white" if contoh[baris, kolom] < 128 else "black"
                    axes[2].text(
                        kolom, baris, str(contoh[baris, kolom]),
                        ha="center", va="center", fontsize=7,
                        color=warna_teks
                    )
            axes[2].set_xticks(range(contoh.shape[1]))
            axes[2].set_yticks(range(contoh.shape[0]))
            axes[2].set_title("Nilai Piksel (0-255)")

            plt.tight_layout()
            plt.show()

    except Exception as error:
        print(f"\nTerjadi kesalahan saat membaca gambar: {error}")
        print("Pastikan file gambar valid dan formatnya didukung.")

if __name__ == "__main__":
    main()
