# Strategi Pemilihan Use Case & Desain Solusi Agen

Dokumen ini memetakan strategi teknis dan katalog use case enterprise dengan potensi skor tertinggi untuk memenangkan ajang **GTNIC 2026 - Kategori AI Agent Development**.

---

## 1. Kriteria Use Case Pemenang (Winning Formula)

Untuk mendapatkan skor maksimal pada **70% Bobot Teknis Juri**, use case yang dipilih **tidak boleh berupa percakapan santai (chat dialog)**. Use case harus memenuhi kriteria:
1. **Multi-Input Heterogen:** Mampu menerima input dokumen bisnis tidak terstruktur (PDF invoice, receipt, CSV) dan perintah bahasa alami.
2. **Kebutuhan Multi-Step Planning Nyata:** Tugas membutuhkan minimal 3 - 5 tahapan berurutan (tidak bisa diselesaikan dengan 1 kali prompt biasa).
3. **Eksekusi Minimal 3 Tools Fungsional:**
   * Tool 1: Reader / Parser (membaca data/dokumen).
   * Tool 2: Logic / Verifier / Query (validasi aturan atau komparasi database).
   * Tool 3: Action Dispatcher (membuat laporan PDF, update database, kirim webhook/notifikasi).
4. **Adanya RAG Berbasis Regulasi:** Membutuhkan aturan atau SOP perusahaan sebagai acuan validitas tindakan.
5. **Dampak Finansial & Waktu Terukur:** Memiliki metrik ROI konkret yang mudah dipahami juri bisnis.

---

## 2. Katalog 3 Use Case Unggulan

Berikut adalah 3 opsi skenario industri terbaik yang paling cocok dengan rubrik penilaian GTNIC 2026:

---

### OPSI 1: Autonomous Enterprise Finance & Procurement Audit Agent (Sangat Direkomendasikan)
* **Kategori Industri:** FinTech, B2B Enterprise, Retail & Manufaktur.
* **Latar Belakang Masalah:** 
  Perusahaan memproses ratusan invoice vendor setiap bulan. Verifikasi manual antara Purchase Order (PO), Surat Jalan (Goods Receipt), dan Tagihan Invoice memakan waktu 30-45 menit per transaksi. Risiko kecurangan (markup harga, tagihan ganda, vendor fiktif) sangat tinggi.
* **Alur Otonomi Agen:**
  1. *Step 1 (Ingestion):* Agen mengekstrak data dari dokumen invoice tagihan baru (nomor PO, vendor, rincian barang, total biaya).
  2. *Step 2 (Database Query):* Agen memanggil tool database internal untuk mengambil data Purchase Order resmi dan status penerimaan barang di gudang.
  3. *Step 3 (Reconciliation & Cross-Check):* Agen membandingkan kuantitas barang dan nominal harga per item. Jika ada selisih, agen menandai anomali.
  4. *Step 4 (RAG SOP Compliance):* Agen mencocokkan deviasi harga dengan SOP batasan toleransi selisih harga pengadaan perusahaan.
  5. *Step 5 (Action Execution):* 
     * Jika valid: Terbitkan draft approval pembayaran dan kirim notifikasi ke sistem finance.
     * Jika anomali: Kunci pembayaran, terbitkan berkas Berita Acara Selisih (PDF), dan picu alert eskalasi ke tim audit.
* **Nilai Juri:**
  * Otonomi: 100% tanpa campur tangan staf administrasi.
  * Tools: PDF Parser, SQL Query Tool, Reconciliation Engine, PDF Report Generator, Webhook Notifier.
  * Metrik Kuantitatif: Waktu audit berkurang 98%, risiko overpayment berkurang menjadi 0%.

---

### OPSI 2: Autonomous IT Operations & Incident Resolution Agent
* **Kategori Industri:** Cloud Infrastructure, Data Center, Software Enterprise.
* **Latar Belakang Masalah:**
  Saat terjadi alert sistem (service down / spike latency), tim DevOps membutuhkan waktu lama untuk menelusuri log error, mencari panduan penanganan (runbook), dan menjalankan command diagnostik.
