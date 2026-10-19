# Panduan & Skrip Video Demo (3 - 5 Menit)

Panduan terstruktur untuk memproduksi video demonstrasi karya yang memikat dewan juri sesuai ketentuan resmi **Slide 11 Technical Meeting GTNIC 2026**.

---

## 1. Spesifikasi Teknis Video
* **Durasi Video:** **3 hingga 5 Menit** (Ideal: 4 menit 15 detik. Dilarang kurang dari 3 menit atau melebihi 5 menit).
* **Resolusi:** Minimal **1080p (Full HD)**, rasio layar **16:9 widescreen**.
* **Audio:** Suara narasi jernih tanpa noise latar belakang.
* **Platform Unggah:** **YouTube** (Visibilitas: Unlisted atau Public) atau **Google Drive** (Hak Akses: *Anyone with the link can view / Siapa saja yang memiliki link dapat melihat*).
* **Verifikasi Sebelum Submit:** Wajib dites buka tautan video melalui jendela Incognito untuk memastikan video tidak terkunci privasi akun.

---

## 2. Struktur 4 Bagian Alur Video (Mandatory Flow)

Sesuai arahan panitia, alur video wajib mencakup 4 bagian berikut:

```text
00:00 - 00:45  [Bagian 1] : Perkenalan Singkat Anggota Tim & Nama Karya
00:45 - 01:30  [Bagian 2] : Latar Belakang Masalah Industri & Nilai Solusi
01:30 - 03:45  [Bagian 3] : Live Interactive Demo Agen Menyelesaikan Tugas (Fokus Inti)
03:45 - 04:30  [Bagian 4] : Penjelasan Arsitektur AI di Balik Layar
04:30 - 04:50  [Penutup]   : Dampak Efisiensi Bisnis & Kalimat Penutup
```

---

## 3. Skrip Storyboard Per Detik (Word-for-Word Guide)

### Bagian 1: Perkenalan Tim & Identitas Karya (00:00 - 00:45)
* **Visual:** Kamera webcam pembicara atau slide pembuka berlogo resmi GTNIC 2026.
* **Narasi Skrip:**
  > *"Halo dewan juri GTNIC 2026 yang terhormat. Kami dari Tim [Nama Tim] mempersembahkan [Nama Karya/Agen], sebuah solusi Autonomous AI Agent untuk kategori Enterprise Productivity. Saya [Nama Ketua] bersama rekan saya [Nama Anggota]. Di era otomasi cerdas saat ini, kami hadir untuk mengubah alur kerja operasional enterprise yang sebelumnya lambat dan manual menjadi eksekusi otonom yang cepat, presisi, dan terverifikasi."*

### Bagian 2: Latar Belakang Masalah Industri (00:45 - 01:30)
* **Visual:** B-roll / ilustrasi tumpukan invoice tidak teratur, tabel data error, atau proses manual staf yang memakan waktu.
* **Narasi Skrip:**
  > *"Di sektor enterprise dan industri, proses verifikasi operasional seperti audit invoice, rekonsiliasi purchase order, dan pengecekan regulasi internal memakan waktu hingga puluhan jam setiap bulannya. Tim operasional rentan mengalami human error yang berujung pada selisih bayar dan kebocoran finansial. Automasi berbasis aturan biasa gagal menangani dokumen yang tidak terstruktur. Oleh karena itu, kami mengembangkan agen cerdas yang tidak hanya mengerti instruksi bahasa alami, tetapi juga mampu bernalar, memanggil tools sistem, dan mengeksekusi tindakan secara mandiri."*

### Bagian 3: Live Interactive Demo (01:30 - 03:45) - *Sorotan Utama*
* **Visual:** Perekaman layar (screen capture) dashboard web publik agen secara langsung.
* **Tindakan 1 (Input Tugas):** Pembicara memasukkan instruksi bisnis ke formulir tugas dan mengunggah sampel invoice anomali.
* **Narasi Skrip:**
  > *"Sekarang mari kita lihat agen kami bekerja secara live. Di sini kami memberikan tugas operasional: 'Lakukan audit kepatuhan terhadap invoice pengadaan nomor INV-2026-09, cocokkan dengan database Purchase Order, dan verifikasi kepatuhan SOP perusahaan'."*
* **Tindakan 2 (Visualisasi Thought Stream & Tool Calls):** Kamera menyorot panel status log real-time.
* **Narasi Skrip:**
  > *"Perhatikan panel visualisasi reasoning di layar. Agen tidak langsung menebak jawaban. Pertama, agen memecah tugas menjadi empat rencana kerja logis. Agen kemudian memanggil Tool 1, yaitu File Parser untuk mengekstrak data item dan nominal dari dokumen PDF. Setelah itu, agen memanggil Tool 2, yakni Database Query Tool untuk menarik data Purchase Order resmi nomor PO-8812."*
* **Tindakan 3 (Deteksi Anomali & Eksekusi Aksi):** Log menunjukkan agen menemukan selisih harga dan mengutip klausul SOP.
* **Narasi Skrip:**
  > *"Dari hasil komparasi, agen menemukan adanya selisih markup harga sebesar Rp 4.500.000 pada item server storage. Agen langsung memanggil RAG Knowledge Base untuk mengecek SOP Pengadaan Pasal 4 Ayat 2 mengenai batas toleransi harga. Karena melebihi batas toleransi, agen secara otonom memanggil Tool 3: membekukan status pembayaran, menghasilkan file Berita Acara Audit resmi dalam format PDF, dan menembakkan alert darurat ke sistem webhook finance. Seluruh siklus ini tuntas hanya dalam 12 detik tanpa satu pun intervensi manual!"*

### Bagian 4: Penjelasan Arsitektur Teknis (03:45 - 04:30)
* **Visual:** Tampilan diagram arsitektur tingkat tinggi dan diagram ReAct loop yang bersih.
* **Narasi Skrip:**
  > *"Di balik antarmuka ini, agen kami dibangun dengan arsitektur ReAct (Reasoning and Acting) berbasis FastAPI dan model LLM mutakhir. Arsitektur kami memisahkan antara Orchestrator Planner, Tool Execution Layer, dan Guardrails Validator. Kami mengimplementasikan validasi skema output berbasis Pydantic untuk mengeliminasi halusinasi, serta mekanisme circuit breaker jika koneksi API eksternal terganggu. Ini memastikan agen beroperasi aman dan andal di lingkungan produksi enterprise."*

### Penutup & Dampak Bisnis (04:30 - 04:55)
* **Visual:** Tampilan tabel metrik efisiensi dan logo tim/kontak penutup.
* **Narasi Skrip:**
  > *"Melalui implementasi agen ini, perusahaan mampu memangkas waktu proses audit sebesar 98% dan menekan risiko kerugian finansial hingga 0%. Inilah inovasi otonom nyata dari kami untuk produktivitas enterprise Indonesia yang lebih unggul. Terima kasih dan salam inovasi!"*

---

## 4. Tips Produksi Video Berkualitas Juara
1. **Hindari Jeda Hening (Dead Air):** Saat sistem sedang memproses data selama 2-3 detik, isi narasi dengan menjelaskan apa yang sedang dilakukan agen di latar belakang.
2. **Gunakan Callout Visual:** Berikan panah atau kotak sorotan berwarna pada video saat tombol tool dipanggil atau status reasoning berubah.
3. **Pencahayaan Webcam:** Jika menampilkan wajah pembicara di sudut layar (Picture-in-Picture), pastikan wajah terang dan memakai pakaian rapi / almamater institusi.
4. **Verifikasi Tautan:** Simpan tautan YouTube dan cadangan Google Drive di catatan pengumpulan.
