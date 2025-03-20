from django import forms
from .models import PublicFeedback
# fmohapp/forms.py
from django import forms
from .models import PressRelease, Newsletter, DiseaseOutbreak, MediaGallery

class PublicFeedbackForm(forms.ModelForm):
    class Meta:
        model = PublicFeedback
        fields = ['name', 'email', 'phone_number', 'message']



class PressReleaseForm(forms.ModelForm):
    class Meta:
        model = PressRelease
        fields = ['title', 'author', 'featured_image', 'content', 'status']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['title', 'date', 'content', 'file']

class DiseaseOutbreakForm(forms.ModelForm):
    class Meta:
        model = DiseaseOutbreak
        fields = ['title', 'description', 'severity', 'is_active']

class MediaGalleryForm(forms.ModelForm):
    class Meta:
        model = MediaGallery
        fields = ['title', 'description', 'media_type', 'image_file', 'video_url']
