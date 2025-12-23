---
description: Setup VS Code Live Share untuk kolaborasi real-time
---

# 🚀 Setup VS Code Live Share - Real-Time Collaboration

## 📌 Apa itu VS Code Live Share?

VS Code Live Share memungkinkan Anda dan tim untuk:
- ✅ Edit kode bersamaan secara real-time (seperti Google Docs/Figma)
- ✅ Melihat kursor dan highlight anggota tim
- ✅ Share terminal dan server (Flask app bisa diakses tim)
- ✅ Voice chat dan text chat built-in
- ✅ Debug bersama
- ✅ **100% GRATIS!**

---

## 🎯 BAGIAN 1: Setup untuk HOST (Anda)

### Langkah 1: Install Extension Live Share

1. Buka **Visual Studio Code**
2. Klik icon **Extensions** di sidebar kiri (atau tekan `Ctrl+Shift+X`)
3. Cari: **"Live Share"**
4. Install extension **"Live Share"** oleh Microsoft
   - Icon: Orang dengan panah
   - Publisher: Microsoft
5. Tunggu sampai instalasi selesai
6. **Reload VS Code** jika diminta

### Langkah 2: Sign In ke Live Share

1. Setelah install, akan muncul tombol **"Live Share"** di status bar (bawah)
2. Klik tombol **"Live Share"**
3. Pilih metode login:
   - **Microsoft Account** (Recommended - pakai akun Outlook/Hotmail)
   - **GitHub Account**
4. Browser akan terbuka untuk login
5. Login dengan akun pilihan Anda
6. Setelah berhasil, browser akan bilang "You're signed in"
7. Kembali ke VS Code

### Langkah 3: Mulai Live Share Session

1. **Buka folder project** Anda di VS Code:
   ```
   File → Open Folder → Pilih "d:\KULIAH\Semester 3\Pemdas\Materi Flask"
   ```

2. Klik tombol **"Live Share"** di status bar (bawah kiri)
   - Atau tekan `Ctrl+Shift+P` → ketik "Live Share: Start Collaboration Session"

3. **Link akan otomatis ter-copy** ke clipboard Anda!
   - Link format: `https://prod.liveshare.vsengsaas.visualstudio.com/join?xxxxx`

4. **Kirim link ini ke anggota tim** via:
   - WhatsApp
   - Email
   - Discord
   - Telegram
   - Atau platform komunikasi lainnya

### Langkah 4: Atur Permission (Opsional tapi Recommended)

Setelah session dimulai, Anda bisa atur permission:

1. Klik **"Live Share"** di sidebar (icon orang)
2. Di panel Live Share, Anda bisa:
   - **Read-only mode**: Tim hanya bisa lihat, tidak bisa edit
     - Klik icon gear → "Make Read-Only"
   - **Read/Write mode** (default): Tim bisa edit kode
   
3. **Accept/Reject participants**:
   - Saat ada yang join, akan muncul notifikasi
   - Klik **"Accept"** untuk izinkan mereka masuk

### Langkah 5: Share Terminal (Untuk Flask App)

Agar tim bisa lihat output Flask app:

