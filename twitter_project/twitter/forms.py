from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Tweet

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    """Custom User Registration Form"""
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class TweetForm(forms.ModelForm):
    """Form untuk membuat tweet dengan lokasi dan foto"""
    
    class Meta:
        model = Tweet
        fields = ['content', 'location', 'latitude', 'longitude', 'image']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Apa yang sedang terjadi? (maks 140 karakter)",
                'rows': 3,
                'maxlength': 140
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cari lokasi (min 3 karakter)',
                'required': True,
                'autocomplete': 'off'
            }),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = 'Pesan'
        self.fields['location'].label = 'Lokasi'
        self.fields['image'].label = 'Foto (opsional)'
        self.fields['latitude'].required = False
        self.fields['longitude'].required = False
        self.fields['image'].required = False
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > 140:
            raise forms.ValidationError("Pesan tidak boleh lebih dari 140 karakter.")
        return content
    
    def clean_location(self):
        location = self.cleaned_data.get('location')
        if not location:
            raise forms.ValidationError("Lokasi wajib diisi.")
        return location