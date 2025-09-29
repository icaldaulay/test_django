from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Tweet

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('bio', 'location', 'birth_date', 'avatar')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('email', 'bio', 'location')}),
    )

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_preview', 'location', 'created_at')
    list_filter = ('created_at', 'location')
    search_fields = ('content', 'user__username', 'location')
    
    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content'

# Follow model telah dihapus karena tidak diperlukan dalam kebutuhan baru
