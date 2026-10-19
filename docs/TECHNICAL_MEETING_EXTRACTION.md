# Ekstraksi Lengkap Video Technical Meeting GTNIC 2026

Dokumen ini berisi transkrip terstruktur, rincian slide per slide, dan instruksi penting dari rekaman video **Technical Meeting Garda Tech National Innovation Competition (GTNIC) 2026 - Kategori AI Agent Development** (`D:\Downloads\AI AGENT .mp4`, durasi 24 menit 38 detik, diselenggarakan 18 Oktober 2026).

---

## 1. Metadata Sesi & Penyelenggara

* **Nama Acara:** Garda Tech National Innovation Competition 2026 (GTNIC 2026)
* **Penyelenggara:** Garda Tech
* **Kategori Kompetisi:** AI Agent Development
* **Sub-tema:** Enterprise Productivity
* **Fokus Utama:** Enterprise & Industry
* **Tanggal TM:** 18 Oktober 2026
* **Masa Pengerjaan:** 19 Oktober - 10 November 2026
* **Format Sesi:** Virtual Meeting (Presentasi Slide Deck 16 Slide + Sesi Tanya Jawab / Q&A)

---

## 2. Bedah Seluruh Slide Presentasi (Slide 01 - 16)

### Slide 01 / 16: Title & Opening
* **Timestamp:** 00:00 - 00:30
* **Judul:** TECHNICAL MEETING - AI AGENT DEVELOPMENT
* **Sub-judul:** Building Intelligent AI Agents for Enterprise Productivity
* **Visual Alur (Agent / Workflow Demo):**
  * Input Tugas (User Prompt): *"Rekap order yang tertunda lalu kirim ke tim finance"*
  * Tahap 1 - **Reasoning:** Memecah tugas jadi 3 langkah otomatis.
  * Tahap 2 - **Tool Call:** Query data pesanan dari database.
  * Tahap 3 - **Action:** Kirim laporan otomatis ke sistem finance.
  * Status: *"Selesai tanpa intervensi manual"*
* **Pesan Utama:** AI Agent bukan chatbot tanya-jawab, melainkan pekerja digital otonom yang mampu bernalar, memanggil tools, dan menuntaskan alur kerja operasional.

---

### Slide 02 / 16: Competition Overview
* **Timestamp:** 00:30 - 02:00
* **Judul:** Competition overview
* **Deskripsi:** Kompetisi yang menantang peserta membangun AI Agent untuk kebutuhan perusahaan dan industri.
* **Our Mission:** *"From manual workflows to autonomous agents"* - Peserta membangun AI Agent yang mampu bernalar, memakai tools, dan menyelesaikan pekerjaan operasional nyata.
* **Tiga Pilar:**
  1. Kategori: AI Agent Development
  2. Fokus: Enterprise & Industry
  3. Kelolosan: Top 5 melaju ke Grand Final

---

### Slide 03 / 16: Competition Context & Transition
* **Timestamp:** 02:00 - 02:05
* **Transisi Pembahasan:** Masuk ke lingkup tantangan industri dan studi kasus yang dapat diangkat oleh peserta.

---

### Slide 04 / 16: Scope & Challenge
* **Timestamp:** 02:05 - 04:30
* **Judul:** Scope & challenge
* **Arahan Utama:** *"Pilih masalah operasional yang jelas, lalu bangun agent yang menyelesaikannya."*
* **Tiga Klaster Tantangan (Tantangan):**
  1. Mengotomatisasi pekerjaan (Workflow automation)
  2. Menganalisis data (Data analytics & insight extraction)
  3. Meningkatkan efisiensi operasional (Operational efficiency boost)
* **Enam Contoh Projek Acuan (Contoh Projek):**
  * **01 - AI Customer Service Assistant** (Otomasi tiket, resolusi komplain, routing dinamis)
  * **02 - AI Sales Assistant** (Lead qualification, follow-up proposal, CRM update)
  * **03 - AI Recruitment Agent** (Screening CV, pencocokan skill, penjadwalan interview)
  * **04 - AI Finance Assistant** (Audit invoice, rekonsiliasi kas/PO, laporan keuangan)
  * **05 - AI Data Analyst Agent** (Query otomatis DB, visualisasi trend, laporan anomali)
  * **06 - AI Document Processing Agent** (Ekstraksi OCR, validasi kepatuhan hukum/kontrak)

---

