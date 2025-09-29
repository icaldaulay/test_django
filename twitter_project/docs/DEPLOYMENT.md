# Deployment Tutorial

## Deployment Options Overview

Tutorial ini mencakup deployment aplikasi Twitter Clone Django di berbagai lingkungan:

1. **Windows Deployment** (IIS + mod_wsgi atau Apache)
2. **Linux/Ubuntu Deployment** (Nginx + Gunicorn)
3. **Cloud Deployment** (Heroku, AWS, DigitalOcean)
4. **Docker Deployment** (Containerized)

---

## 1. Windows Deployment dengan IIS

### Prerequisites

- Windows Server 2016/2019/2022 atau Windows 10/11 Pro
- IIS (Internet Information Services) enabled
- Python 3.8+ installed
- pip dan virtualenv

### Step 1: Prepare Application

1. **Clone atau copy project ke server**:

   ```cmd
   mkdir C:\inetpub\wwwroot\twitter_project
   cd C:\inetpub\wwwroot\twitter_project
   # Copy semua file project ke direktori ini
   ```

2. **Create Virtual Environment**:

   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```cmd
   # Option 1: Use Windows-specific requirements file
   pip install -r requirements-windows.txt

   # Option 2: Install complete dependencies
   pip install -r requirements.txt

   # Option 3: Install manually
   pip install django pillow wfastcgi psycopg2-binary gunicorn
   ```

4. **Available Requirements Files**:

   - `requirements.txt` - Complete dependencies
   - `requirements-windows.txt` - Windows IIS deployment
   - `requirements-prod.txt` - Production minimal
   - `requirements-dev.txt` - Development tools

   See `REQUIREMENTS_GUIDE.md` for detailed explanations.

### Step 2: Configure Django for Production

1. **Update settings.py**:

   ```python
   # settings.py
   import os

   DEBUG = False
   ALLOWED_HOSTS = ['your-domain.com', 'localhost', '127.0.0.1']

   # Static files
   STATIC_URL = '/static/'
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

   # Media files
   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

   # Database (keep SQLite for simplicity or use SQL Server)
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

2. **Collect Static Files**:

   ```cmd
   python manage.py collectstatic
   ```

3. **Run Migrations**:
   ```cmd
   python manage.py migrate
   ```

### Step 3: Configure IIS

1. **Enable IIS Features**:

   - Open "Turn Windows features on or off"
   - Enable Internet Information Services
   - Enable CGI under Application Development Features

2. **Install wfastcgi**:

   ```cmd
   pip install wfastcgi
   wfastcgi-enable
   ```

3. **Create web.config**:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <configuration>
     <system.webServer>
       <handlers>
         <add name="Python FastCGI"
              path="*"
              verb="*"
              modules="FastCgiModule"
              scriptProcessor="C:\inetpub\wwwroot\twitter_project\venv\Scripts\python.exe|C:\inetpub\wwwroot\twitter_project\venv\Lib\site-packages\wfastcgi.py"
              resourceType="Unspecified" />
       </handlers>
       <staticContent>
         <mimeMap fileExtension=".woff" mimeType="application/font-woff" />
         <mimeMap fileExtension=".woff2" mimeType="application/font-woff2" />
       </staticContent>
     </system.webServer>
     <appSettings>
       <add key="WSGI_HANDLER" value="app_config.wsgi.application" />
       <add key="PYTHONPATH" value="C:\inetpub\wwwroot\twitter_project" />
       <add key="DJANGO_SETTINGS_MODULE" value="app_config.settings" />
     </appSettings>
   </configuration>
   ```

### Step 4: Configure IIS Site

1. **Open IIS Manager**
2. **Add Website**:

   - Site name: TwitterProject
   - Physical path: C:\inetpub\wwwroot\twitter_project
   - Port: 80 (or 443 for HTTPS)

3. **Configure FastCGI**:
   - Go to FastCGI Settings
   - Add application:
     - Full Path: C:\inetpub\wwwroot\twitter_project\venv\Scripts\python.exe
     - Arguments: C:\inetpub\wwwroot\twitter_project\venv\Lib\site-packages\wfastcgi.py

---

## 2. Windows Deployment dengan Apache

### Prerequisites

- XAMPP atau Apache HTTP Server
- mod_wsgi for Python
- Python 3.8+

### Step 1: Install Apache dan mod_wsgi

1. **Download dan install XAMPP**:

   ```
   https://www.apachefriends.org/download.html
   ```

