# Project Structure Documentation

## Complete Directory Structure

```
twitter_project/                           # Root project directory
├── manage.py                             # Django management command interface
├── .gitignore                            # Git ignore patterns
├── db.sqlite3                            # SQLite database file (auto-generated)
│
├── docs/                                 # Documentation files
│   ├── README.md                         # Project overview
│   ├── ERD.md                           # Entity Relationship Diagram
│   ├── ARCHITECTURE.md                   # Application architecture
│   ├── USER_FLOW.md                     # User flow diagrams
│   ├── PROJECT_STRUCTURE.md             # This file
│   ├── DEPLOYMENT.md                    # Deployment tutorials
│   └── API_DOCS.md                      # API documentation
│
├── app_config/                          # Django project configuration
│   ├── __init__.py                      # Python package marker
│   ├── settings.py                      # Django settings/configuration
│   ├── urls.py                          # Root URL configuration
│   ├── wsgi.py                          # WSGI application entry point
│   ├── asgi.py                          # ASGI application entry point
│   └── __pycache__/                     # Python bytecode cache
│       ├── __init__.cpython-313.pyc
│       ├── settings.cpython-313.pyc
│       ├── urls.cpython-313.pyc
│       └── wsgi.cpython-313.pyc
│
├── twitter/                             # Main Django application
│   ├── __init__.py                      # Python package marker
│   ├── models.py                        # Database models (User, Tweet)
│   ├── views.py                         # View functions/business logic
│   ├── forms.py                         # Django forms for validation
│   ├── urls.py                          # Application URL patterns
│   ├── admin.py                         # Django admin configuration
│   ├── apps.py                          # Application configuration
│   ├── tests.py                         # Unit tests
│   ├── __pycache__/                     # Python bytecode cache
│   │   ├── __init__.cpython-313.pyc
│   │   ├── admin.cpython-313.pyc
│   │   ├── apps.cpython-313.pyc
│   │   ├── forms.cpython-313.pyc
│   │   ├── models.cpython-313.pyc
│   │   ├── urls.cpython-313.pyc
│   │   └── views.cpython-313.pyc
│   └── migrations/                      # Database migration files
│       ├── __init__.py
│       ├── 0001_initial.py              # Initial models creation
│       ├── 0002_tweet_latitude_tweet_location_tweet_longitude_and_more.py
│       ├── 0003_tweet_image.py          # Add image field
│       ├── 0004_alter_tweet_latitude_alter_tweet_location_and_more.py
│       ├── 0005_alter_tweet_latitude_alter_tweet_longitude.py
│       └── __pycache__/                 # Migration bytecode cache
│           ├── __init__.cpython-313.pyc
│           ├── 0001_initial.cpython-313.pyc
│           ├── 0002_tweet_latitude_tweet_location_tweet_longitude_and_more.cpython-313.pyc
│           ├── 0003_tweet_image.cpython-313.pyc
│           ├── 0004_alter_tweet_latitude_alter_tweet_location_and_more.cpython-313.pyc
│           └── 0005_alter_tweet_latitude_alter_tweet_longitude.cpython-313.pyc
│
├── templates/                           # HTML template files
│   ├── base.html                        # Base template with navigation
│   ├── login.html                       # User login page
│   ├── register.html                    # User registration page
│   ├── dashboard.html                   # Main timeline/dashboard
│   ├── profile.html                     # User profile pages
│   ├── map.html                         # Interactive map with Leaflet.js
│   └── api_view.html                    # API documentation page
│
├── static/                              # Static files (CSS, JS, Images)
│   ├── css/
│   │   └── style.css                    # Main stylesheet
│   ├── js/                              # JavaScript files (if any)
│   ├── images/                          # Static images
│   └── Coding Test.pdf                  # Project requirements document
│
└── media/                               # User-uploaded files
    ├── avatars/                         # User profile pictures
    └── tweet_images/                    # Tweet photo uploads
        └── tkpsda.png                   # Example uploaded image
```

## File Descriptions

### Root Level Files

| File         | Purpose           | Description                                                           |
| ------------ | ----------------- | --------------------------------------------------------------------- |
| `manage.py`  | Django Management | Entry point for Django management commands (runserver, migrate, etc.) |
| `.gitignore` | Version Control   | Specifies files/folders to ignore in Git repository                   |
| `db.sqlite3` | Database          | SQLite database file (auto-generated on first migration)              |

### Configuration Directory (`app_config/`)

| File          | Purpose         | Description                                                       |
| ------------- | --------------- | ----------------------------------------------------------------- |
| `settings.py` | Configuration   | Main Django settings (database, installed apps, middleware, etc.) |
| `urls.py`     | URL Routing     | Root URL configuration that includes app-specific URLs            |
| `wsgi.py`     | WSGI Deployment | Web Server Gateway Interface for production deployment            |
| `asgi.py`     | ASGI Deployment | Asynchronous Server Gateway Interface for async features          |

### Main Application (`twitter/`)

