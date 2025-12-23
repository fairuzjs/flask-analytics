# 📊 Analisis Diabetes Mellitus di Jawa Barat

Aplikasi web interaktif berbasis Flask untuk menganalisis dan memvisualisasikan data penderita Diabetes Mellitus (DM) di Jawa Barat periode 2017-2024.

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## 📋 Deskripsi Project

Project ini merupakan aplikasi web yang menganalisis data penderita Diabetes Mellitus di 27 kabupaten/kota di Jawa Barat. Aplikasi ini menyajikan visualisasi data interaktif, analisis statistik, dan insight mendalam tentang penyebaran penyakit DM di wilayah Jawa Barat.

### ✨ Fitur Utama

- 📈 **Visualisasi Data Interaktif**: Grafik dan chart yang menampilkan tren penderita DM
- 🗺️ **Analisis per Wilayah**: Data detail untuk 27 kabupaten/kota di Jawa Barat
- 📊 **Kategori Risiko**: Klasifikasi wilayah berdasarkan tingkat risiko (Rendah/Sedang/Tinggi)
- 📉 **Analisis Tren**: Tren perkembangan kasus DM dari tahun 2017-2024
- 🎯 **Top 10 Wilayah**: Identifikasi wilayah dengan kasus tertinggi
- 📱 **Responsive Design**: Tampilan yang optimal di berbagai perangkat

## 🛠️ Teknologi yang Digunakan

- **Backend**: Flask (Python Web Framework)
- **Data Processing**: Pandas, NumPy
- **Data Visualization**: Matplotlib
- **Frontend**: HTML, CSS, JavaScript
- **Data Format**: JSON, CSV

## 📁 Struktur Project

```
Materi Flask/
├── app.py                          # Aplikasi Flask utama
├── Soal_Pemdas_Kelompok.ipynb     # Jupyter Notebook untuk analisis data
├── data/
│   ├── eksplorasi_lengkap.json    # Data hasil eksplorasi lengkap (Soal 1-19)
│   ├── data_detail_wilayah.json   # Data detail per wilayah
│   └── ringkasan_analisis.json    # Ringkasan hasil analisis
├── templates/
│   └── index.html                 # Template HTML utama
├── static/
│   └── images/                    # Folder untuk visualisasi grafik
├── dinkes-od_17448_jml_penderita_diabetes_melitus_brdsrkn_kabupatenko_v2_data.csv
└── venv/                          # Virtual environment
```

## 🚀 Cara Menjalankan Project

### Prerequisites

- Python 3.7 atau lebih tinggi
- pip (Python package manager)

### Instalasi

1. **Clone repository** (atau download project)
   ```bash
   git clone <repository-url>
   cd "Materi Flask"
   ```

2. **Buat virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Aktifkan virtual environment**
   
   Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install flask pandas numpy matplotlib
   ```

5. **Jalankan aplikasi**
   ```bash
   python app.py
   ```

6. **Buka browser** dan akses:
   ```
   http://localhost:5000
   ```

## 📊 Data Source

Data yang digunakan berasal dari:
- **Sumber**: Dinas Kesehatan Provinsi Jawa Barat (Open Data)
- **Dataset**: Jumlah Penderita Diabetes Melitus Berdasarkan Kabupaten/Kota
- **Periode**: 2017 - 2024
- **Cakupan**: 27 Kabupaten/Kota di Jawa Barat

## 📈 Analisis yang Tersedia

### 1. Eksplorasi Data (Soal 1-19)
Analisis mendalam mencakup:
- Statistik deskriptif
- Analisis per tahun
- Analisis per wilayah
- Identifikasi outlier
- Korelasi antar variabel

### 2. Visualisasi Data (Soal 20-24)
- **Top 10 Kabupaten/Kota** dengan penderita DM terbanyak
- **Tren Top 5 Wilayah** periode 2017-2021
- **Tren Provinsi** Jawa Barat secara keseluruhan
- **Distribusi Kategori Risiko** (Pie Chart)
- **Jumlah Wilayah per Kategori** (Bar Chart)

### 3. Kategori Risiko

Wilayah dikategorikan berdasarkan jumlah kumulatif penderita DM:
- 🟢 **Rendah**: < 10,000 kasus
- 🟡 **Sedang**: 10,000 - 25,000 kasus
- 🔴 **Tinggi**: > 25,000 kasus

## 🔍 Temuan Utama

### 1. Wilayah dengan Kasus Tertinggi
**Kabupaten Bogor** memiliki jumlah penderita DM tertinggi (>25.000 kasus) dan konsisten menempati posisi teratas di semua tahun pengamatan (2017-2021).

### 2. Tren Perkembangan
Jumlah penderita DM di Jawa Barat **cenderung NAIK** secara konsisten dari tahun ke tahun, meningkat dari ~120.000 kasus (2017) menjadi ~165.000 kasus (2021) - peningkatan **37.5%** dalam 5 tahun.

### 3. Distribusi Kategori
- 52% wilayah (14 kab/kota): Kategori **Rendah**
- 33% wilayah (9 kab/kota): Kategori **Sedang**
- 15% wilayah (4 kab/kota): Kategori **Tinggi**


## 🤝 Kontribusi

Jika Anda ingin berkontribusi pada project ini:
1. Fork repository
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📞 Kontak

Untuk pertanyaan atau saran, silakan hubungi tim pengembang melalui GitHub Issues.

---

**Dibuat dengan ❤️ untuk Tugas Pemrograman Dasar**
