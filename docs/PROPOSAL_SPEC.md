# Spesifikasi Dokumen Proposal GTNIC 2026

Berdasarkan pedoman Slide 10 Technical Meeting GTNIC 2026:
> *"Jelaskan arsitektur dan alasan di balik keputusan teknis, bukan hanya tampilan akhir."*

---

## 1. Aturan Format Dokumen
* **Jenis File:** PDF
* **Batas Halaman:** Maksimal 15 halaman (termasuk lampiran/gambar)
* **Ukuran Kertas:** A4
* **Font:** Times New Roman, ukuran 12 pt
* **Spasi:** 1.5
* **Margin:**
  * Kiri: 4 cm
  * Atas: 3 cm
  * Kanan: 3 cm
  * Bawah: 3 cm
* **Bahasa:** Bahasa Indonesia atau Bahasa Inggris
* **Cover:** Wajib memuat Logo Resmi GTNIC 2026
* **Penamaan File:** `GTNIC2026_AIAgent_NamaTim.pdf`

---

## 2. Struktur 8 Komponen Wajib Proposal

### 01. Judul Karya & Nama Tim
* Judul inovasi yang spesifik mencerminkan fungsi agen dan industri sasaran.
* Susunan anggota tim, asal institusi, dan peran masing-masing.

### 02. Latar Belakang Masalah Enterprise/Industry
* Masalah operasional konkret yang dihadapi perusahaan saat ini.
* Bukti/fakta bahwa proses manual memakan banyak waktu, rentan human error, atau berbiaya tinggi.

### 03. Tujuan, Manfaat & Solusi Otomatisasi
* Tujuan pengembangan AI Agent.
* Manfaat strategis yang ditawarkan dibanding otomasi berbasis aturan biasa (rule-based automation).

### 04. Target Perusahaan atau Pengguna
* Profil industri sasaran (misal: logistik, keuangan, layanan konsumen, TI).
* Persona user di dalam enterprise yang akan berinteraksi dengan agen.

### 05. Arsitektur Sistem (Alur / RAG, Tech Stack, API)
* Diagram arsitektur sistem tingkat tinggi.
* Penjelasan workflow penalaran (reasoning loop / state graph).
* Mekanisme RAG (jika ada): ingestion, chunking, embedding, vector retrieval.
* Tech stack yang dipilih dan alasan pemilihan teknologinya.
* Daftar API eksternal dan tool calling yang diintegrasikan.

### 06. Fitur Utama & Metrik Efisiensi
* Rincian fitur otonom agen.
* Tabel komparasi metrik efisiensi: Proses Manual vs AI Agent (waktu pengerjaan, akurasi, biaya operasional).

### 07. Batasan Sistem & Mitigasi Risiko
* Batasan lingkup kemampuan agen (edge cases).
* Guardrails teknis untuk mitigasi halusinasi model AI.
* Proteksi data sensitif dan error recovery ketika eksekusi tool gagal.

### 08. Screenshot Antarmuka & Future Development
* Tangkapan layar antarmuka dashboard live yang menampilkan alur kerja agen.
* Roadmap rencana pengembangan jangka panjang pasca kompetisi.
