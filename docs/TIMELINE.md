# Master Timeline & Daily Goals (19 Oktober - 14 November 2026)

Dokumen ini memetakan rencana kerja harian secara presisi untuk memenangkan **Garda Tech National Innovation Competition (GTNIC) 2026 - Kategori AI Agent Development**.

Total durasi: **23 Hari Kerja (Pengerjaan Karya) + 4 Hari (Grand Final Prep)**.

---

## FASE 1: Problem Definition, Data Mock, & Scaffolding (19 - 22 Oktober)
*Target: Mengunci use case enterprise bernilai tinggi, menyiapkan mock dataset realistis, dan setup arsitektur dasar.*

### 19 Oktober (Hari Ini) - Domain Lock & Setup Repo
* **Goal:** Repositori siap, seluruh acuan lomba terdokumentasi di repo, dan use case industri terkunci.
* **Aksi:**
  1. Inisialisasi repo GitHub publik `kycjojo/aiagentdev`.
  2. Dokumentasikan seluruh ekstraksi video Technical Meeting, aturan lomba, dan spesifikasi proposal.
  3. Kunci 1 domain use case operasional enterprise (contoh: Autonomous Finance & Procurement Audit Agent).
* **Output Verifikasi:** Commit dan push ke GitHub berhasil, dokumen panduan lengkap di folder `docs/`.

### 20 Oktober - Data Schema & Mock Enterprise Dataset
* **Goal:** Menyiapkan skenario uji data riil yang akan dipecahkan oleh agen.
* **Aksi:**
  1. Buat folder `data/` dengan sampel dokumen operasional: 5 invoice mock (format teks/PDF), 1 database transaksi PO (SQLite/JSON), dan 1 berkas SOP pengadaan barang/jasa.
  2. Masukkan kasus uji spesifik: transaksi normal, selisih nominal (anomali harga), dan vendor mencurigakan.
* **Output Verifikasi:** Script parser lokal mampu membaca seluruh file mock tanpa gagal.

### 21 Oktober - Tool Interface & System Prompt Engineering
* **Goal:** Merancang kontrak antarmuka 3 tools utama dan system prompt ReAct agen.
* **Aksi:**
  1. Tulis skema Pydantic untuk input/output tool di `src/tools/base.py`.
  2. Rancang system prompt yang mewajibkan loop ReAct (Thought > Action > Observation) dengan batasan peran enterprise.
* **Output Verifikasi:** Unit test schema tool berhasil tereksekusi tanpa type error.

### 22 Oktober - Tracer Test & Review Fase 1
* **Goal:** Agen mampu menerima user request dan mengembalikan alur tahapan kerja (execution plan).
* **Aksi:**
  1. Buat test runner `tests/test_planner.py`.
  2. Uji agen dengan kalimat instruksi kompleks; pastikan agen memecah tugas menjadi minimal 3 langkah logis.
* **Output Verifikasi:** Log terminal menampilkan breakdown langkah kerja secara berurutan.

---

## FASE 2: Core Engineering, Tools, RAG & Guardrails (23 - 28 Oktober)
*Target: Mengamankan 70% bobot teknis juri (Otonomi 25%, Reasoning 15%, Tool Use 15%, Arsitektur 15%).*

### 23 Oktober - Tool 1: Data Query & Document Ingestion
* **Goal:** Agen mampu mengekstrak data dari dokumen/database secara terstruktur.
* **Aksi:**
  1. Implementasi tool pembaca file invoice dan query data pesanan/pembelian.
  2. Normalisasi data mentah menjadi format JSON standar (nomor PO, nama vendor, tanggal, item barang, subtotal, pajak).
* **Output Verifikasi:** Tool 1 berhasil mengekstrak 100% data kunci dari file sampel secara mandiri.