### Slide 05 / 16: Competition Timeline
* **Timestamp:** 04:35 - 05:35
* **Judul:** Competition timeline
* **Sub-judul:** *"Catat tanggal penting berikut agar pengerjaan dan pengumpulan berjalan tepat waktu."*
* **Periode Pengerjaan Karya:** **19 OKTOBER — 10 NOVEMBER 2026**
* **Milestone Jadwal:**
  * **18 OKT:** Technical Meeting (Pembahasan teknis)
  * **19 OKT:** Mulai Pengerjaan Karya
  * **10 NOV:** **Deadline Submission (23.59 WIB)** - Batas akhir submit berkas
  * **12 NOV:** Pengumuman Top 5 Finalis kategori
  * **14 NOV:** Grand Final & Exhibition (Online via Zoom)

---

### Slide 06 / 16: Competition Rules
* **Timestamp:** 05:40 - 06:35
* **Judul:** Competition rules
* **Sub-judul:** *"Ketentuan dasar yang harus dipatuhi setiap peserta dan tim sepanjang kompetisi."*
* **Enam Aturan Pokok:**
  1. **Individu atau Tim:** Tim beranggotakan 1 - 3 orang; diperbolehkan lintas institusi.
  2. **Satu Karya per Tim:** Setiap tim hanya boleh mengirimkan 1 karya AI Agent.
  3. **Tema Wajib Sesuai:** Sub-tema Enterprise Productivity, fokus Enterprise & Industry.
  4. **Karya Orisinal:** 100% buatan sendiri, belum pernah dipublikasikan atau memenangkan lomba lain.
  5. **Komposisi Tim Tetap:** Anggota tidak dapat diganti setelah pendaftaran selesai.
  6. **Output Aman:** Keluaran dilarang memuat SARA, pornografi, kekerasan, atau konten provokatif.
* **Peringatan Resmi:** *"Pelanggaran ketentuan, termasuk plagiarisme atau berkas tidak sesuai, dapat berujung diskualifikasi."*

---

### Slide 07 / 16: Technical Requirements
* **Timestamp:** 06:35 - 08:00
* **Judul:** Technical requirements
* **Sub-judul:** *"Teknologi bebas, tetapi AI Agent harus memiliki fungsi nyata dan dapat diakses publik."*
* **Spesifikasi Teknis yang Diperbolehkan:**
  * **Teknologi Bebas:** Bebas menggunakan LLM/API apapun (OpenAI, Gemini, Anthropic, open-source), framework (LangChain, LlamaIndex, kustom), atau low-code platform (n8n, Flowise). Seluruh arsitektur harus dijelaskan di proposal.
  * **Fitur Lanjut Wajib (Minimal Memiliki 1 Fitur Aktif):**
    1. *Reasoning dan perencanaan langkah* (Multi-step reasoning & planning)
    2. *Integrasi API atau tool calling* untuk mengambil data maupun menjalankan aksi nyata
    3. *RAG (Retrieval-Augmented Generation)* untuk mencari dan menggunakan informasi dari dokumen/basis pengetahuan internal
  * **Deployment Publik:** Interface web AI Agent harus dapat diakses publik secara daring, disertai link demo live dan repo GitHub publik (atau shareable workflow link).
* **LARANGAN KERAS (DILARANG):**
  * **Chatbot yang Hanya Membungkus API LLM ("ChatGPT Wrapper")**
  * Submisi yang hanya meneruskan prompt pengguna ke API LLM dan mengembalikan jawaban teks tanpa logika kustom, eksekusi tool, atau kapabilitas penyelesaian masalah **tidak memenuhi kriteria lomba**.

---

### Slide 08 / 16: Expected Deliverables
* **Timestamp:** 08:05 - 08:50
* **Judul:** Expected deliverables
* **Sub-judul:** *"Empat output utama yang perlu disiapkan dan diserahkan melalui formulir resmi."*
* **Empat Output Utama:**
  1. **01 | Live Interface:** Tautan antarmuka web AI Agent yang dapat diakses publik.
  2. **02 | Repo / Workflow:** Repositori GitHub publik, atau tautan workflow jika menggunakan low-code.
  3. **03 | Proposal PDF:** Dokumen tertulis yang menjelaskan masalah, arsitektur sistem, dan solusi.
  4. **04 | Video Demo:** Video berdurasi 3 - 5 menit berisi walkthrough dan live interactive demo agen.
* **Dokumen Pendukung Wajib:**
  * **SURAT PERNYATAAN KEASLIAN KARYA** (Wajib ditandatangani dan diunggah).