| File        | Purpose           | Description                                                 |
| ----------- | ----------------- | ----------------------------------------------------------- |
| `models.py` | Data Models       | Database models (User, Tweet) with fields and relationships |
| `views.py`  | Business Logic    | View functions handling HTTP requests and responses         |
| `forms.py`  | Form Validation   | Django forms for user input validation and rendering        |
| `urls.py`   | URL Patterns      | Application-specific URL routing                            |
| `admin.py`  | Admin Interface   | Django admin panel configuration                            |
| `apps.py`   | App Configuration | Application configuration and metadata                      |
| `tests.py`  | Unit Tests        | Test cases for application functionality                    |

### Templates Directory (`templates/`)

| File             | Purpose           | Description                                    |
| ---------------- | ----------------- | ---------------------------------------------- |
| `base.html`      | Base Template     | Common HTML structure, navigation, and styling |
| `login.html`     | Authentication    | User login form and validation                 |
| `register.html`  | Registration      | New user registration form                     |
| `dashboard.html` | Main Interface    | Timeline, tweet creation, and pagination       |
| `profile.html`   | User Profiles     | Individual user profile and tweet listing      |
| `map.html`       | Interactive Map   | Leaflet.js map with tweet markers and search   |
| `api_view.html`  | API Documentation | API endpoint documentation and examples        |

### Static Files (`static/`)

| Directory/File  | Purpose       | Description                          |
| --------------- | ------------- | ------------------------------------ |
| `css/style.css` | Styling       | Custom CSS for application styling   |
| `js/`           | JavaScript    | Client-side JavaScript files         |
| `images/`       | Static Images | Logo, icons, and other static images |

### Media Directory (`media/`)

| Directory       | Purpose          | Description                 |
| --------------- | ---------------- | --------------------------- |
| `avatars/`      | Profile Pictures | User-uploaded avatar images |
| `tweet_images/` | Tweet Photos     | Photos attached to tweets   |

### Migration Files (`twitter/migrations/`)

| File                  | Purpose              | Description                               |
| --------------------- | -------------------- | ----------------------------------------- |
| `0001_initial.py`     | Initial Setup        | Creates User and Tweet models             |
| `0002_*.py`           | Location Fields      | Adds location, latitude, longitude fields |
| `0003_tweet_image.py` | Image Upload         | Adds image field to Tweet model           |
| `0004_*.py`           | Field Adjustments    | Modifies field types and constraints      |
| `0005_*.py`           | Coordinate Precision | Final adjustments to coordinate fields    |

## File Dependencies

### Template Inheritance

```
base.html
├── login.html
├── register.html
├── dashboard.html
├── profile.html
├── map.html
└── api_view.html
```

### URL Routing Hierarchy

```
app_config/urls.py (Root)
└── include('twitter.urls')
    └── twitter/urls.py (App URLs)
        ├── dashboard_view
        ├── login_view
        ├── register_view
        ├── map_view
        ├── profile_view
        ├── api_posts
        └── api_view
```

### Model Relationships

```
User (AbstractUser)
└── Tweet (ForeignKey)
    ├── content
    ├── location
    ├── coordinates (lat/lng)
    └── image
```

## Configuration Files

### Django Settings (`app_config/settings.py`)

Key configurations:

- Database: SQLite (development)
- Static files: `/static/` URL prefix
- Media files: `/media/` URL prefix
- Templates: Template directory location
- Installed apps: django.contrib.\*, twitter app
- Middleware: Security, sessions, authentication
- Time zone: UTC
- Language: English

### URL Configuration (`app_config/urls.py`)

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('twitter.urls')),
]
```

### App URLs (`twitter/urls.py`)

```python
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('map/', views.map_view, name='map'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('api/posts/', views.api_posts, name='api_posts'),
    path('api/', views.api_view, name='api_view'),
    path('delete/<int:tweet_id>/', views.delete_tweet, name='delete_tweet'),
]
```

## Code Organization Patterns

### MVC Pattern Implementation

- **Models** (`models.py`): Data structure and business rules
- **Views** (`views.py`): Request handling and business logic
- **Templates** (`templates/`): Presentation layer

### Form Handling Pattern

```python
# views.py
if request.method == 'POST':
    form = TweetForm(request.POST, request.FILES)
    if form.is_valid():
        # Process form
    else:
        # Show errors

# forms.py
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'location', 'image']
```

### Authentication Pattern

```python
@login_required
def protected_view(request):
    # Only accessible to logged-in users
    pass
```

## Development Workflow

### Adding New Features

1. **Models**: Update `models.py` if database changes needed
2. **Migrations**: Run `python manage.py makemigrations`
3. **Views**: Add business logic in `views.py`
4. **URLs**: Add URL patterns in `urls.py`
5. **Templates**: Create/update HTML templates
6. **Static Files**: Add CSS/JS if needed
7. **Testing**: Add tests in `tests.py`

### File Modification Guidelines

- **Never edit**: `__pycache__/`, migration files (after applied)
- **Safe to edit**: `views.py`, `templates/`, `static/`, `forms.py`
- **Caution**: `models.py` (requires migrations), `settings.py`

## Production Considerations

### Files to Exclude from Deployment

- `__pycache__/` directories
- `db.sqlite3` (use production database)
- `*.pyc` files
- Development-specific settings

### Files Required for Deployment

- All Python source files
- Templates and static files
- Migration files
- `requirements.txt` (package dependencies)
- Production settings configuration
