# Panduan Penulisan Proposal PDF (Maks. 15 Halaman)

Dokumen ini membedah standar format resmi dan strategi penulisan 8 komponen wajib proposal untuk **GTNIC 2026 - Kategori AI Agent Development**.

Prinsip Utama (Slide 10 Technical Meeting):
> *"Jelaskan arsitektur dan alasan di balik keputusan teknis, bukan hanya tampilan akhir."*

---

## 1. Spesifikasi Format Fisik Dokumen

Proposal yang melanggar aturan format fisik dapat dikenai penalti nilai administrasi oleh dewan juri. Pastikan seluruh ketentuan berikut terpenuhi:

* **Format File:** Portable Document Format (**PDF**)
* **Batas Tebal:** **Maksimal 15 Halaman** (sudah termasuk halaman judul/cover, daftar isi, pembahasan, dan lampiran)
* **Ukuran Kertas:** **A4** (210 mm x 297 mm)
* **Jenis & Ukuran Font:** **Times New Roman, 12 pt** (Judul/sub-judul dapat disesuaikan hirarkinya, misal 14 pt bold)
* **Spasi Antar Baris:** **1.5 spasi**
* **Aturan Margin:**
  * Margin Kiri: **4 cm** (standar penjilidan resmi)
  * Margin Atas: **3 cm**
  * Margin Kanan: **3 cm**
  * Margin Bawah: **3 cm**
* **Bahasa:** Bahasa Indonesia atau Bahasa Inggris baku
* **Ketentuan Cover:** **Wajib mencantumkan Logo Resmi GTNIC 2026**
* **Standar Penamaan Berkas:** **`GTNIC2026_AIAgent_NamaTim.pdf`**

---

## 2. Bedah Taktis 8 Komponen Wajib Isi Proposal

### Komponen 01: Judul Karya & Nama Tim (Alokasi: Cover & Hal. 1)
* **Judul Karya:** Buat judul yang mencerminkan fungsi teknis agen dan sektor industri sasaran secara jelas.
  * *Contoh Lemah:* "Penerapan AI untuk Perusahaan"
  * *Contoh Kuat:* "AUDITBOT: Autonomous Enterprise Financial Audit & Procurement Reconciliation Agent Berbasis Multi-Tool Reasoning"
* **Profil Tim:** Cantumkan nama lengkap ketua dan anggota, asal institusi/kampus, peran spesifik dalam tim (misal: AI Engineer, Backend & Cloud Architect, Domain/Data Specialist), dan kontak resmi.

### Komponen 02: Latar Belakang Masalah Enterprise/Industry (Alokasi: Hal. 2 - 3)
* Paparkan masalah operasional nyata yang dihadapi divisi tertentu di perusahaan (misal divisi finance, logistik, atau TI).
* Sertakan data/fakta industri: berapa jam kerja yang terbuang untuk verifikasi manual, berapa potensi kerugian akibat human error, dan mengapa otomasi konvensional (rule-based) gagal menangani variasi data tidak terstruktur.

### Komponen 03: Tujuan, Manfaat & Solusi Otomatisasi (Alokasi: Hal. 4)
* **Tujuan:** Sasaran spesifik yang dicapai oleh agen (misal: memangkas waktu verifikasi dokumen dari 40 menit menjadi 15 detik dengan akurasi 99%).
* **Solusi Otomatisasi:** Jelaskan bagaimana kecerdasan agen mentransformasikan proses manual menjadi alur kerja mandiri (autonomous workflow).
* **Manfaat:** Peningkatan produktivitas karyawan, eliminasi fraud transaksi, dan ketersediaan jejak audit (audit trail) otomatis.

### Komponen 04: Target Perusahaan atau Pengguna (Alokasi: Hal. 5)
* **Profil Industri Sasaran:** Klasifikasikan skala dan sektor enterprise yang menjadi target (misal: Retail Supply Chain, Perbankan/Fintech, B2B SaaS, atau Manufaktur).
* **Persona Pengguna:** Definisikan persona user yang akan terbantu langsung oleh agen (misal: Finance Operations Officer, Procurement Manager, atau IT Incident Responder).

