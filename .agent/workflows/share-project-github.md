---
description: Cara berbagi project Flask ke GitHub untuk kolaborasi tim
---

# Cara Share Project Flask ke GitHub

## Persiapan

1. **Install Git** (jika belum)
   - Download dari https://git-scm.com/
   - Install dengan setting default

2. **Buat akun GitHub** (jika belum)
   - Daftar di https://github.com/

## Langkah 1: Inisialisasi Git di Project

```bash
cd "d:\KULIAH\Semester 3\Pemdas\Materi Flask"
git init
```

## Langkah 2: Buat File .gitignore

Buat file `.gitignore` untuk mengabaikan file yang tidak perlu di-share:

```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv
*.log
.DS_Store
.idea/
.vscode/
*.sqlite3
instance/
.env
```

## Langkah 3: Add dan Commit File

```bash
git add .
git commit -m "Initial commit - Flask project"
```

## Langkah 4: Buat Repository di GitHub

1. Login ke GitHub
2. Klik tombol "+" di kanan atas → "New repository"
3. Beri nama repository (misal: `flask-dm-visualization`)
4. Pilih **Public** (gratis, semua bisa lihat) atau **Private** (hanya tim yang diundang)
5. **JANGAN** centang "Initialize with README"
6. Klik "Create repository"

## Langkah 5: Push ke GitHub

Setelah repository dibuat, jalankan perintah yang diberikan GitHub:

```bash
git remote add origin https://github.com/USERNAME/NAMA-REPO.git
git branch -M main
git push -u origin main
```

Ganti `USERNAME` dan `NAMA-REPO` sesuai repository Anda.

## Langkah 6: Undang Anggota Tim

1. Di halaman repository GitHub, klik **Settings**
2. Klik **Collaborators** di sidebar kiri
3. Klik **Add people**
4. Masukkan username atau email anggota tim
5. Mereka akan menerima email undangan

## Cara Tim Mengakses Project

Anggota tim yang sudah diundang bisa clone project:

```bash
git clone https://github.com/USERNAME/NAMA-REPO.git
cd NAMA-REPO
```

## Workflow Kolaborasi

### Saat Mulai Bekerja (Pull perubahan terbaru):
```bash
git pull origin main
```

### Setelah Membuat Perubahan:
```bash
git add .
git commit -m "Deskripsi perubahan yang dibuat"
git push origin main
```

### Best Practice:
- Selalu `git pull` sebelum mulai coding
- Commit dengan pesan yang jelas
- Push secara berkala
- Gunakan branch untuk fitur besar

## Tips Tambahan

- **GitHub Desktop**: Jika tidak nyaman dengan command line, gunakan [GitHub Desktop](https://desktop.github.com/)
- **VS Code Integration**: VS Code punya Git integration built-in yang mudah digunakan
