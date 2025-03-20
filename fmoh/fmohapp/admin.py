from django.contrib import admin
from .models import PressRelease, Newsletter, DiseaseOutbreak, MediaGallery,PublicFeedback


@admin.register(PublicFeedback)
class PublicFeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'submitted_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    ordering = ('-submitted_at',)


@admin.register(PressRelease)
class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'status')
    list_filter = ('status', 'date_published')
    search_fields = ('title', 'author', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date_published'
    ordering = ('-date_published',)

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'
    ordering = ('-date',)

@admin.register(DiseaseOutbreak)
class DiseaseOutbreakAdmin(admin.ModelAdmin):
    list_display = ('title', 'alert_date', 'severity', 'is_active')
    list_filter = ('severity', 'alert_date', 'is_active')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'alert_date'
    ordering = ('-alert_date',)

@admin.register(MediaGallery)
class MediaGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'uploaded_at')
    list_filter = ('media_type', 'uploaded_at')
    search_fields = ('title', 'description')
    ordering = ('-uploaded_at',)