2. **Install mod_wsgi**:

   ```cmd
   pip install mod_wsgi
   mod_wsgi-express module-config
   ```

3. **Copy output ke httpd.conf**:
   ```apache
   LoadFile "c:/python313/python313.dll"
   LoadModule wsgi_module "c:/python313/lib/site-packages/mod_wsgi/server/mod_wsgi.cp313-win_amd64.pyd"
   WSGIPythonHome "c:/python313"
   ```

### Step 2: Configure Apache Virtual Host

1. **Edit httpd-vhosts.conf**:

   ```apache
   <VirtualHost *:80>
       ServerName localhost
       DocumentRoot "C:/xampp/htdocs/twitter_project"

       WSGIScriptAlias / "C:/xampp/htdocs/twitter_project/app_config/wsgi.py"
       WSGIPythonPath "C:/xampp/htdocs/twitter_project"

       <Directory "C:/xampp/htdocs/twitter_project/app_config">
           <Files wsgi.py>
               Require all granted
           </Files>
       </Directory>

       Alias /static "C:/xampp/htdocs/twitter_project/staticfiles"
       <Directory "C:/xampp/htdocs/twitter_project/staticfiles">
           Require all granted
       </Directory>

       Alias /media "C:/xampp/htdocs/twitter_project/media"
       <Directory "C:/xampp/htdocs/twitter_project/media">
           Require all granted
       </Directory>
   </VirtualHost>
   ```

---

## 3. Linux/Ubuntu Deployment dengan Nginx + Gunicorn

### Prerequisites

- Ubuntu 20.04/22.04 LTS
- Python 3.8+
- Nginx
- Gunicorn

### Step 1: Setup Server Environment

1. **Update system**:

   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

2. **Install dependencies**:

   ```bash
   sudo apt install python3 python3-pip python3-venv nginx postgresql postgresql-contrib
   ```

3. **Create user for application**:
   ```bash
   sudo adduser twitter
   sudo usermod -aG sudo twitter
   su - twitter
   ```

### Step 2: Setup Application

1. **Clone project**:

   ```bash
   cd /home/twitter
   git clone https://github.com/your-repo/twitter_project.git
   cd twitter_project
   ```

2. **Create virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   # Option 1: Production minimal (recommended for servers)
   pip install -r requirements-prod.txt

   # Option 2: Complete dependencies
   pip install -r requirements.txt

   # Option 3: Docker optimized
   pip install -r requirements-docker.txt
   ```

### Step 3: Configure Database (PostgreSQL)

1. **Setup PostgreSQL**:

   ```bash
   sudo -u postgres psql
   ```

   ```sql
   CREATE DATABASE twitter_db;
   CREATE USER twitter_user WITH PASSWORD 'strong_password';
   GRANT ALL PRIVILEGES ON DATABASE twitter_db TO twitter_user;
   \q
   ```

2. **Update Django settings**:
   ```python
   # settings.py
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'twitter_db',
           'USER': 'twitter_user',
           'PASSWORD': 'strong_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### Step 4: Configure Django for Production

1. **Production settings**:

   ```python
   # settings.py
   DEBUG = False
   ALLOWED_HOSTS = ['your-domain.com', 'your-ip-address']

   STATIC_URL = '/static/'
   STATIC_ROOT = '/home/twitter/twitter_project/staticfiles'

   MEDIA_URL = '/media/'
   MEDIA_ROOT = '/home/twitter/twitter_project/media'
   ```

2. **Run migrations and collect static**:
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   python manage.py createsuperuser
   ```

### Step 5: Configure Gunicorn

1. **Test Gunicorn**:

   ```bash
   cd /home/twitter/twitter_project
   gunicorn --bind 0.0.0.0:8000 app_config.wsgi:application
   ```

2. **Create Gunicorn systemd service**:

   ```bash
   sudo nano /etc/systemd/system/gunicorn.service
   ```

   ```ini
   [Unit]
   Description=gunicorn daemon
   After=network.target

   [Service]
   User=twitter
   Group=www-data
   WorkingDirectory=/home/twitter/twitter_project
   ExecStart=/home/twitter/twitter_project/venv/bin/gunicorn \
             --access-logfile - \
             --workers 3 \
             --bind unix:/home/twitter/twitter_project/twitter_project.sock \
             app_config.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

3. **Enable and start service**:
   ```bash
   sudo systemctl start gunicorn
   sudo systemctl enable gunicorn
   sudo systemctl status gunicorn
   ```

