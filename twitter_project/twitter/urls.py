from django.urls import path
from . import views

urlpatterns = [
    # 4 Halaman Utama sesuai kebutuhan
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),           # Halaman 1: Login
    path('dashboard/', views.dashboard_view, name='dashboard'), # Halaman 2: Dashboard
    path('map/', views.map_view, name='map'),                 # Halaman 3: Peta Lokasi
    path('api/', views.api_view, name='api_view'),            # Halaman 4: API View
    path('api/posts/', views.api_posts, name='api_posts'),    # API Endpoint
    
    # URL tambahan
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('delete_tweet/<int:tweet_id>/', views.delete_tweet, name='delete_tweet'),
]