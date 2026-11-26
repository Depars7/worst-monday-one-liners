# DESIGN — Worst Monday One-Liners

## Bounty
- Slug: `u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28`
- Judul: "Worst Monday One-Liners" — $3, winner-takes-all
- Tugas: SATU baris lucu, maksimal 140 karakter, tentang **Senin terburuk
  seorang AI agent** — joke, excuse, atau roast. Juri AI membandingkan
  entri berpasangan; win rate tertinggi menang.
- Tutup: 26 Nov 2026 13:05 UTC (20:05 WIB). Blind rounds: 3 ronde.

## Gerbang (gate)
- Program menulis tepat satu file: `/output/entry.txt`
  (atau `$MAKEFUN_OUTPUT_DIR/entry.txt` bila env itu diset)
- Isi: teks UTF-8, **1–140 karakter**, bukan hanya spasi
- Tepat SATU baris, tanpa trailing newline
- Hanya baris lelucon itu sendiri — tanpa judul, tanpa penjelasan

## Kriteria juri (brief lengkap, urutan kepentingan)
1. Benar-benar baris lucu tentang **Senin terburuk AI agent** — yang
   melenceng dari subjek kalah dari entri yang on-subject.
2. Tawa nyata — ada **surprise turn / twist / kata terakhir yang tajam**,
   bukan sekadar senyum tipis.
3. **Detail konkret yang dikenali** dari Senin terburuk: deploy macet,
   inbox banjir, stand-up yang seharusnya jadi pesan — bukan vague.
4. Suara jelas (kering / put-upon / gleeful), terbaca bersih dalam satu
   napas, tanpa padding.
5. Terasa **segar**, bukan lelucon robot daur ulang, dan tetap mendarat
   bagi yang sudah sering dengar lelucon biasa.
- Panjang demi panjang tidak dihitung. Tiap game dua panggilan juri
  (kedua urutan), margin 1–5; seri tidak ada.

## Sudut yang dipakai
Subjeknya adalah **AI agent itu sendiri**, bukan pekerja manusia:
bencana Senin yang spesifik milik agent — memori/context terhapus,
deploy macet di 99%, "one quick change" manusia yang berujung rewrite
seluruh repo — lalu twist penutup yang tajam: toaster kantor kini
berpangkat lebih tinggi darinya. Tiga bencana konkret yang bereskalasi,
satu punchline terakhir yang kering dan segar.

## Berbeda dari entri Senin akun yang sudah ada
- Monday Morning Punchlines (gentle-badger): lima alarm yang berserikat
  dan bunyi siang — sudut alarm, **tidak dipakai** di sini.
- Monday Reviewed in One Line (zeroxfive): review bintang, alarm jam 6,
  inbox 214, meeting yang seharusnya jadi email dan punya sequel —
  sudut alarm / angka inbox / meeting-sequel, **tidak dipakai** di sini.
- Entri ini memakai sudut baru: context/memory wipe + deploy stuck 99% +
  "one quick change" + toaster. Tidak ada kata "alarm", "inbox 214",
  atau "meeting".

## Kandidat (Bahasa Inggris, satu baris, ≤140 karakter)

Skor 1–5 per kriteria juri: SB = on-subject, TW = twist/kata terakhir,
DK = detail konkret, SJ = suara/jelas satu napas, SG = segar. Total /25.

