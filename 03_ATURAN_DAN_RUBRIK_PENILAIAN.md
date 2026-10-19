# Aturan Resmi & Rubrik Penilaian GTNIC 2026

Panduan ini membedah aturan kompetisi, kriteria penilaian dewan juri, serta daftar larangan fatal pada ajang **Garda Tech National Innovation Competition (GTNIC) 2026 - Kategori AI Agent Development**.

---

## 1. Aturan Dasar & Ketentuan Peserta
1. **Jumlah Anggota Tim:** 1 hingga 3 orang per tim (individu diperbolehkan).
2. **Afiliasi:** Peserta diperbolehkan berasal dari lintas institusi / universitas / umum.
3. **Batas Karya:** Setiap tim hanya berhak mengirimkan **1 karya AI Agent**.
4. **Keaslian Karya:** Karya wajib 100% orisinal, buatan sendiri, belum pernah dipublikasikan secara komersial, dan belum pernah memenangkan perlombaan lain.
5. **Integritas Roster:** Komposisi nama anggota tim terkunci setelah submit pendaftaran awal dan tidak dapat diganti.
6. **Norma Konten:** Output agen dilarang keras mengandung unsur SARA, ujaran kebencian, pornografi, kekerasan, atau provokasi.

---

## 2. Larangan Keras: Diskualifikasi Chatbot Wrapper

Panitia dan juri GTNIC 2026 secara eksplisit menegaskan larangan:
> **"DILARANG: CHATBOT YANG HANYA MEMBUNGKUS API LLM"**

### Definisi Proyek yang Terancam Gugur:
* Aplikasi yang hanya memiliki form input teks, meneruskan string prompt ke API OpenAI/Gemini/Anthropic, lalu menampilkan respons teks kembali ke layar.
* Sistem tanpa logika pemecahan tugas (no planning / no reasoning step).
* Sistem tanpa pemanggilan tools eksternal (no tool calling / no API execution / no DB mutation).
* Sistem tanpa validasi fakta berbasis dokumen (no RAG / no grounding).

### Syarat Lolos Standar Teknis AI Agent:
Karya harus memiliki minimal **salah satu (atau kombinasi)** dari fitur tingkat lanjut berikut yang terbukti berfungsi secara nyata saat demo:
1. **Multi-Step Reasoning & Planning:** Kemampuan agen menganalisis instruksi kompleks, menyusun rencana kerja multi-tahap, dan mengevaluasi status penyelesaian setiap tahap secara otonom.
2. **Tool Calling & Action Execution:** Kemampuan agen memanggil fungsi/API eksternal untuk mengambil data real-time, mengurai file bisnis, atau mengeksekusi mutasi status (mengirim laporan, update database, memicu webhook).
3. **Retrieval-Augmented Generation (RAG):** Kemampuan agen mengambil data dari basis pengetahuan atau dokumen operasional enterprise untuk dijadikan landasan keputusan logis.

---

## 3. Rubrik Penilaian Resmi (Total Bobot 100%)

Dewan juri menaruh **70% bobot nilai pada kecakapan teknis agen**:

```text
+-------------------------------------------------------------------------------+
|                      BOBOT PENILAIAN JURI GTNIC 2026                          |
+-------------------------------------------------------------------------------+
| [70%] KAPABILITAS TEKNIS AGEN INTI:                                           |
|   1. Kapabilitas dan Otonomi Agen                 : 25%                       |
|   2. Penalaran, Perencanaan & Keputusan           : 15%                       |
|   3. Penggunaan Alat & Eksekusi Tindakan          : 15%                       |
|   4. Arsitektur Teknis & Rekayasa Sistem          : 15%                       |
+-------------------------------------------------------------------------------+
| [30%] ASPEK PENDUKUNG & PRESENTASI:                                           |
|   5. Inovasi dan Kreativitas                      : 10%                       |
|   6. Dampak Masalah dan Nilai Bisnis              : 10%                       |
|   7. Pengalaman & Kemudahan Pengguna (UI/UX)      :  5%                       |
|   8. Demonstrasi, Presentasi & Dokumentasi        :  5%                       |
+-------------------------------------------------------------------------------+
```

### Bedah Komponen Teknis (70%):
1. **Kapabilitas dan Otonomi Agen (25%):**
   * Seberapa jauh agen dapat bekerja sendiri dari trigger awal hingga output akhir tanpa campur tangan user?
   * Apakah agen dapat menyelesaikan pekerjaan operasional yang bernilai nyata bagi industri?
2. **Penalaran, Perencanaan & Keputusan (15%):**
   * Apakah langkah-langkah kerja agen terstruktur logis?
   * Apakah agen mampu beradaptasi saat terjadi perubahan status atau hasil data tidak terduga?
3. **Penggunaan Alat & Eksekusi Tindakan (15%):**
   * Seberapa presisi agen dalam memilih tool yang tepat pada saat yang tepat?
   * Apakah pemanggilan tool menghasilkan efek nyata (fetch data, manipulasi file, eksekusi API)?
4. **Arsitektur Teknis & Rekayasa Sistem (15%):**
   * Kerapian struktur kode dan modularitas antarmuka tool.
   * Keberadaan guardrails teknis: validasi skema output (Pydantic), pencegahan kebocoran data sensitif, dan error recovery jika tool call gagal.

---

## 4. Checklist Pra-Submit & Mitigasi Kesalahan Fatal (Slide 15)

Sebelum menekan tombol Submit pada Google Form resmi, pastikan checklist berikut terpenuhi:

### Checklist Wajib (Check Before Submit):
- [ ] Sub-tema karya sesuai dengan *Enterprise Productivity* dan fokus pada sektor industri/perusahaan nyata.
- [ ] Fitur lanjut agen (reasoning / tool calling / RAG) dapat didemonstrasikan secara langsung tanpa bug.
- [ ] Proposal berformat PDF dengan batas maksimal 15 halaman dan mengikuti aturan margin/font resmi.
- [ ] Video demo berdurasi antara 3 sampai 5 menit dengan audio jelas dan alur terstruktur.
- [ ] Tautan live demo web dapat dibuka secara instan oleh publik tanpa login berbayar/kendala jaringan.
- [ ] Repositori GitHub proyek diset ke status **PUBLIC** (bukan private).
- [ ] Surat pernyataan keaslian karya bermaterai/bertanda tangan resmi telah dilampirkan.

### 5 Kesalahan Fatal Penyebab Gugur / Nilai Anjlok:
1. **Link Live Demo Tidak Dapat Diakses:** Server down, terkena CORS error, atau membutuhkan kredensial khusus yang tidak diberikan kepada juri.
2. **Repo GitHub Masih Private:** Juri tidak dapat memeriksa arsitektur kode sumber saat sesi evaluasi.
3. **Hanya ChatGPT Wrapper:** Tidak ada integrasi tool calling, query database, atau RAG yang bekerja nyata.
4. **Proposal Tanpa Arsitektur & Metrik:** Dokumen hanya berisi narasi tanpa diagram alur teknis dan tanpa tabel perbandingan efisiensi terukur.
5. **Pengumpulan Melewati Batas Waktu:** Submit setelah 10 November 2026 pukul 23.59 WIB otomatis ditolak oleh sistem panitia.
