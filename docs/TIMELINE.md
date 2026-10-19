# Timeline & Action Plan Harian (19 Oktober - 14 November 2026)

Total durasi: 23 hari kerja menuju submission + 4 hari menuju Grand Final.

---

### Fase 1: Problem Definition, Tech Stack, & Scaffolding (19 - 22 Oktober)
* **19 Okt (Hari Ini):**
  * Kunci rumusan masalah operasional enterprise (use case target).
  * Tentukan nama tim dan identitas proyek.
  * Inisialisasi repo GitHub publik `aiagentdev` & dokumentasi dasar.
* **20 Okt:**
  * Setup environment project backend & konfigurasi dependency.
  * Rancang arsitektur ReAct / Plan-and-Execute state loop.
  * Siapkan sample dataset mock enterprise (dokumen/database mock).
* **21 Okt:**
  * Definisikan tool interface yang dibutuhkan agen (schema input & output).
  * Implementasi prompt system dasar, memory buffer, dan safety bounds.
* **22 Okt:**
  * Verifikasi milestone Fase 1: Arsitektur selesai dan skenario uji end-to-end terpetakan.

---

### Fase 2: Core Engine, Tool Calling, & Guardrails (23 - 28 Oktober)
* **23 Okt:**
  * Implementasi Tool 1: Data Querying / Document Parser (PDF/CSV/XLSX).
  * Unit testing tool secara deterministik tanpa LLM.
* **24 Okt:**
  * Implementasi Tool 2 & 3: Action Execution (API call, report generator, webhook trigger).
* **25 Okt:**
  * Integrasi ReAct Loop: LLM memecah tugas, menentukan urutan tool, dan mengeksekusi secara otonom.
* **26 Okt:**
  * Integrasi RAG: Embedding & retriever untuk regulasi/SOP perusahaan.
* **27 Okt:**
  * Implementasi Guardrails & Structured Output:
    * Validasi skema output via Pydantic.
    * Fallback mechanism jika API tool timeout atau data kosong.
* **28 Okt:**
  * Benchmark performa: ukur akurasi reasoning, latency, dan tingkat otonomi tanpa campur tangan user.

---

### Fase 3: Dashboard Interface & Public Deployment (29 Oktober - 2 November)
* **29 Okt:**
  * Setup project frontend (dashboard monitoring agen).
  * Buat layout UI: task input, live thought trace, log tool calls, dan download output report.
* **30 Okt:**
  * Integrasi streaming logs (WebSocket / SSE) agar alur reasoning agen terlihat berjalan live.
* **31 Okt:**
  * Polish UI/UX: status loading, visual badges, error boundary, dark/light modern tech aesthetic.
* **01 Nov:**
  * Deployment backend & frontend ke hosting publik (Railway / Vercel / VPS).
  * Konfigurasi domain / HTTPS publik.
* **02 Nov:**
  * Testing menyeluruh: cek stabilitas server, sanitasi environment variable, dan uji multi-device.

---

### Fase 4: Penulisan Dokumen Proposal (3 - 6 November)
* **03 Nov:**
  * Setup template dokumen sesuai format resmi (A4, TNR 12, Spasi 1.5, Margin 4-3-3-3).
  * Tulis Bab 1 - 4: Judul/Tim, Latar Belakang Masalah, Tujuan & Solusi, Target Pengguna.
* **04 Nov:**
  * Tulis Bab 5: Arsitektur Sistem lengkap, diagram alur RAG, diagram alur reasoning, integrasi API.
* **05 Nov:**
  * Tulis Bab 6 - 7: Fitur Utama, Tabel Metrik Efisiensi vs Manual, Batasan Sistem & Mitigasi Risiko.
* **06 Nov:**
  * Tulis Bab 8: Screenshot UI Antarmuka & Roadmap Future Development.
  * Proofreading, cek batas maksimal 15 halaman, ekspor ke `GTNIC2026_AIAgent_NamaTim.pdf`.

---

### Fase 5: Produksi Video Walkthrough Demo (7 - 8 November)
* **07 Nov:**
  * Penyusunan skrip video demo (durasi 3 - 5 menit):
    * 00:00 - 00:45: Intro tim & problem statement.
    * 00:45 - 02:45: Live interactive demo (agen menyelesaikan tugas otomatisasi nyata).
    * 02:45 - 03:45: Penjelasan arsitektur teknis di balik layar.
    * 03:45 - 04:15: Dampak efisiensi bisnis & closing.
  * Rekam screen capture flow kerja agen dengan audio jernih.
* **08 Nov:**
  * Editing video: tambahkan callout tools, percepat proses loading statis, export 1080p.
  * Unggah ke YouTube (Unlisted/Public) atau Google Drive (akses publik: anyone with link).

---

### Fase 6: Final Verification & Submission (9 - 10 November)
* **09 Nov (Hari Submit Target):**
  * Tanda tangan Surat Pernyataan Keaslian Karya.
  * Verifikasi semua link publik (web UI, repo GitHub, video YouTube/Drive).
  * Submit seluruh berkas ke Google Form resmi GTNIC 2026.
  * Ambil tangkapan layar bukti submit.
* **10 Nov (Deadline Resmi 23.59 WIB):**
  * Buffer day darurat. Monitor uptime server publik.

---

### Fase 7: Grand Final & Exhibition (11 - 14 November)
* **11 - 12 Nov:** Pantau pengumuman Top 5 Finalis (12 Nov).
* **13 Nov:** Susun 10-slide deck presentasi live pitching & gladi bersih via Zoom.
* **14 Nov:** Hari H Grand Final & Live Pitching di depan juri.
