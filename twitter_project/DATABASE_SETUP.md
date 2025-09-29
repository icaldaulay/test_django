# Database Setup Guide

## PostgreSQL Setup (Recommended)

### 1. Install PostgreSQL

- Download dari: https://www.postgresql.org/download/windows/
- Install dengan default settings
- Catat password yang Anda set untuk user `postgres`

### 2. Create Database

```sql
-- Buka pgAdmin atau psql command line
CREATE DATABASE twitter_db;
CREATE USER twitter_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE twitter_db TO twitter_user;
```

### 3. Update Settings

Edit `app_config/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'twitter_db',
        'USER': 'twitter_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## MySQL Setup (Alternative)

### 1. Install MySQL

- Download dari: https://dev.mysql.com/downloads/installer/
- Install MySQL Server dan MySQL Workbench

### 2. Create Database

```sql
-- Buka MySQL Workbench atau command line
CREATE DATABASE twitter_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'twitter_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON twitter_db.* TO 'twitter_user'@'localhost';
FLUSH PRIVILEGES;
```

### 3. Install MySQL Driver

```bash
pip install mysqlclient
```

### 4. Update Settings

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'twitter_db',
        'USER': 'twitter_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        }
    }
}
```

## SQLite Setup (Development Only)

### Quick Testing

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## Migration Commands

```bash
# Setelah setup database
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Error Troubleshooting

### PostgreSQL Connection Error

- Pastikan PostgreSQL service running
- Cek port 5432 tidak diblokir firewall
- Verifikasi username/password benar

### MySQL Connection Error

- Pastikan MySQL service running
- Cek port 3306 tidak diblokir firewall
- Install mysqlclient driver

### Permission Error

- Pastikan user database memiliki privilege yang cukup
- Run `GRANT ALL PRIVILEGES` commands
