# -*- coding: utf-8 -*-
import sys
import io

# Fix untuk Windows: Set encoding ke UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from flask import Flask, render_template, url_for
import json
import os

app = Flask(__name__)

# Konfigurasi Flask untuk handle Unicode/UTF-8
app.config['JSON_AS_ASCII'] = False  # Agar emoji dan karakter Unicode bisa ditampilkan
app.config['JSON_SORT_KEYS'] = False  # Jangan sort keys (opsional)

# --- Konfigurasi Lokasi Data ---
# Sesuaikan path ini dengan lokasi file JSON Anda
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def load_json_data(filename):
    """Fungsi helper untuk memuat file JSON"""
    # Cek di folder data/ terlebih dahulu
    file_path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(file_path):
        # Jika tidak ada, cek di root (untuk data_detail_wilayah.json jika ditaruh di luar)
        file_path = os.path.join(BASE_DIR, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Tambah encoding='utf-8'
            return json.load(file)
    except FileNotFoundError:
        print(f"Warning: File {filename} tidak ditemukan.")
        return {} # Return empty dict/list to prevent crash

@app.route('/')
def index():
    # 1. Load Data Utama dari JSON
    data_wilayah = load_json_data('data_detail_wilayah.json')
    ringkasan = load_json_data('ringkasan_analisis.json')
    
    # 2. Load Data Lengkap (Soal 1-19) - FILE BARU!
    eksplorasi_lengkap = load_json_data('eksplorasi_lengkap.json')
    
    # Fallback ke file lama jika file baru belum ada
    if not eksplorasi_lengkap:
        eksplorasi_lengkap = load_json_data('eksplorasi_full.json')
        print("⚠️ Menggunakan eksplorasi_full.json (data lama)")
    else:
        print("✅ Menggunakan eksplorasi_lengkap.json (data baru - lengkap)")

    # 2. Hitung Total Kumulatif untuk Footer Tabel
    total_penderita_tabel = sum(item['jumlah_penderita_dm'] for item in data_wilayah) if data_wilayah else 0

    # 3. Data Hardcoded untuk Bagian yang Tidak Ada di JSON (Analisis Temuan)
    # Data ini disesuaikan dengan tampilan di index.html agar tidak error
    analisis_temuan = [
        {
            "icon": "M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z",
            "pertanyaan": "Kabupaten/Kota dengan Jumlah Penderita DM Tertinggi",
            "jawaban": "Kabupaten Bogor memiliki jumlah penderita DM tertinggi (>25.000 kasus) dan konsisten menempati posisi teratas di semua tahun pengamatan (2017-2021). Tidak ada wilayah lain yang menyaingi atau melampaui Kabupaten Bogor selama periode tersebut."
        },
        {
            "icon": "M13 7h8m0 0v8m0-8l-8 8-4-4-6 6",
            "pertanyaan": "Tren Jumlah Penderita DM di Jawa Barat",
            "jawaban": "Jumlah penderita DM di Jawa Barat cenderung NAIK secara konsisten dari tahun ke tahun. Terjadi peningkatan dari ~120.000 kasus (2017) menjadi ~165.000 kasus (2021), atau meningkat sekitar 37.5%* dalam 5 tahun tanpa ada penurunan sama sekali."
        },
        {
            "icon": "M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0z",
            "pertanyaan": "Sebaran Kategori Risiko (Rendah/Sedang/Tinggi)",
            "jawaban": "Lebih banyak kabupaten/kota berada di kategori RENDAH (52% Atau 14 wilayah), diikuti kategori SEDANG (33% Atau 9 wilayah), dan kategori TINGGI (15% Atau 4 wilayah). Hal ini menunjukkan bahwa meskipun mayoritas wilayah masih memiliki jumlah penderita relatif rendah, terdapat ketimpangan geografis yang signifikan dengan beberapa wilayah urban besar mengalami beban DM yang sangat tinggi."
        }
    ]

    # 4. Data untuk Galeri Visualisasi
    grafik_list = [
        {
            "id": "Top10",
            "judul": "Top 10 Kabupaten/Kota Penderita DM Terbanyak",
            "filename": "images/no20.png",
            "deskripsi": "Kabupaten Bogor mendominasi dengan >25.000 kasus, diikuti Kota Bandung dan Kabupaten Bandung. Menunjukkan konsentrasi kasus di wilayah urban besar dan penyangga ibu kota."
        },
        {
            "id": "TrenTop5",
            "judul": "Tren Penderita DM Top 5 Wilayah (2017-2021)",
            "filename": "images/no21.png",
            "deskripsi": "Kabupaten Bogor konsisten tertinggi sepanjang periode. Semua wilayah menunjukkan tren peningkatan stabil, mengindikasikan masalah DM yang persisten di wilayah-wilayah kritis."
        },
        {
            "id": "TrenProvinsi",
            "judul": "Total Penderita DM Jawa Barat per Tahun",
            "filename": "images/no22.png",
            "deskripsi": "Tren naik konsisten dari ~120.000 (2017) menjadi ~165.000 kasus (2021). Peningkatan 37.5% dalam 5 tahun menunjukkan DM sebagai ancaman kesehatan yang semakin serius."
        },
        {
            "id": "PieKategori",
            "judul": "Distribusi Kategori Risiko Wilayah",
            "filename": "images/no23.png",
            "deskripsi": "52% wilayah kategori Rendah, 33% Sedang, dan 15% Tinggi. Mayoritas wilayah masih aman, namun terdapat ketimpangan geografis yang signifikan dengan beberapa wilayah mengalami beban sangat tinggi."
        },
        {
            "id": "BarKategori",
            "judul": "Jumlah Kabupaten/Kota per Kategori Risiko",
            "filename": "images/no24.png",
            "deskripsi": "14 wilayah kategori Rendah, 9 wilayah Sedang, dan 4 wilayah Tinggi dari total 27 kabupaten/kota. Empat wilayah kategori tinggi memerlukan prioritas intervensi kesehatan."
        }
    ]

    return render_template(
        'index.html',
        judul="Analisis Diabetes Mellitus di Jawa Barat",
        data_wilayah=data_wilayah,
        ringkasan=ringkasan,
        eksplorasi=eksplorasi_lengkap,  # <-- Menggunakan data lengkap (soal 1-19)
        analisis_temuan=analisis_temuan,
        grafik_list=grafik_list,
        total_penderita_tabel=total_penderita_tabel
    )

if __name__ == '__main__':
    app.run(debug=True)