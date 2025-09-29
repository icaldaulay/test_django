# Application Architecture Diagram

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        PRESENTATION LAYER                       │
├─────────────────────────────────────────────────────────────────┤
│  Web Browser (Chrome, Firefox, Safari, Edge)                   │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │   HTML/CSS/JS   │  │   Bootstrap 5   │  │   jQuery 3.6    │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │  Leaflet.js     │  │  Font Awesome   │  │  Responsive     │ │
│  │  (Maps)         │  │  (Icons)        │  │  Design         │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                                │
                          HTTP/HTTPS
                                │
┌─────────────────────────────────────────────────────────────────┐
│                      APPLICATION LAYER                          │
├─────────────────────────────────────────────────────────────────┤
│                    Django 5.2.6 Framework                      │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │    URL Router   │  │   Middleware    │  │   Templates     │ │
│  │   (urls.py)     │  │   Pipeline      │  │   (Jinja2)      │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                │                                │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │     Views       │  │     Forms       │  │   Static Files  │ │
│  │   (views.py)    │  │   (forms.py)    │  │   Handler       │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                                │
                          ORM (Django)
                                │
┌─────────────────────────────────────────────────────────────────┐
│                        DATA LAYER                               │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │    Models       │  │   SQLite DB     │  │   Media Files   │ │
│  │  (models.py)    │  │   (db.sqlite3)  │  │   (Images)      │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                                                                 │
│  Database Tables:              File Storage:                   │
│  • auth_user (Django built-in) • /media/avatars/              │
│  • twitter_user (Custom)       • /media/tweet_images/         │
│  • twitter_tweet               • /static/css/                 │
│                                • /static/js/                  │
│                                • /static/images/              │
└─────────────────────────────────────────────────────────────────┘
```

## External Services Integration

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXTERNAL APIs & SERVICES                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │  Nominatim API  │  │   Photon API    │  │   Browser GPS   │ │
│  │ (OpenStreetMap) │  │    (Komoot)     │  │  Geolocation    │ │
│  │   Geocoding     │  │   Geocoding     │  │     API         │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│           │                     │                     │         │
│           │                     │                     │         │
│      REST API              REST API              JavaScript     │
│      (JSON)                (JSON)                Navigator      │
└─────────────────────────────────────────────────────────────────┘
                                │
                          HTTP Requests
                                │
┌─────────────────────────────────────────────────────────────────┐
│                       DJANGO APPLICATION                        │
│                                                                 │
│  Location Search Flow:                                          │
│  1. User types location → JavaScript                           │
│  2. Promise.allSettled([Nominatim, Photon])                   │
│  3. Merge and rank results                                      │
│  4. Display suggestions to user                                │
│  5. Save coordinates to Tweet model                            │
└─────────────────────────────────────────────────────────────────┘
```

## Django Application Structure

```
twitter_project/
├── manage.py                    # Django management script
├── app_config/                  # Project settings
│   ├── __init__.py
│   ├── settings.py             # Configuration
│   ├── urls.py                 # Root URL routing
│   ├── wsgi.py                 # WSGI application
│   └── asgi.py                 # ASGI application (async)
├── twitter/                     # Main application
│   ├── __init__.py
│   ├── models.py               # Data models (User, Tweet)
│   ├── views.py                # Business logic
│   ├── forms.py                # Form validation
│   ├── urls.py                 # App URL routing
│   ├── admin.py                # Admin interface
│   ├── apps.py                 # App configuration
│   ├── tests.py                # Unit tests
│   └── migrations/             # Database migrations
├── templates/                   # HTML templates
│   ├── base.html               # Base template
│   ├── login.html              # Authentication
│   ├── register.html           # User registration
│   ├── dashboard.html          # Main timeline
│   ├── profile.html            # User profiles
│   ├── map.html                # Interactive map
│   └── api_view.html           # API documentation
├── static/                      # Static assets
│   ├── css/
│   │   └── style.css           # Custom styles
│   ├── js/                     # JavaScript files
│   └── images/                 # Static images
└── media/                       # User uploads
    ├── avatars/                # Profile pictures
    └── tweet_images/           # Tweet photos
```

## MVC (Model-View-Controller) Pattern

### Model Layer

```python
# models.py
class User(AbstractUser):
    # Extended user model with additional fields
    bio = models.TextField(max_length=160, blank=True)
    location = models.CharField(max_length=30, blank=True)
    # ... other fields

class Tweet(models.Model):
    # Tweet model with location support
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=140)
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=16, decimal_places=10)
    # ... other fields
```

### View Layer (Controller in MVC)

```python
# views.py
@login_required
def dashboard_view(request):
    # Handle tweet creation and display timeline
    if request.method == 'POST':
        # Process new tweet with location data

    tweets = Tweet.objects.all().select_related('user')
    # Pagination and context preparation
    return render(request, 'dashboard.html', context)

def api_posts(request):
    # RESTful API endpoint
    # Return JSON data for external consumption
    return JsonResponse(data)
```

### Template Layer (View in MVC)

```html
<!-- dashboard.html -->
<div class="tweet-form">
  <!-- Tweet creation form with location search -->
</div>

<div class="timeline">
  <!-- Tweet display with pagination -->
  {% for tweet in page_obj %}
  <!-- Tweet card with user info, content, location -->
  {% endfor %}
</div>
```

## Request/Response Flow

```
1. Browser Request
   │
   ├── Static Files (CSS/JS/Images)
   │   └── Django Static Files Handler
   │       └── Served directly
   │
   └── Dynamic Content
       │
       1. URL Dispatcher (urls.py)
       │
       2. Middleware Pipeline
       │   ├── Security Middleware
       │   ├── Session Middleware
       │   ├── Authentication Middleware
       │   └── CSRF Middleware
       │
       3. View Function (views.py)
       │   ├── Authentication Check
       │   ├── Form Processing
       │   ├── Database Query (ORM)
       │   └── Context Preparation
       │
       4. Template Rendering
       │   ├── Load Template (HTML)
       │   ├── Context Variables
       │   ├── Template Tags/Filters
       │   └── Generate HTML
       │
       5. HTTP Response
           └── HTML + Status Code
```

## Security Architecture

### Authentication & Authorization

- Django built-in authentication system
- Session-based authentication
- CSRF protection for forms
- Login required decorators for protected views

### Data Validation

- Form validation in forms.py
- Model field validation
- Input sanitization
- File upload validation (images only)

### Security Headers

- CSRF tokens
- Secure cookie settings
- Content Security Policy (via middleware)

## Performance Considerations

### Database Optimization

- select_related() for foreign key queries
- Pagination to limit data load
- Database indexes on frequently queried fields

### Frontend Optimization

- CDN for Bootstrap and jQuery
- Minified CSS/JS files
- Image optimization for uploads
- Responsive design for mobile performance

### Caching Strategy

- Django's built-in caching framework ready for implementation
- Static file caching via web server
- Browser caching for assets

## Scalability Architecture

### Current Setup (Development)

- Single server deployment
- SQLite database
- Local file storage for media

### Production Recommendations

- PostgreSQL/MySQL database
- Redis for caching
- AWS S3/CloudFront for media files
- Load balancer for multiple app servers
- Celery for background tasks