### 24 Oktober - Tool 2 & 3: Action Execution & Reconciliation
* **Goal:** Agen mampu memvalidasi silang data dan mengeksekusi aksi/notifikasi nyata.
* **Aksi:**
  1. Implementasi Tool 2: Verifikasi silang nominal PO vs tagihan invoice vs bukti mutasi.
  2. Implementasi Tool 3: Action Dispatcher (generate ringkasan PDF laporan audit & kirim webhook notifikasi status).
* **Output Verifikasi:** Tool 3 mampu meng-output file laporan hasil rekonsiliasi dan webhook mock terpanggil.

### 25 Oktober - The ReAct Autonomous Loop
* **Goal:** LLM secara otonom memilih dan mengeksekusi tools dalam loop dinamis sampai tugas tuntas.
* **Aksi:**
  1. Rangkai loop ReAct: LLM mengamati output Tool 1, menganalisis selisih/anomali, memanggil Tool 2, lalu mengeksekusi Tool 3.
  2. Buat mekanisme deteksi "Stop Condition" saat seluruh tugas telah selesai.
* **Output Verifikasi:** Diberikan 1 prompt perintah, agen mengeksekusi ketiga tools berurutan secara otonom tanpa intervensi manual.

### 26 Oktober - Integrasi RAG (Knowledge Base Perusahaan)
* **Goal:** Setiap keputusan agen diselaraskan dengan SOP dan regulasi industri.
* **Aksi:**
  1. Indexing SOP pengadaan / regulasi keuangan internal ke vector store atau keyword retriever.
  2. Agen wajib menyertakan sitasi aturan SOP ketika menolak invoice atau mendeteksi pelanggaran prosedur.
* **Output Verifikasi:** Output rekomendasi agen menyertakan kutipan klausul SOP yang akurat.

### 27 Oktober - Guardrails & Self-Correction (Arsitektur Tahan Banting)
* **Goal:** Sistem kebal halusinasi dan mampu menangani kegagalan tool (fallback mechanism).
* **Aksi:**
  1. Pasang output validation Pydantic di setiap tahapan LLM.
  2. Pasang exception handling jika tool timeout atau data tidak ditemukan (agen mencoba jalur alternatif atau menyatakan batasan secara jujur).
* **Output Verifikasi:** Uji skenario input rusak/anomali ekstrem; sistem tidak crash dan mencatat error log dengan rapi.

### 28 Oktober - Benchmark & Evaluasi Metrik
* **Goal:** Menghasilkan data angka kuantitatif untuk Bab 6 dokumen proposal.
* **Aksi:**
  1. Jalankan benchmark pada 20 variasi kasus bisnis.
  2. Ukur: Success Rate (%), Rata-rata Latensi (detik), dan Estimasi Penghematan Waktu vs Manual.
* **Output Verifikasi:** Tabel metrik performa siap disematkan ke dalam proposal.

---

## FASE 3: Web Dashboard Interface & Public Deployment (29 Oktober - 2 November)
*Target: Aplikasi memiliki UI modern dan live di internet dengan URL publik yang stabil.*

### 29 Oktober - Setup Frontend Dashboard
* **Goal:** Antarmuka web enterprise interaktif siap digunakan.
* **Aksi:**
  1. Inisialisasi frontend dashboard (Next.js / Vite React).
  2. Rancang komponen: panel input tugas bisnis, selector preset data uji, dan panel hasil audit.
* **Output Verifikasi:** UI berjalan lokal dan responsif di desktop maupun layar kecil.

### 30 Oktober - Real-Time Thought & Tool Calling Stream
* **Goal:** Pengunjung/juri dapat melihat langkah pemikiran agen secara real-time.
* **Aksi:**
  1. Hubungkan backend FastAPI ke frontend via Server-Sent Events (SSE) / WebSocket.
  2. Tampilkan badge status ketika agen sedang: `Reasoning`, `Calling Tool: [Nama Tool]`, `Observing`, dan `Finalizing`.
* **Output Verifikasi:** Alur kerja agen muncul secara bertahap di UI saat tugas dieksekusi.

