from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils import timezone

class User(AbstractUser):
    """Custom User model dengan additional fields"""
    bio = models.TextField(max_length=160, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    
    # Properties untuk follow system dihapus karena tidak diperlukan

class Tweet(models.Model):
    """Model untuk menyimpan tweet dengan lokasi"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    content = models.TextField(max_length=140)  # Ubah dari 280 ke 140 karakter
    location = models.CharField(max_length=255)  # Field lokasi wajib
    latitude = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)  # Koordinat untuk peta (-90.0000000000 to 90.0000000000)
    longitude = models.DecimalField(max_digits=16, decimal_places=10, null=True, blank=True)  # Koordinat untuk peta (-180.0000000000 to 180.0000000000)
    image = models.ImageField(upload_to='tweet_images/', null=True, blank=True)  # Field untuk upload foto
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username}: {self.content[:50]} - {self.location}"
    
    @property
    def time_since_posted(self):
        return timezone.now() - self.created_at

# Model Follow dihapus karena tidak diperlukan dalam kebutuhan baru
