# AI Agent Development - GTNIC 2026

Repositori pengembangan AI Agent untuk **Garda Tech National Innovation Competition (GTNIC) 2026**.
* **Kategori:** AI Agent Development
* **Sub-tema:** Enterprise Productivity (Fokus: Enterprise & Industry)
* **Periode Pengerjaan:** 19 Oktober - 10 November 2026 (Deadline: 23.59 WIB)
* **Grand Final:** 14 November 2026 (Top 5 Finalists)

---

## 1. Ringkasan & Sasaran Utama

Membangun AI Agent otonom untuk otomasi alur kerja operasional enterprise nyata.
Bukan sekadar "LLM Wrapper", melainkan sistem yang memiliki:
1. **Multi-Step Reasoning & Planning:** Mampu memecah instruksi bisnis kompleks menjadi tahapan eksekusi logis.
2. **Tool Calling & Real Action Execution:** Integrasi API, query basis data, parsing dokumen, dan dispatching aksi ke sistem eksternal.
3. **Knowledge Retrieval (RAG):** Mengambil dan menyelaraskan keputusan dengan regulasi, SOP, atau dokumen internal perusahaan.
4. **Safety & Guardrails:** Validasi skema output terstruktur dan pemulihan otomatis jika tool call gagal.

---

## 2. Bobot Penilaian (Judging Criteria)

Total penilaian berbobot 100%, dengan **70% fokus pada kapabilitas teknis inti**:

| Kriteria | Bobot | Deskripsi |
| :--- | :---: | :--- |
| **Kapabilitas & Otonomi Agen** | **25%** | Kemandirian agen menyelesaikan tugas dari awal sampai selesai tanpa campur tangan manual |
| **Penalaran, Perencanaan & Keputusan** | **15%** | Kualitas alur reasoning, logika pemilihan langkah, dan adaptabilitas keputusan |
| **Penggunaan Alat & Eksekusi Tindakan** | **15%** | Kemampuan memanggil tools, query data riil, dan mutasi aksi yang aman |
| **Arsitektur Teknis & Rekayasa Sistem** | **15%** | Kebersihan kode, modularitas, penanganan guardrails, error recovery |
| **Inovasi & Kreativitas** | **10%** | Keunikan pendekatan solusi dibanding automasi konvensional |
| **Dampak Masalah & Nilai Bisnis** | **10%** | Penghematan waktu/biaya nyata bagi operasional industri target |
| **Pengalaman & Kemudahan Pengguna** | **5%** | Kemudahan antarmuka dashboard dan kejelasan status eksekusi agen |
| **Demonstrasi, Presentasi & Dokumentasi** | **5%** | Kualitas proposal PDF dan video walkthrough live demo |

---

## 3. Berkas Wajib Pengumpulan (Google Form Submission)

Deadline: **10 November 2026, 23.59 WIB**
1. **Live Interface Web:** Tautan aplikasi agen yang dapat diakses publik.
2. **Repositori GitHub Publik:** Repositori kode sumber dengan dokumentasi lengkap.
3. **Proposal PDF (Maks. 15 Halaman):** 
   * Format: A4, Times New Roman 12, Spasi 1.5, Margin Kiri 4 cm, Lainnya 3 cm.
   * Nama file: `GTNIC2026_AIAgent_NamaTim.pdf`
   * Cover wajib mencantumkan logo resmi GTNIC 2026.
4. **Video Demo (3 - 5 Menit):** Walkthrough dan demo interaktif live via YouTube / Google Drive publik.
5. **Surat Pernyataan Keaslian Karya:** Bertanda tangan materai/resmi menyatakan 100% orisinal.

---

## 4. Struktur Proyek

```text
aiagentdev/
├── README.md
├── requirements.txt
├── .gitignore
├── docs/
│   ├── TIMELINE.md              # Rencana aksi per hari (19 Okt - 14 Nov)
│   ├── COMPETITION_RULES.md     # Panduan teknis & checklist mitigasi kesalahan
│   └── PROPOSAL_SPEC.md         # Rincian 8 komponen isi proposal resmi
├── src/
│   ├── agent/                   # Core agent loop, planner, state machine
│   │   ├── __init__.py
│   │   ├── core.py
│   │   └── planner.py
│   ├── tools/                   # Integrasi tool eksekusi (DB, API, Document Parser)
│   │   ├── __init__.py
│   │   └── base.py
│   └── api/                     # Backend API & WebSocket/SSE streaming
│       ├── __init__.py
│       └── server.py
└── data/                        # Sample dataset mock enterprise & test cases
```

---

## 5. Timeline Ringkas

* **19 - 22 Okt:** Problem Definition, Tech Stack, & Scaffolding Arsitektur
* **23 - 28 Okt:** Core Engine, Tool Calling, RAG, & Guardrails
* **29 Okt - 02 Nov:** Web Dashboard Interface & Public Deployment
* **03 - 06 Nov:** Penulisan Proposal PDF (15 Hal) & Pengujian Metrik
* **07 - 08 Nov:** Produksi Video Walkthrough Demo (3 - 5 Menit)
* **09 Nov:** Final Checklist, Verifikasi Publik, & Submit Google Form
* **10 Nov:** Buffer Day (Monitoring Sistem & Uptime Demo)
* **14 Nov:** Grand Final & Live Pitching via Zoom
