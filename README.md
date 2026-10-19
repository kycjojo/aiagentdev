# AI Agent Development - GTNIC 2026

Repositori resmi pengembangan proyek AI Agent untuk **Garda Tech National Innovation Competition (GTNIC) 2026**.

* **Kategori:** AI Agent Development
* **Sub-tema:** Enterprise Productivity (Fokus: Enterprise & Industry)
* **Penyelenggara:** Garda Tech
* **Periode Pengerjaan:** 19 Oktober - 10 November 2026 (Deadline Submit: 23.59 WIB)
* **Pengumuman Top 5:** 12 November 2026
* **Grand Final & Exhibition:** 14 November 2026 (Live Pitching via Zoom)

---

## 1. Indeks Dokumen & Acuan Lomba

Seluruh hasil analisis video Technical Meeting, aturan penilaian, panduan proposal, dan action plan harian telah didokumentasikan secara terstruktur di folder `docs/`:

1. [**`docs/TIMELINE.md`**](docs/TIMELINE.md)
   * Master action plan harian per tanggal (19 Oktober - 14 November 2026).
   * Memuat **Goals**, **Aksi Eksekusi**, dan **Output Verifikasi** harian untuk 7 Fase kerja.
2. [**`docs/TECHNICAL_MEETING_EXTRACTION.md`**](docs/TECHNICAL_MEETING_EXTRACTION.md)
   * Ekstraksi lengkap video Technical Meeting 24m38s (`AI AGENT .mp4`).
   * Rincian slide-by-slide (Slide 01 - 16), timestamp, contoh kasus industri, dan poin sesi Q&A.
3. [**`docs/COMPETITION_RULES.md`**](docs/COMPETITION_RULES.md)
   * Ketentuan dasar lomba, batasan tim, larangan keras (anti-chatbot wrapper).
   * Rubrik penilaian resmi 100% dan checklist mitigasi 5 kesalahan fatal (Slide 15).
4. [**`docs/PROPOSAL_SPEC.md`**](docs/PROPOSAL_SPEC.md)
   * Aturan format fisik dokumen proposal PDF (A4, TNR 12 pt, spasi 1.5, margin 4-3-3-3, maks. 15 hal).
   * Rincian struktur 8 komponen wajib isi proposal.

---

## 2. Sasaran Teknis Utama (Mengamankan 70% Bobot Juri)

Juri mengalokasikan **70% nilai pada kapabilitas teknis inti agen**. Proyek ini dirancang agar memenuhi 4 pilar teknis tersebut:

| Kriteria Penilaian | Bobot | Target Implementasi Teknis |
| :--- | :---: | :--- |
| **Kapabilitas & Otonomi Agen** | **25%** | Agen menyelesaikan siklus tugas operasional dari awal sampai akhir tanpa intervensi manual user |
| **Penalaran, Perencanaan & Keputusan** | **15%** | Loop ReAct / Plan-and-Execute yang memecah problem bisnis kompleks menjadi langkah terstruktur |
| **Penggunaan Alat & Eksekusi Tindakan** | **15%** | Tool calling nyata untuk query database, parsing dokumen bisnis, dan dispatching aksi ke sistem eksternal |
| **Arsitektur Teknis & Rekayasa Sistem** | **15%** | Guardrails validasi schema (Pydantic), proteksi halusinasi, dan pemulihan otomatis jika tool gagal (fallback) |
| **Inovasi & Kreativitas** | **10%** | Solusi agen cerdas adaptif dibanding otomasi rule-based konvensional |
| **Dampak Masalah & Nilai Bisnis** | **10%** | Metrik kuantitatif penghematan waktu kerja operasional dan penurunan tingkat kesalahan manusia |
| **Pengalaman & Kemudahan Pengguna** | **5%** | Dashboard web modern yang menampilkan alur pemikiran agen (thought stream) secara live |
| **Demonstrasi, Presentasi & Dokumen** | **5%** | Kerapian proposal 15 halaman dan kejelasan video walkthrough demo 3 - 5 menit |

---

## 3. Berkas Wajib Pengumpulan (Deadline: 10 Nov 2026, 23.59 WIB)

1. **Link Live Interface Web:** Aplikasi web AI Agent yang dapat diakses publik.
2. **Link Repositori GitHub Publik:** Repositori kode sumber dengan dokumentasi lengkap.
3. **Proposal PDF (Maks. 15 Halaman):** Format nama file `GTNIC2026_AIAgent_NamaTim.pdf` dengan logo GTNIC 2026 di cover.
4. **Link Video Demo (3 - 5 Menit):** Walkthrough dan live demo di YouTube / Google Drive publik.
5. **Surat Pernyataan Keaslian Karya:** Berkas resmi bertanda tangan menyatakan orisinalitas 100%.

---

## 4. Struktur Proyek

```text
aiagentdev/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── docs/
│   ├── TIMELINE.md                     # Master timeline harian & daily goals (19 Okt - 14 Nov)
│   ├── TECHNICAL_MEETING_EXTRACTION.md # Ekstraksi lengkap rekaman video TM GTNIC 2026 (Slide 1-16)
│   ├── COMPETITION_RULES.md            # Ketentuan teknis, rubrik penilaian, & common mistakes
│   └── PROPOSAL_SPEC.md                # Standar 8 komponen wajib proposal 15 halaman
├── src/
│   ├── agent/                          # Core autonomous agent & ReAct planner loop
│   │   ├── __init__.py
│   │   ├── core.py
│   │   └── planner.py
│   ├── tools/                          # Interface eksekusi tool nyata (DB, parser, API)
│   │   ├── __init__.py
│   │   └── base.py
│   └── api/                            # FastAPI server backend & streaming endpoint
│       ├── __init__.py
│       └── server.py
└── data/                               # Sample mock dataset operasional enterprise
    └── .gitkeep
```

---

## 5. Ringkasan Jadwal Pengerjaan

* **Fase 1 (19 - 22 Okt):** Problem Definition, Scaffolding, Data Mock & Tracer Test
* **Fase 2 (23 - 28 Okt):** Core Engine, 3 Functional Tools, ReAct Loop, RAG, & Guardrails
* **Fase 3 (29 Okt - 02 Nov):** Web Dashboard Interface, Thought Streaming, & Public Deployment
* **Fase 4 (03 - 06 Nov):** Penulisan Proposal Resmi 15 Halaman & Ekspor PDF
* **Fase 5 (07 - 08 Nov):** Rekam Skrip, Editing, & Upload Video Demo 3 - 5 Menit
* **Fase 6 (09 - 10 Nov):** Verifikasi Seluruh Link Publik & Early Submission Google Form
* **Fase 7 (11 - 14 Nov):** Grand Final Pitching Preparation & Exhibition
