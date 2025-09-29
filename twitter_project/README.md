# Twitter Clone - Aplikasi Microblogging

Aplikasi Twitter sederhana yang dibuat dengan Django untuk Windows.

## Fitur Utama

- ✅ Register dan Login pengguna
- ✅ Posting tweet dengan lokasi (wajib)
- ✅ Upload foto di tweet
- ✅ Timeline semua tweet dengan pagination
- ✅ Peta interaktif untuk melihat lokasi tweet
- ✅ Search dan filter tweet di peta
- ✅ API endpoint untuk data tweet

## Cara Install

### 1. Persiapan

- Install Python 3.8+ dari [python.org](https://python.org)
- Install PostgreSQL dari [postgresql.org](https://postgresql.org) (opsional)

### 2. Setup Project

```bash
# Clone atau download project
cd twitter_project

# Buat virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py migrate

# Jalankan server
python manage.py runserver
```

### 3. Akses Aplikasi

Buka browser ke: http://127.0.0.1:8000

## Halaman Utama

- **Dashboard**: Timeline dan buat tweet baru
- **Map**: Peta interaktif lokasi tweet
- **API**: Data JSON untuk integrasi

## Database

Aplikasi menggunakan SQLite secara default (cocok untuk development).
Untuk production, bisa menggunakan PostgreSQL.

## Requirements

File `requirements.txt` berisi 3 package utama:

- **Django 5.2.6**: Framework web
- **Pillow**: Untuk upload gambar
- **psycopg2-binary**: PostgreSQL database adapter

## Dokumentasi Lengkap

Lihat folder `docs/` untuk dokumentasi detail:

- Struktur database
- Arsitektur aplikasi
- User flow
- Tutorial deployment

---

**Dibuat untuk kebutuhan pembelajaran dan portfolio development.**