### 31 Oktober - Polish UI/UX & Fitur Download Laporan
* **Goal:** Tampilan dashboard terlihat profesional, bersih, dan berstandar komersial.
* **Aksi:**
  1. Sempurnakan desain visual (dark/light clean corporate theme).
  2. Tambahkan tombol unduh laporan hasil eksekusi (format PDF/JSON).
* **Output Verifikasi:** User dapat mengunduh dokumen laporan hasil audit langsung dari antarmuka web.

### 01 November - Deployment Backend & Frontend ke Publik
* **Goal:** Seluruh sistem aktif di internet dengan URL publik.
* **Aksi:**
  1. Deploy backend API ke Railway / Render / VPS.
  2. Deploy frontend ke Vercel / Cloudflare Pages.
  3. Konfigurasi HTTPS, CORS, dan environment variables production.
* **Output Verifikasi:** URL publik dapat diakses dengan respons status HTTP 200 OK.

### 02 November - Public Stability & Cross-Device Testing
* **Goal:** Memastikan tidak ada bug koneksi bagi penguji luar.
* **Aksi:**
  1. Uji akses URL publik melalui Incognito Mode, jaringan seluler, dan browser berbeda.
  2. Uji skenario stres ringan untuk memastikan API tidak timeout.
* **Output Verifikasi:** Seluruh alur demo agen berjalan mulus di URL publik tanpa error console.

---

## FASE 4: Penulisan Proposal PDF (Maks. 15 Halaman) (3 - 6 November)
*Target: Menghasilkan dokumen proposal resmi sesuai 8 komponen wajib GTNIC 2026.*

### 03 November - Setup Format & Bab 1 - 4
* **Goal:** Format margin 4-3-3-3, font TNR 12 pt, spasi 1.5, dan 4 bab awal rampung.
* **Aksi:** Tulis Bab 1 (Judul & Profil Tim), Bab 2 (Latar Belakang Masalah Industri), Bab 3 (Tujuan & Solusi Otomatisasi), Bab 4 (Target Pengguna).
* **Output Verifikasi:** 4 halaman awal selesai ditulis dengan bahasa profesional dan berbasis fakta industri.

### 04 November - Bab 5: Arsitektur Sistem & Alur Penalaran
* **Goal:** Membedah rekayasa teknis sistem agen secara mendalam.
* **Aksi:**
  1. Masukkan diagram arsitektur tingkat tinggi (High-Level Architecture).
  2. Gambarkan diagram alur ReAct loop, integrasi tools, pipeline RAG, dan tabel tech stack.
* **Output Verifikasi:** Diagram sistem resolusi tinggi dan penjelasan teknis tertata rapi di dokumen.

### 05 November - Bab 6 & 7: Metrik Efisiensi & Mitigasi Risiko
* **Goal:** Menyajikan bukti kuantitatif efisiensi sistem dan keandalan mitigasi.
* **Aksi:**
  1. Tampilkan tabel komparasi: Proses Manual vs AI Agent (waktu pengerjaan, akurasi, biaya).
  2. Rinci batasan sistem (edge cases) dan arsitektur guardrails penanganan kegagalan.
* **Output Verifikasi:** Tabel metrik hasil benchmark 28 Oktober tertuang lengkap di Bab 6.

### 06 November - Bab 8, Final Proofreading, & Export PDF
* **Goal:** Proposal final siap submit tanpa pelanggaran batas halaman.
* **Aksi:**
  1. Masukkan tangkapan layar antarmuka live dashboard dan roadmap future development.
  2. Cek total halaman (harus <= 15 halaman termasuk cover & lampiran).
  3. Ekspor ke file: `GTNIC2026_AIAgent_NamaTim.pdf`.
* **Output Verifikasi:** Berkas PDF dicek ulang margin, nomor halaman, dan keberadaan logo GTNIC 2026 pada cover.

---

## FASE 5: Produksi Video Walkthrough Demo (7 - 8 November)
*Target: Video demonstrasi 3 - 5 menit yang to-the-point dan meyakinkan juri.*