1. Buka terminal di VS Code (`Ctrl+` ` atau View → Terminal)
2. Di panel **Live Share** (sidebar), klik **"Share Terminal"**
3. Pilih:
   - **Read-only**: Tim hanya bisa lihat output
   - **Read/Write**: Tim bisa jalankan command juga
4. Klik **"Share"**

Sekarang saat Anda jalankan Flask:
```bash
python app.py
```
Tim bisa lihat output terminal secara real-time!

### Langkah 6: Share Server (Flask App)

Agar tim bisa akses Flask app di browser mereka:

1. Jalankan Flask app Anda:
   ```bash
   python app.py
   ```
   
2. Flask akan jalan di `http://127.0.0.1:5000`

3. Di panel **Live Share**, klik **"Share Server"**
4. Masukkan port: **5000**
5. Klik **"Share"**

Sekarang tim bisa akses Flask app di browser mereka dengan link yang diberikan!

### Langkah 7: Fitur Tambahan

#### Voice/Audio Call
1. Di panel Live Share, klik icon **microphone**
2. Tim yang join bisa ikut voice call
3. Sangat berguna untuk diskusi sambil coding!

#### Focus Follow
- Klik nama participant → **"Follow Participant"**
- Layar Anda akan otomatis ikut ke file/baris yang mereka edit
- Berguna untuk code review atau teaching

---

## 👥 BAGIAN 2: Setup untuk TIM (Collaborators)

### Langkah 1: Install VS Code & Extension

1. **Download dan Install VS Code**:
   - Download dari: https://code.visualstudio.com/
   - Install dengan setting default

2. **Install Extension Live Share**:
   - Buka VS Code
   - Tekan `Ctrl+Shift+X`
   - Cari: **"Live Share"**
   - Install extension **"Live Share"** oleh Microsoft
   - Reload VS Code

### Langkah 2: Sign In

1. Klik tombol **"Live Share"** di status bar
2. Pilih metode login (Microsoft atau GitHub)
3. Login di browser
4. Kembali ke VS Code

### Langkah 3: Join Session

Ada 2 cara join:

#### Cara 1: Via Link (Paling Mudah)
1. **Klik link** yang dikirim host
2. Browser akan tanya "Open Visual Studio Code?"
3. Klik **"Open"** atau **"Yes"**
4. VS Code akan otomatis join session!

#### Cara 2: Manual
1. Tekan `Ctrl+Shift+P`
2. Ketik: **"Live Share: Join Collaboration Session"**
3. Paste link yang dikirim host
4. Tekan Enter

### Langkah 4: Mulai Kolaborasi!

Setelah join, Anda bisa:

✅ **Lihat dan Edit File**:
- Semua file project akan muncul di Explorer
- Edit seperti biasa, perubahan langsung terlihat semua orang

✅ **Lihat Kursor Tim**:
- Setiap orang punya warna kursor berbeda
- Nama mereka muncul di samping kursor

✅ **Akses Terminal** (jika di-share):
- Lihat output Flask app
- Jalankan command (jika diberi permission)

✅ **Akses Flask App** (jika server di-share):
- Klik link di panel Live Share
- Browser akan buka Flask app

✅ **Voice Chat**:
- Klik icon microphone untuk join voice call

---

## 🎨 TIPS & BEST PRACTICES

### Untuk Host:

1. **Komunikasi Jelas**:
   - Gunakan voice chat atau text chat
   - Bilang sebelum edit file penting

2. **Atur Permission**:
   - Read-only untuk presentasi/demo
   - Read/Write untuk kolaborasi aktif

3. **Share Terminal & Server**:
   - Selalu share agar tim bisa test perubahan

4. **Save Secara Berkala**:
   - Tekan `Ctrl+S` untuk save
   - Perubahan langsung sync ke semua orang

### Untuk Collaborators:

1. **Jangan Edit File yang Sama Bersamaan**:
   - Koordinasi siapa edit file apa
   - Atau edit bagian berbeda di file yang sama

2. **Gunakan Follow Mode**:
   - Follow host untuk tutorial/demo
   - Unfollow untuk kerja mandiri

3. **Komunikasi**:
   - Tanya sebelum edit file penting
   - Bilang kalau mau test sesuatu

---

## 🔧 TROUBLESHOOTING

### Problem: Link Tidak Bisa Dibuka
**Solusi**: 
- Pastikan VS Code sudah terinstall
- Coba cara manual (copy-paste link di VS Code)

### Problem: Tidak Bisa Login
**Solusi**:
- Pastikan internet stabil
- Coba metode login lain (GitHub vs Microsoft)
- Restart VS Code

### Problem: Perubahan Tidak Sync
**Solusi**:
- Pastikan file sudah di-save (`Ctrl+S`)
- Check koneksi internet
- Restart Live Share session

### Problem: Flask App Tidak Bisa Diakses Tim
**Solusi**:
- Pastikan server sudah di-share (port 5000)
- Pastikan Flask app sedang running
- Check firewall Windows

---

## 📊 PERBANDINGAN: Live Share vs GitHub

| Fitur | Live Share | GitHub |
|-------|-----------|--------|
| Real-time editing | ✅ Ya | ❌ Tidak |
| Lihat kursor tim | ✅ Ya | ❌ Tidak |
| Voice chat | ✅ Ya | ❌ Tidak |
| Version control | ❌ Tidak | ✅ Ya |
| History perubahan | ❌ Tidak | ✅ Ya |
| Offline access | ❌ Tidak | ✅ Ya |
| **Best for** | Coding bareng real-time | Kolaborasi jangka panjang |

### 💡 Rekomendasi:
**Gunakan KEDUANYA!**
- **Live Share**: Untuk coding session bareng, diskusi, pair programming
- **GitHub**: Untuk save progress, version control, backup

---

## 🎯 WORKFLOW IDEAL

1. **Sebelum Live Share Session**:
   ```bash
   git add .
   git commit -m "Before live session"
   git push
   ```

2. **Selama Live Share Session**:
   - Coding bareng dengan Live Share
   - Test Flask app bersama
   - Diskusi via voice chat

3. **Setelah Live Share Session**:
   ```bash
   git add .
   git commit -m "After live session - added feature X"
   git push
   ```

Dengan cara ini, Anda dapat:
- ✅ Real-time collaboration (Live Share)
- ✅ Version control & backup (GitHub)
- ✅ Best of both worlds!

---

## 📞 QUICK REFERENCE

### Shortcut Penting:

| Action | Shortcut |
|--------|----------|
| Start Live Share | `Ctrl+Shift+P` → "Live Share: Start" |
| Join Session | `Ctrl+Shift+P` → "Live Share: Join" |
| Stop Session | `Ctrl+Shift+P` → "Live Share: End" |
| Follow Participant | Klik nama → "Follow" |
| Open Live Share Panel | Klik icon orang di sidebar |

### Link Berguna:
- Dokumentasi: https://docs.microsoft.com/en-us/visualstudio/liveshare/
- Troubleshooting: https://docs.microsoft.com/en-us/visualstudio/liveshare/troubleshooting

---

## ✅ CHECKLIST

### Untuk Host:
- [ ] Install Live Share extension
- [ ] Sign in dengan Microsoft/GitHub
- [ ] Buka folder project
- [ ] Start Live Share session
- [ ] Copy dan kirim link ke tim
- [ ] Share terminal (optional)
- [ ] Share server port 5000 (untuk Flask)
- [ ] Accept participants yang join

### Untuk Collaborators:
- [ ] Install VS Code
- [ ] Install Live Share extension
- [ ] Sign in dengan Microsoft/GitHub
- [ ] Terima link dari host
- [ ] Join session via link
- [ ] Mulai kolaborasi!

---

**Selamat Berkolaborasi! 🎉**