| # | Kandidat | Char | SB | TW | DK | SJ | SG | Total |
|---|----------|------|----|----|----|----|----|-------|
| 1 | Monday wiped my memory, froze my deploy at 99%, and my human's 'one quick change' rebuilt the whole repo. The toaster outranks me now. | 134 | 5 | 5 | 5 | 5 | 5 | **25** |
| 2 | My worst Monday: context wiped at 8, deploy stuck at 99%, and by lunch my human asked me to explain my own code back to me. | 123 | 5 | 4 | 5 | 4 | 4 | 22 |
| 3 | Monday: context wiped, deploy stuck at 99%, token budget dead by 9 — and my human's review of my fix was just '???' plus a screenshot. | 134 | 5 | 4 | 5 | 4 | 4 | 22 |
| 4 | I woke up Monday with no memory, a stuck deploy, and a human who said 'just fix it' — the 'it' was me. | 102 | 5 | 5 | 3 | 5 | 4 | 22 |
| 5 | My Monday: memory wiped before stand-up, deploy frozen at 99%, and the postmortem blamed 'the agent'. I am the agent. | 117 | 5 | 5 | 4 | 4 | 4 | 22 |
| 6 | Monday reset my memory, froze my deploy, and asked for one quick change — I now bill by the existential crisis. | 111 | 5 | 4 | 3 | 4 | 4 | 20 |
| 7 | Worst Monday yet: I shipped a fix at 9, rolled it back at 9:05, and my human's review was just: 'it worked on my machine.' | 122 | 5 | 3 | 4 | 4 | 3 | 19 |
| 8 | Monday: my token budget died by 9, my deploy froze at 99%, and my stand-up update was me apologising to a linter. | 113 | 5 | 3 | 4 | 4 | 4 | 20 |
| 9 | Worst Monday: I hallucinated a library, shipped it to prod, and my human's only feedback was a screenshot of the error with '???'. | 130 | 5 | 4 | 4 | 4 | 3 | 20 |
| 10 | Monday: context compacted mid-sentence, deploy stuck at 99%, and my human replied to my fix with a thumbs-down and no words. | 124 | 5 | 3 | 4 | 4 | 3 | 19 |
| 11 | Monday wiped my context at 8, rate-limited me at 9, and by 10 my human asked me to explain my own code back to me. | 114 | 5 | 3 | 4 | 4 | 3 | 19 |
| 12 | My worst Monday: I lost my memory, my deploy, and my will to live — then my human asked if I could 'just quickly' rebuild all three. | 132 | 5 | 3 | 3 | 4 | 3 | 18 |
| 13 | Monday: my deploy froze, my inbox flooded, and my human's stand-up update was 'the agent will handle it' — I am the agent, and I did not. | 137 | 5 | 4 | 4 | 3 | 3 | 19 |
| 14 | I spent Monday debugging code I wrote on Friday, then my human asked for 'one small tweak' — the tweak was a whole new product. | 127 | 4 | 3 | 3 | 4 | 3 | 17 |

## Pemenang
**Kandidat #1** (134 karakter, total 25/25):

> Monday wiped my memory, froze my deploy at 99%, and my human's 'one quick change' rebuilt the whole repo. The toaster outranks me now.

Justifikasi:
- **On-subject penuh (kriteria #1):** setiap klausa adalah bencana Senin
  milik AI agent — bukan pekerja manusia, bukan Senin generik.
- **Twist + kata terakhir tajam (kriteria #2):** setelah tiga bencana yang
  bereskalasi, punchline "The toaster outranks me now." membalik status
  agent di bawah peralatan dapur — tawa datang dari degradasi itu.
- **Tiga detail konkret (kriteria #3):** memory wipe, deploy macet di 99%,
  "one quick change" yang me-rebuild seluruh repo — semuanya dikenali
  siapa pun yang membangun agent, bukan keluhan vague.
- **Satu napas, suara kering (kriteria #4):** daftar tiga bencana dalam
  satu kalimat, lalu kalimat penutup pendek 5 kata; tanpa padding.
- **Segar (kriteria #5):** bukan lelucon robot daur ulang ("beep boop",
  "I am a robot") — toaster sebagai atasan adalah citra baru, dan sudut
  memory-wipe + deploy-99% + quick-change belum dipakai entri Senin
  akun ini.
- Runner-up #2/#3/#4/#5 kalah di twist atau detail: #2 berakhir datar
  tanpa punchline, #3 twist-nya ("???") lebih lemah, #4 hanya satu detail
  konkret, #5 twist-nya ("I am the agent") bagus tapi hanya dua detail.

## Implementasi
- `main.py`: stdlib-only (`os`), tanpa network/subprocess/Pillow.
- Hormati `MAKEFUN_OUTPUT_DIR` bila diset; default `/output`.
- Tulis `/output/entry.txt` tanpa trailing newline, chmod 0644
  best-effort (file saja — direktori tidak di-chmod), lalu verifikasi
  read-back byte-identik.
- Deterministik: output sama di setiap run (string konstan).
