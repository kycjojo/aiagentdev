# Panduan Teknis & Evaluasi GTNIC 2026

Dokumen ini merangkum seluruh aturan resmi, kriteria penilaian, dan daftar kesalahan fatal yang harus dihindari berdasarkan Technical Meeting resmi GTNIC 2026.

---

## 1. Aturan Dasar Kompetisi
1. **Format Tim:** 1 - 3 orang per tim (lintas institusi diperbolehkan).
2. **Karya:** Maksimal 1 karya per tim. 100% buatan sendiri, orisinal, belum pernah dipublikasikan atau menang lomba lain.
3. **Komposisi Tim:** Roster tim terkunci setelah pendaftaran selesai (tidak dapat diganti).
4. **Keamanan Konten:** Keluaran dilarang memuat unsur SARA, pornografi, kekerasan, atau provokatif.

---

## 2. Ketentuan Teknis AI Agent
* **Teknologi Bebas:** Bebas menggunakan LLM API (OpenAI, Gemini, Anthropic, open-source), framework (LangChain, LlamaIndex, custom), atau low-code platform (n8n, Flowise).
* **Fitur Lanjut Wajib (Minimal 1 fungsi riil):**
  1. Reasoning dan perencanaan langkah otomatis (multi-step planning).
  2. Integrasi API atau tool calling untuk fetch data dan aksi nyata.
  3. RAG untuk mengambil data dari dokumen/basis pengetahuan internal.
* **Larangan Keras:** Dilarang mengumpulkan chatbot yang sekadar membungkus API LLM ("ChatGPT wrapper") tanpa logika kustom, tool, atau kapabilitas penyelesaian masalah nyata.
* **Deployment Publik:** Wajib menyediakan URL live demo publik dan link repositori GitHub publik.

---

## 3. Komponen Penilaian (Bobot Resmi 100%)
* **25%** - Kapabilitas dan Otonomi Agen (menyelesaikan tugas tanpa intervensi manual).
* **15%** - Penalaran, Perencanaan & Pengambilan Keputusan (reasoning loop logis).
* **15%** - Penggunaan Alat & Eksekusi Tindakan (tool calling fungsional).
* **15%** - Arsitektur Teknis & Rekayasa Sistem (guardrails, error handling, clean design).
* **10%** - Inovasi dan Kreativitas solusi.
* **10%** - Dampak Masalah dan Nilai Bisnis (ROI/efisiensi untuk industri).
* **5%** - Pengalaman & Kemudahan Pengguna (UI dashboard interaktif).
* **5%** - Demonstrasi, Presentasi & Dokumentasi (proposal & video).

---

## 4. Checklist Pra-Submit (Slide 15 - Common Mistakes)

### Wajib Diperiksa:
- [ ] Karya sesuai sub-tema Enterprise Productivity & fokus industri nyata.
- [ ] Fitur lanjut (reasoning / tool calling / RAG) terbukti berfungsi saat live demo.
- [ ] Format dokumen proposal PDF (maks. 15 hal) & format video demo (3 - 5 menit) terpenuhi.
- [ ] Tautan live demo web dapat diakses tanpa login terbatas/kendala jaringan.
- [ ] Repositori GitHub sudah diset ke status **PUBLIC** (bukan private).
- [ ] Surat pernyataan keaslian karya dan nama tim sudah dilampirkan.

### Kesalahan Fatal yang Wajib Dihindari:
1. Link live demo tidak dapat dibuka (HTTP 500 / 404 / down).
2. Repo GitHub masih berstatus **PRIVATE** saat juri menilai.
3. Hanya wrapper ChatGPT standar tanpa tool calling / RAG.
4. Proposal tidak menyertakan diagram arsitektur sistem dan metrik kuantitatif.
5. Mengumpulkan formulir melewati batas waktu (10 November 2026, 23.59 WIB).