### Komponen 05: Arsitektur Sistem (Alur / RAG, Tech Stack, API) (Alokasi: Hal. 6 - 9)
*Ini adalah bagian paling berbobot dalam evaluasi proposal (bagian dari 70% nilai teknis).*
* **Diagram Arsitektur Tingkat Tinggi (High-Level Architecture):** Gambarkan pemisahan antara Presentation Layer (Dashboard), Agent Engine (Planner & Reasoning Loop), Tool Layer (Database, External API, File Parser), dan Knowledge Layer (RAG Vector Store).
* **Alur Penalaran (Reasoning Loop):** Jelaskan implementasi siklus ReAct (Thought > Action > Observation) atau state graph yang memandu agen mengambil keputusan secara otonom.
* **Mekanisme RAG (Jika Digunakan):** Paparkan alur ingestion dokumen SOP/regulasi, chunking strategy, embedding model yang dipilih, dan cara agen mengutip klausul dokumen.
* **Tabel Tech Stack & Justifikasi:** Sebutkan model LLM, backend framework (FastAPI/Python), vector store, dan database yang dipakai beserta alasan rasional pemilihannya.
* **Katalog API & Tools:** Rincikan daftar tool eksternal yang terhubung dengan agen (nama tool, fungsi, input payload, output schema).

### Komponen 06: Fitur Utama & Metrik Efisiensi (Alokasi: Hal. 10 - 11)
* **Rincian Fitur Inti:** Jelaskan kemampuan fungsional utama agen saat menangani kasus bisnis nyata.
* **Tabel Komparasi Metrik Efisiensi (Wajib Kuantitatif):**

| Parameter Evaluasi | Proses Manual Tradisional | Dengan AI Agent (Hasil Uji) | Tingkat Efisiensi |
| :--- | :--- | :--- | :--- |
| **Waktu Pemrosesan per Transaksi** | 30 - 45 Menit | 8 - 15 Detik | Peningkatan kecepatan > 98% |
| **Akurasi Verifikasi Dokumen** | 88% - 92% (Human Error) | 99.2% (Validated Schema) | Penurunan error rate drastis |
| **Biaya Operasional per 1.000 Dokumen** | Rp 15.000.000 (Gaji/Jam Kerja) | ~ Rp 150.000 (Token API) | Penghematan biaya ~ 90% |
| **Ketergantungan Intervensi User** | 100% Manual | 0% (Kecuali kasus eskalasi anomali) | Otonomi penuh |

### Komponen 07: Batasan Sistem & Mitigasi Risiko (Alokasi: Hal. 12 - 13)
* **Batasan Sistem (Boundary & Edge Cases):** Nyatakan secara transparan batas kemampuan agen (misal: tidak menangani persetujuan pencairan dana di atas limit tertentu tanpa verifikasi multi-faktor direksi).
* **Mitigasi Halusinasi AI:** Penggunaan output skema ketat (Pydantic validation) dan temperature rendah pada model.
* **Keamanan Data & Privasi Enterprise:** Mekanisme penyamaran data sensitif (data masking pada nomor rekening/PII) sebelum dikirim ke API model.
* **Fallback Mechanism:** Apa yang dilakukan agen jika API pihak ketiga down atau data tidak ditemukan (agen mencoba tool alternatif atau menghasilkan laporan status pending secara aman).

### Komponen 08: Screenshot Antarmuka & Future Development (Alokasi: Hal. 14 - 15)
* **Tangkapan Layar Antarmuka Publik:** Sertakan screenshot antarmuka web live demo yang memperlihatkan:
  * Form input tugas operasional.
  * Visualisasi log pemikiran agen (*Thought stream & Tool Calls*).
  * Laporan akhir atau dokumen hasil keluaran sistem.
* **Roadmap Future Development:** Petakan rencana pengembangan 6 - 12 bulan ke depan (misal: integrasi multi-agent collaboration, integrasi langsung ke sistem ERP SAP/Oracle, dan self-learning capability).