---

### Slide 09 / 16: Recommended Build Process
* **Timestamp:** 08:50 - 09:30
* **Judul:** Recommended build process
* **Sub-judul:** *"Alur ilustratif untuk menghubungkan masalah, arsitektur, dan hasil akhir agent."*
* **Enam Tahapan Pengerjaan Disarankan:**
  1. **01 PROBLEM:** Identifikasi masalah operasional enterprise yang spesifik.
  2. **02 ARCHITECTURE:** Rancang alur logika reasoning, RAG pipeline, dan tech stack.
  3. **03 BUILD:** Integrasikan LLM, tool/function calling, dan integrasi API.
  4. **04 GUARDRAILS:** Bangun mitigasi halusinasi, proteksi kebocoran data, dan fallback.
  5. **05 DEPLOY:** Deploy UI publik, uji live demo, dan rapikan repositori.
  6. **06 DOCUMENT:** Tulis proposal, hitung metrik efisiensi, dan rekam video demo.
* **Catatan Juri:** *Alur ini sebagai panduan kerja; yang wajib ada dalam proposal adalah arsitektur teknis dan mitigasi risiko.*

---

### Slide 10 / 16: Proposal Document Guidelines
* **Timestamp:** 09:30 - 09:40
* **Judul:** Proposal document
* **Prinsip Utama:** *"Jelaskan arsitektur dan alasan di balik keputusan teknis, bukan hanya tampilan akhir."*
* **Format Fisik Dokumen:**
  * Format File: **PDF**
  * Batas Tebal: **Maksimal 15 Halaman**
  * Ukuran Kertas: **A4**
  * Huruf: **Times New Roman, 12 pt**
  * Spasi: **1.5**
  * Margin: **Kiri 4 cm, Atas 3 cm, Kanan 3 cm, Bawah 3 cm**
  * Bahasa: **Bahasa Indonesia atau Bahasa Inggris**
  * Cover: **Wajib mencantumkan logo GTNIC 2026**
* **Delapan Komponen Wajib Isi Proposal:**
  * **01:** Judul karya & nama tim
  * **02:** Latar belakang masalah Enterprise/Industry
  * **03:** Tujuan, manfaat & solusi otomatisasi
  * **04:** Target perusahaan atau pengguna
  * **05:** Arsitektur sistem (alur logika / RAG, tech stack, API)
  * **06:** Fitur utama & metrik efisiensi (komparasi kuantitatif)
  * **07:** Batasan sistem & mitigasi risiko
  * **08:** Screenshot antarmuka & future development

---

### Slide 11 / 16: Video Demonstration Guidelines
* **Timestamp:** 09:40 - 10:20
* **Judul:** Video demonstration
* **Sub-judul:** *"Bantu juri memahami masalah, solusi, dan cara kerja agent melalui demonstrasi singkat."*
* **Ketentuan Durasi & Platform:**
  * Durasi: **3 — 5 MENIT**
  * Platform Unggah: **YouTube / Google Drive (Wajib Akses Publik)**
* **Empat Bagian Alur Video yang Harus Dicakup:**
  * **01:** Perkenalan singkat anggota tim.
  * **02:** Latar belakang masalah industri & solusi AI (diperbolehkan pitching).
  * **03:** **Demo interaktif agent menyelesaikan tugas otomatisasi secara live** (Fokus utama video).
  * **04:** Penjelasan singkat arsitektur AI di balik layar.

---

### Slide 12 / 16: Submission Guidelines
* **Timestamp:** 10:20 - 11:40
* **Judul:** Submission guidelines
* **Sub-judul:** *"Kumpulkan seluruh berkas melalui Google Form resmi sebelum batas waktu pengumpulan."*
* **Deadline Pengumpulan:** **10 NOVEMBER 2026, 23.59 WIB**
* **Ketentuan Nama File Proposal:**
  * **`GTNIC2026_AIAgent_NamaTim.pdf`**
  * Logo GTNIC 2026 wajib ada di cover.
* **Lima Berkas yang Wajib Diserahkan di Form:**
  1. Nama tim (diisi pada Google Form)
  2. Link live interface / web AI Agent
  3. Link repo GitHub publik atau workflow low-code
  4. Proposal PDF & link video demo (akses publik)
  5. Surat pernyataan keaslian karya

---