### Step 6: Configure Nginx

1. **Create Nginx configuration**:

   ```bash
   sudo nano /etc/nginx/sites-available/twitter_project
   ```

   ```nginx
   server {
       listen 80;
       server_name your-domain.com your-ip-address;

       location = /favicon.ico { access_log off; log_not_found off; }

       location /static/ {
           root /home/twitter/twitter_project;
       }

       location /media/ {
           root /home/twitter/twitter_project;
       }

       location / {
           include proxy_params;
           proxy_pass http://unix:/home/twitter/twitter_project/twitter_project.sock;
       }
   }
   ```

2. **Enable site**:

   ```bash
   sudo ln -s /etc/nginx/sites-available/twitter_project /etc/nginx/sites-enabled
   sudo nginx -t
   sudo systemctl restart nginx
   ```

3. **Configure firewall**:
   ```bash
   sudo ufw allow 'Nginx Full'
   sudo ufw enable
   ```

---

## 4. SSL/HTTPS Configuration (Let's Encrypt)

### For Linux/Ubuntu with Nginx

1. **Install Certbot**:

   ```bash
   sudo apt install certbot python3-certbot-nginx
   ```

2. **Obtain SSL certificate**:

   ```bash
   sudo certbot --nginx -d your-domain.com
   ```

3. **Test renewal**:
   ```bash
   sudo certbot renew --dry-run
   ```

---

## 5. Docker Deployment

### Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app_config.wsgi:application"]
```

### Create docker-compose.yml

```yaml
version: "3.8"

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    environment:
      - DEBUG=False
    depends_on:
      - db

  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_DB=twitter_db
      - POSTGRES_USER=twitter_user
      - POSTGRES_PASSWORD=strong_password

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

### Deploy with Docker

```bash
docker-compose up -d --build
```

---

## 6. Cloud Deployment (Heroku)

### Step 1: Prepare for Heroku

1. **Install Heroku CLI**
2. **Create Procfile**:

   ```
   web: gunicorn app_config.wsgi --log-file -
   ```

3. **Create runtime.txt**:

   ```
   python-3.11.0
   ```

4. **Update requirements.txt**:
   ```
   django
   gunicorn
   pillow
   dj-database-url
   whitenoise
   psycopg2
   ```

### Step 2: Configure Django for Heroku

```python
# settings.py
import dj_database_url
import os

# Production settings
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL')
        )
    }

# Whitenoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Step 3: Deploy to Heroku

```bash
heroku create twitter-clone-app
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

---

## 7. Monitoring dan Maintenance

### Log Files Locations

**Windows IIS**:

- Application logs: `C:\inetpub\logs\LogFiles\`
- Python errors: Check Event Viewer

**Linux**:

- Nginx: `/var/log/nginx/`
- Gunicorn: Use systemd journal `sudo journalctl -u gunicorn`
- Django: Configure logging in settings.py

### Performance Monitoring

```python
# settings.py - Production logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/twitter.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### Backup Strategy

1. **Database backup**:

   ```bash
   # PostgreSQL
   pg_dump twitter_db > backup_$(date +%Y%m%d).sql

   # SQLite
   cp db.sqlite3 backup_$(date +%Y%m%d).sqlite3
   ```

2. **Media files backup**:
   ```bash
   tar -czf media_backup_$(date +%Y%m%d).tar.gz media/
   ```

### Security Checklist

- [ ] DEBUG = False in production
- [ ] Strong SECRET_KEY
- [ ] HTTPS enabled
- [ ] Database credentials secured
- [ ] Regular security updates
- [ ] Firewall configured
- [ ] File upload validation
- [ ] Rate limiting implemented

---

## Troubleshooting Common Issues

### 1. Static Files Not Loading

```python
# Ensure in settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Run collectstatic
python manage.py collectstatic
```

### 2. Database Connection Errors

- Check database credentials
- Ensure database service is running
- Verify network connectivity

### 3. Permission Errors (Linux)

```bash
sudo chown -R twitter:www-data /home/twitter/twitter_project
sudo chmod -R 755 /home/twitter/twitter_project
```

### 4. Gunicorn Socket Errors

```bash
sudo systemctl status gunicorn
sudo journalctl -u gunicorn
sudo systemctl restart gunicorn
```

---

**Deployment Complete!** Your Twitter Clone application should now be accessible via your domain or IP address.
