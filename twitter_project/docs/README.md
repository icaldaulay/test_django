# Twitter Clone Application Documentation

## Deskripsi Aplikasi

Aplikasi Twitter Clone adalah platform microblogging sederhana yang dibangun menggunakan Django 5.2.6. Aplikasi ini memungkinkan pengguna untuk:

- Membuat akun dan login/logout
- Menulis tweet dengan batasan 140 karakter
- Menambahkan lokasi pada setiap tweet dengan dukungan GPS
- Upload foto pada tweet
- Melihat timeline semua tweet dari pengguna
- Melihat profil pengguna
- Menjelajahi tweet berdasarkan lokasi geografis di peta interaktif
- Search dan filter tweet berdasarkan konten, pengguna, atau lokasi

## Teknologi yang Digunakan

### Backend

- **Django 5.2.6**: Web framework utama
- **SQLite**: Database (default Django)
- **Python 3.13**: Bahasa pemrograman

### Frontend

- **Bootstrap 5.1.3**: CSS framework untuk responsive design
- **jQuery 3.6.0**: JavaScript library
- **Leaflet.js 1.9.4**: Library untuk peta interaktif
- **Font Awesome**: Icon library

### APIs

- **Nominatim API**: Geocoding service (OpenStreetMap)
- **Photon API**: Alternative geocoding service (Komoot)

## Struktur Database

Aplikasi menggunakan 2 model utama dengan relasi One-to-Many:

### 1. User Model (Custom User)

Extends dari `AbstractUser` Django dengan field tambahan:

- `bio`: Biography pengguna (160 karakter)
- `location`: Lokasi pengguna (30 karakter)
- `birth_date`: Tanggal lahir
- `avatar`: Foto profil
- `created_at`: Timestamp registrasi

### 2. Tweet Model

Model utama untuk menyimpan data tweet dengan lokasi:

- `user`: Foreign Key ke User (CASCADE)
- `content`: Isi tweet (140 karakter)
- `location`: Nama lokasi (required)
- `latitude/longitude`: Koordinat GPS (opsional)
- `image`: Foto tweet (opsional)
- `created_at/updated_at`: Timestamps

**Relasi**: User dapat memiliki banyak Tweet (1:N)

## Features

### Core Features

- ✅ User Authentication (Register, Login, Logout)
- ✅ Create Tweet (dengan lokasi wajib)
- ✅ Upload foto pada tweet
- ✅ Timeline dengan pagination (5 tweets per halaman)
- ✅ GPS Coordinate support
- ✅ User Profile pages
- ✅ Delete tweet (hanya pemilik)

### Advanced Features

- ✅ Interactive Map dengan Leaflet.js
- ✅ Real-time location search dengan multiple APIs
- ✅ Tweet markers pada peta dengan popup detail
- ✅ Search & filter tweets di peta
- ✅ Statistics dashboard pada peta
- ✅ Responsive design untuk mobile
- ✅ Enhanced UI/UX dengan animations
- ✅ RESTful API endpoint

## Version History

- **v1.0.0**: Basic Twitter functionality
- **v1.1.0**: Added location support and GPS coordinates
- **v1.2.0**: Enhanced UI with Bootstrap 5
- **v1.3.0**: Added photo upload functionality
- **v2.0.0**: Complete map integration with Leaflet.js
- **v2.1.0**: Enhanced location search with multiple APIs
- **v2.2.0**: Advanced map features (search, filter, statistics)

## 📚 Dokumentasi Lengkap

Dokumentasi aplikasi terdiri dari beberapa file terpisah:

### 🗂️ Struktur & Arsitektur

- **[Entity Relationship Diagram (ERD)](ERD.md)**: Struktur database dan relasi antar tabel
- **[Application Architecture](ARCHITECTURE.md)**: Arsitektur sistem dan komponen aplikasi
- **[Project Structure](PROJECT_STRUCTURE.md)**: Struktur direktori dan penjelasan file

### 🔄 User Experience

- **[User Flow Diagram](USER_FLOW.md)**: Alur pengguna dan navigasi aplikasi

### 🚀 Deployment

- **[Deployment Guide](DEPLOYMENT.md)**: Tutorial deployment untuk Windows & Linux
  - Windows (IIS + Apache)
  - Linux (Nginx + Gunicorn)
  - Cloud (Heroku, AWS)
  - Docker containerization

### 🔌 API Integration

- **[API Documentation](API_DOCS.md)**: RESTful API endpoints dan format data

### 📋 Quick Links

- [Instalasi & Setup](#installation)
- [Menjalankan Aplikasi](#running)
- [Testing](#testing)
- [Contributing](#contributing)

---

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git (for cloning)

### Setup Steps

1. **Clone Repository**:

   ```bash
   git clone https://github.com/your-repo/twitter_project.git
   cd twitter_project
   ```

2. **Create Virtual Environment**:

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create Superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

## 🏃‍♂️ Running

### Development Server

```bash
python manage.py runserver
```

Akses aplikasi di: http://127.0.0.1:8000

### Available URLs

- `/` - Home/Dashboard
- `/login/` - User Login
- `/register/` - User Registration
- `/map/` - Interactive Map
- `/api/posts/` - RESTful API
- `/admin/` - Django Admin Panel

## 🧪 Testing

### Run Tests

```bash
python manage.py test
```

### Check Code Coverage

```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

Project ini dibuat untuk keperluan edukasi dan pengembangan portfolio.

---

**Author**: Twitter Clone Development Team  
**Created**: September 2025  
**Documentation Version**: 2.2.0
