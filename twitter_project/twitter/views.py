from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from decimal import Decimal
from .forms import CustomUserCreationForm, TweetForm
from .models import User, Tweet

def home_view(request):
    """Home page - redirect to login if not authenticated"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')

def login_view(request):
    """Halaman Login dengan error handling yang lebih baik"""
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        # Validasi input kosong
        if not username or not password:
            messages.error(request, '⚠️ Username dan password harus diisi!')
            return render(request, 'login.html')
        
        # Cek apakah username terlalu pendek
        if len(username) < 3:
            messages.error(request, '⚠️ Username minimal 3 karakter!')
            return render(request, 'login.html')
        
        try:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f'✅ Selamat datang, {user.username}!')
                    return redirect('dashboard')
                else:
                    messages.error(request, '🔒 Akun Anda tidak aktif. Hubungi administrator.')
            else:
                # Cek apakah user exists
                if User.objects.filter(username=username).exists():
                    messages.error(request, '🔑 Password salah. Silakan coba lagi.')
                else:
                    messages.error(request, '👤 Username tidak ditemukan. Silakan daftar terlebih dahulu.')
        
        except Exception as e:
            messages.error(request, '❌ Terjadi kesalahan sistem. Silakan coba lagi.')
    
    return render(request, 'login.html')

def register_view(request):
    """User registration view dengan error handling yang lebih baik"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        # Validasi manual tambahan
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        
        # Validasi input kosong
        if not all([username, email, password1, password2]):
            messages.error(request, '⚠️ Semua field harus diisi!')
            return render(request, 'register.html', {'form': form})
        
        # Validasi username sudah ada
        if User.objects.filter(username=username).exists():
            messages.error(request, f'👤 Username "{username}" sudah digunakan. Pilih username lain.')
            return render(request, 'register.html', {'form': form})
        
        # Validasi email sudah ada
        if User.objects.filter(email=email).exists():
            messages.error(request, f'📧 Email "{email}" sudah terdaftar. Gunakan email lain atau login.')
            return render(request, 'register.html', {'form': form})
        
        # Validasi password tidak sama
        if password1 != password2:
            messages.error(request, '🔑 Password dan konfirmasi password tidak sama!')
            return render(request, 'register.html', {'form': form})
        
        # Validasi panjang password
        if len(password1) < 8:
            messages.error(request, '🔐 Password minimal 8 karakter!')
            return render(request, 'register.html', {'form': form})
        
        try:
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'🎉 Akun berhasil dibuat untuk {username}! Selamat bergabung!')
                login(request, user)
                return redirect('dashboard')
            else:
                # Tampilkan error dari form
                for field, errors in form.errors.items():
                    for error in errors:
                        if 'password' in field.lower():
                            messages.error(request, f'🔑 Password: {error}')
                        elif 'username' in field.lower():
                            messages.error(request, f'👤 Username: {error}')
                        elif 'email' in field.lower():
                            messages.error(request, f'📧 Email: {error}')
                        else:
                            messages.error(request, f'⚠️ {field}: {error}')
        
        except Exception as e:
            messages.error(request, '❌ Terjadi kesalahan saat membuat akun. Silakan coba lagi.')
    
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    """User logout view"""
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    """Dashboard - posted list dengan detail lengkap dan paging 5 per halaman"""
    
    # Post tweet baru dengan support untuk foto dan GPS coordinates
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            
            # Save GPS coordinates if provided
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            
            if latitude and longitude:
                try:
                    tweet.latitude = Decimal(str(latitude))
                    tweet.longitude = Decimal(str(longitude))
                except (ValueError, TypeError):
                    pass
            
            tweet.save()
            messages.success(request, 'Tweet berhasil dipost!')
            return redirect('dashboard')
    else:
        form = TweetForm()
    
    # Ambil semua tweets dengan urutan terbaru
    tweets = Tweet.objects.all().select_related('user').order_by('-created_at')
    
    # Pagination - 5 post per halaman sesuai kebutuhan
    paginator = Paginator(tweets, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'form': form,
        'page_obj': page_obj,
        'tweet_count': request.user.tweets.count(),
    }
    
    return render(request, 'dashboard.html', context)

@login_required
def map_view(request):
    """Halaman Peta Lokasi menggunakan Leaflet.js"""
    tweet_id = request.GET.get('tweet_id')
    tweet = None
    
    if tweet_id:
        tweet = get_object_or_404(Tweet, id=tweet_id)
    
    context = {
        'tweet': tweet,
    }
    
    return render(request, 'map.html', context)

def api_posts(request):
    """API endpoint untuk berbagi pakai data detail posted (tanggal, waktu, user, pesan, lokasi)"""
    tweets = Tweet.objects.all().select_related('user').order_by('-created_at')
    
    data = []
    for tweet in tweets:
        data.append({
            'id': tweet.id,
            'tanggal': tweet.created_at.strftime('%Y-%m-%d'),
            'waktu': tweet.created_at.strftime('%H:%M:%S'),
            'user': tweet.user.username,
            'pesan': tweet.content,
            'lokasi': tweet.location,
            'latitude': float(tweet.latitude) if tweet.latitude else None,
            'longitude': float(tweet.longitude) if tweet.longitude else None,
            'foto': tweet.image.url if tweet.image else None,
        })
    
    return JsonResponse({
        'status': 'success',
        'data': data,
        'total': len(data),
        'description': 'Data detail posted dari halaman dashboard'
    }, safe=False)

@login_required
def api_view(request):
    """Halaman untuk menampilkan dokumentasi dan interface API"""
    return render(request, 'api_view.html')

@login_required
def profile_view(request, username):
    """User profile view (opsional untuk navigasi)"""
    profile_user = get_object_or_404(User, username=username)
    tweets = profile_user.tweets.all()
    
    # Pagination
    paginator = Paginator(tweets, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'profile_user': profile_user,
        'page_obj': page_obj,
        'tweet_count': tweets.count(),
    }
    
    return render(request, 'profile.html', context)

@login_required
@require_POST
def delete_tweet(request, tweet_id):
    """Delete tweet - hanya pemilik tweet yang bisa menghapus"""
    tweet = get_object_or_404(Tweet, id=tweet_id)
    
    # Pastikan hanya pemilik tweet yang bisa menghapus
    if tweet.user != request.user:
        messages.error(request, 'Anda tidak memiliki izin untuk menghapus tweet ini.')
        return redirect('dashboard')
    
    # Hapus file gambar jika ada
    if tweet.image:
        try:
            tweet.image.delete()
        except:
            pass
    
    tweet.delete()
    messages.success(request, 'Tweet berhasil dihapus!')
    
    # Redirect back to the previous page
    next_page = request.POST.get('next', 'dashboard')
    return redirect(next_page)