### 07 November - Skrip Terstruktur & Screen Recording
* **Goal:** Rekaman walkthrough demo interaktif agen menyelesaikan tugas bisnis secara live.
* **Aksi:**
  1. Buat skrip ketat durasi 3 - 5 menit:
     * 00:00 - 00:45: Pembukaan, perkenalan tim, dan latar belakang masalah industri.
     * 00:45 - 02:45: Demo interaktif live (eksekusi prompt, pemikiran agen, pemanggilan tool, hasil akhir).
     * 02:45 - 03:45: Penjelasan arsitektur teknis di balik layar.
     * 03:45 - 04:15: Nilai bisnis, dampak efisiensi, dan penutup.
  2. Rekam layar dengan audio bersih dan resolusi tajam (1080p).
* **Output Verifikasi:** Video mentah berdurasi 4 menit dengan audio penjelasan yang jernih.

### 08 November - Video Editing & Upload Publik
* **Goal:** Video selesai diedit dan dapat diakses publik di YouTube / Google Drive.
* **Aksi:**
  1. Beri callout visual saat tool dipanggil dan percepat bagian pemrosesan statis.
  2. Render video format MP4 1080p.
  3. Upload ke YouTube (status: Unlisted/Public) dan siapkan mirror link di Google Drive (Akses: Siapa saja yang memiliki link).
* **Output Verifikasi:** Link video dites buka lewat Incognito Window dan dapat diputar lancar.

---

## FASE 6: Final Verification & Early Submission (9 - 10 November)
*Target: Mengirimkan seluruh berkas 24 jam sebelum deadline resmi untuk mitigasi risiko teknis.*

### 09 November (HARI SUBMIT UTAMA) - Submit Google Form
* **Goal:** Seluruh berkas resmi terkirim melalui formulir panitia.
* **Aksi:**
  1. Pastikan repo GitHub `kycjojo/aiagentdev` berstatus **PUBLIC** dan file rahasia/API key bersih.
  2. Tanda tangani Surat Pernyataan Keaslian Karya (scan ke PDF).
  3. Buka Google Form resmi GTNIC 2026, isi:
     * Nama Tim
     * Link Live Interface Web
     * Link Repositori GitHub Publik
     * Upload File Proposal PDF (`GTNIC2026_AIAgent_NamaTim.pdf`)
     * Link Video Demo (YouTube/Drive publik)
     * Upload Surat Pernyataan Keaslian Karya
  4. Submit formulir dan simpan tangkapan layar bukti submit.
* **Output Verifikasi:** Bukti tanda terima formulir Google Form tersimpan aman.

### 10 November - Buffer Day (Deadline Resmi 23.59 WIB)
* **Goal:** Hari tenang tanpa kepanikan teknis.
* **Aksi:** Pantau server live demo agar tetap up dan berjalan normal. Tidak melakukan perubahan kode besar.
* **Output Verifikasi:** Seluruh tautan tetap aktif dan dapat dibuka oleh pihak luar.

---

## FASE 7: Persiapan Grand Final (Top 5) (11 - 14 November)
*Target: Mengunci kemenangan pada sesi Live Pitching & Tanya Jawab Juri.*

### 11 - 12 November - Monitoring Pengumuman & Penyusunan Pitch Deck
* **Goal:** Menyiapkan slide presentasi 10 lembar yang memikat juri.
* **Aksi:** Susun slide deck: Problem > Solution > High-Level Architecture > Live Demo Scenario > Business Impact/ROI > Future Roadmap.

### 13 November - Rehearsal & Backup Environment
* **Goal:** Penguasaan waktu presentasi dan kesiapan demo darurat.
* **Aksi:**
  1. Latihan pitching tepat waktu (presentasi + Q&A).
  2. Siapkan rekaman demo lokal cadangan jika koneksi internet terganggu saat sesi Zoom berlangsung.

### 14 November - GRAND FINAL & EXHIBITION
* **Goal:** Tampil maksimal di hadapan juri, pertahankan argumen teknis secara lugas, dan bawa pulang gelar juara.
