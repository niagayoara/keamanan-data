# Alat Cipher

## Deskripsi

Repositori ini berisi berbagai alat enkripsi dan dekripsi menggunakan berbagai algoritma seperti Caesar Cipher, Steganografi, DES, dan Mesin Enigma. Setiap alat dilengkapi dengan antarmuka grafis (GUI) berbasis Python menggunakan pustaka tkinter untuk mempermudah penggunaan.

---

## Daftar Alat

### 1. **Caesar Cipher**
Alat untuk enkripsi dan dekripsi teks menggunakan Caesar Cipher dengan pergeseran tertentu.
- **Input:** Teks yang akan dienkripsi atau didekripsi, nilai pergeseran, mode (enkripsi/dekripsi).
- **Output:** Hasil teks yang telah diproses.
- **Cara Menggunakan:**
  1. Masukkan teks pada kolom input.
  2. Tentukan nilai pergeseran.
  3. Pilih mode "Encrypt" atau "Decrypt".
  4. Klik tombol "Process Text".

---

### 2. **Steganografi**
Alat untuk menyisipkan pesan teks ke dalam gambar (encode) dan membaca pesan tersembunyi dari gambar (decode).
- **Input:**
  - Untuk encode: Gambar dan pesan teks.
  - Untuk decode: Gambar yang telah disisipkan pesan.
- **Output:**
  - Untuk encode: Gambar baru dengan pesan tersembunyi.
  - Untuk decode: Pesan yang disisipkan.
- **Cara Menggunakan:**
  1. Untuk encode:
     - Klik "Encode Message".
     - Pilih gambar.
     - Masukkan pesan.
     - Simpan gambar yang telah diubah.
  2. Untuk decode:
     - Klik "Decode Message".
     - Pilih gambar.
     - Pesan akan muncul di kolom teks.

---

### 3. **DES Encryption**
Alat untuk enkripsi dan dekripsi teks menggunakan algoritma Data Encryption Standard (DES).
- **Input:** Teks yang akan dienkripsi atau didekripsi, kunci sepanjang 8 karakter.
- **Output:**
  - Untuk enkripsi: Teks terenkripsi dalam format Base64.
  - Untuk dekripsi: Teks asli.
- **Cara Menggunakan:**
  1. Masukkan teks pada kolom input.
  2. Masukkan kunci sepanjang 8 karakter.
  3. Klik "Encrypt" untuk enkripsi atau "Decrypt" untuk dekripsi.

---

### 4. **Mesin Enigma**
Simulasi Mesin Enigma untuk enkripsi teks menggunakan tiga rotor.
- **Input:** Teks yang akan dienkripsi, posisi awal ketiga rotor.
- **Output:** Teks terenkripsi.
- **Cara Menggunakan:**
  1. Masukkan teks pada kolom input.
  2. Tentukan posisi awal rotor 1, 2, dan 3.
  3. Klik tombol "Encrypt".

---

## Cara Menjalankan Program
1. Pastikan Python telah terinstal di komputer Anda.
2. Instal pustaka tambahan jika diperlukan:
   ```bash
   pip install pillow pycryptodome
   ```
3. Jalankan file Python yang sesuai dengan alat yang ingin digunakan:
   ```bash
   python nama_file.py
   ```

---