* **Alur Otonomi Agen:**
  1. *Step 1 (Alert Ingestion):* Menerima payload alert notifikasi insiden.
  2. *Step 2 (Log Extraction):* Memanggil tool untuk menarik error stack trace dan metrik server terkait.
  3. *Step 3 (RAG Runbook Search):* Mencari prosedur penanganan insiden yang relevan pada knowledge base dokumentasi internal.
  4. *Step 4 (Diagnostic Command Tool):* Menjalankan perintah health check atau uji konektivitas service secara otomatis.
  5. *Step 5 (Remediation & Post-Mortem):* Mengeksekusi restart service yang aman atau auto-scale, serta menyusun draft laporan Post-Mortem insiden dalam format Markdown/PDF.
* **Nilai Juri:** Menunjukkan keunggulan kapabilitas pemanggilan tool level sistem dan adaptabilitas reasoning.

---

### OPSI 3: Enterprise Operations & Smart Order Fulfillment Agent
* **Kategori Industri:** Supply Chain, E-Commerce B2B, Logistik.
* **Latar Belakang Masalah:**
  Pemesanan barang dari klien korporat masuk melalui berbagai format dokumen acak. Staf harus manual mengecek stok di multi-gudang, menentukan armada kurir paling efisien, dan menerbitkan surat jalan.
* **Alur Otonomi Agen:**
  1. *Step 1 (Parsing):* Mengurai purchase request dari dokumen PDF/email klien.
  2. *Step 2 (Inventory Query):* Mengecek ketersediaan stok di seluruh cabang gudang melalui database API.
  3. *Step 3 (Logistics Optimization):* Menghitung rute dan armada logistik terbaik berdasarkan volume muatan dan estimasi waktu kirim.
  4. *Step 4 (Dispatch Action):* Memotong stok di database pusat, menerbitkan Surat Jalan dan Faktur resmi, serta mengirimkan nomor resi ke webhook klien.
* **Nilai Juri:** Visual alur kerja operasional sangat aplikatif dan mudah dipahami oleh juri non-teknis.

---

## 3. Cetak Biru Arsitektur Teknis Agen (ReAct Pattern)

Untuk mengamankan skor tertinggi di babak penyisihan dan final, agen dirancang dengan pola **ReAct (Reasoning + Acting)**:

```text
[ USER TASK / INSTRUCTION ]
           │
           ▼
┌─────────────────────────────────────────────────────────────┐
│                 AGENT CONTROLLER (LLM CORE)                 │
│                                                             │
│   Loop:                                                     │
│   1. THOUGHT    : "Apa tujuan saat ini dan apa yang kurang?"│
│   2. ACTION     : Memilih nama tool dan menyusun payload     │
│   3. DISPATCH   : Menjalankan eksekusi ke Tool Layer         │
│   4. OBSERVATION: Menganalisis respon output dari tool      │
│   5. REFLECT    : "Apakah tugas sudah selesai atau lanjut?"  │
└───────────────────────┬─────────────────────────────────────┘
                        │
       ┌────────────────┼────────────────┐
       ▼                ▼                ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  TOOL 1:     │ │  TOOL 2:     │ │  TOOL 3:     │
│  Data Fetch  │ │  Logic Check │ │  Dispatcher  │
│  & File OCR  │ │  & DB Query  │ │  & Reporter  │
└──────────────┘ └──────────────┘ └──────────────┘
```

### Komponen Guardrails Wajib:
* **Pydantic Validation:** Setiap output tool dan respon akhir agen divalidasi tipe datanya agar tidak menghasilkan format yang rusak.
* **Loop Circuit Breaker:** Batasan maksimal 8 - 10 putaran reasoning agar agen tidak terjebak dalam infinite loop jika menghadapi error eksternal.
* **Deterministic Fallback:** Jika salah satu API tool gagal merespons, agen secara cerdas mengalihkan ke mode offline audit dan menandai status sebagai "Needs Manual Review" daripada menghasilkan jawaban halusinasi.