### Slide 13 / 16: Judging Criteria & Scoring Weight
* **Timestamp:** 11:40 - 12:55
* **Judul:** Judging criteria
* **Sub-judul:** *"Bobot resmi penilaian AI Agent dalam kompetisi GTNIC 2026."*
* **TOTAL 100% | 70% BOBOT PADA KEMAMPUAN TEKNIS AGENT:**
  1. **Kapabilitas dan Otonomi Agen (25%):** Kemampuan agen bekerja mandiri memproses input hingga output final tanpa campur tangan manusia.
  2. **Penalaran, Perencanaan & Keputusan (15%):** Logika ReAct/planning dalam memecah tugas kompleks menjadi tahapan terstruktur.
  3. **Penggunaan Alat & Eksekusi Tindakan (15%):** Keakuratan pemilihan dan pemanggilan tool untuk mengambil data dan aksi sistem.
  4. **Arsitektur Teknis & Rekayasa Sistem (15%):** Kebersihan arsitektur, modularitas, guardrails terhadap error, dan keamanan.
  5. **Inovasi dan Kreativitas (10%):** Kebaruan ide dalam menyelesaikan problem enterprise dibanding automasi konvensional.
  6. **Dampak Masalah dan Nilai Bisnis (10%):** Kuantifikasi nilai bisnis nyata (penghematan jam kerja, biaya, penurunan error rate).
  7. **Pengalaman & Kemudahan Pengguna (5%):** UX dashboard, kejelasan status eksekusi agen, visualisasi step.
  8. **Demonstrasi, Presentasi & Dokumentasi (5%):** Kerapian proposal dan kejelasan video demo.

---

### Slide 14 / 16: Competition Stages & Final Pitching
* **Timestamp:** 12:55 - 13:10
* **Judul:** Competition stages & final pitching
* **Sub-judul:** *"Dua tahap utama: seleksi karya secara daring dan presentasi langsung bagi finalis."*
* **Struktur Tahapan:**
  * **STAGE 01: BABAK PENYISIHAN (Online Evaluation)**
    * Evaluasi berkas Proposal, Karya akhir & live interface, serta Video demonstrasi.
  * **STAGE 02: GRAND FINAL (TOP 5 FINALISTS)**
    * Waktu: **14 November 2026**
    * Format: Live pitching online via Zoom di hadapan dewan juri.
    * Agenda: Presentasi dan live interactive demo di depan juri.

---

### Slide 15 / 16: Final Checklist & Common Mistakes
* **Timestamp:** 13:10 - 13:25
* **Judul:** Final checklist & common mistakes
* **Sub-judul:** *"Lakukan pemeriksaan terakhir sebelum menekan tombol Submit pada Google Form."*
* **CHECK BEFORE SUBMIT:**
  * [x] Karya sesuai sub-tema & fokus industri.
  * [x] Fitur lanjut (reasoning / tool calling / RAG) berfungsi live.
  * [x] Proposal & video sesuai format resmi (PDF max 15 hal, video 3-5 menit).
  * [x] Link live demo & repositori GitHub sudah berstatus PUBLIK.
  * [x] Surat keaslian karya dan nama tim sudah dilampirkan.
* **AVOID THESE MISTAKES (Kesalahan Fatal):**
  * [!] Link live demo tidak dapat diakses / broken link.
  * [!] Repositori GitHub masih berstatus PRIVATE saat dinilai juri.
  * [!] Hanya chatbot wrapper tanpa integrasi tool / RAG.
  * [!] Proposal tidak memuat diagram arsitektur teknis dan metrik kuantitatif.
  * [!] Pengumpulan melewati deadline (lewat 10 November 23.59 WIB).

---

### Slide 16 / Sesi Q&A & Penutupan
* **Timestamp:** 13:30 - 24:38
* **Visual:** Slide interaktif 3D mascot "Q&A session" dilanjutkan sesi tanya jawab via Zoom bersama panitia dan peserta.
* **Poin Penting Tanya Jawab:**
  * *Pertanyaan Model/API:* Penggunaan model komersial (GPT-4o, Claude, Gemini) maupun open-source lokal (Llama, Mistral) diperbolehkan asal biaya API ditanggung peserta dan alur tool call bekerja nyata.
  * *Pertanyaan Tim:* Batas maksimal 3 orang, diperbolehkan mahasiswa aktif atau peserta independen sesuai ketentuan umum.
  * *Pertanyaan Hosting:* Peserta bebas memilih platform hosting demo (Vercel, Render, Railway, HuggingFace Spaces, VPS) selama URL dapat diakses langsung oleh juri tanpa login berbayar.
