# fmohapp/portal_views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import PressRelease, Newsletter, DiseaseOutbreak, MediaGallery
from .forms import (
    PressReleaseForm, NewsletterForm, DiseaseOutbreakForm, MediaGalleryForm
)
from django.http import JsonResponse


def staff_check(user):
    return user.is_active and user.is_staff

# ... login, logout, dashboard, press release views already defined ...


def staff_check(user):
    return user.is_active and user.is_staff  # or user.is_superuser

def portal_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and staff_check(user):
            login(request, user)
            return redirect('fmohapp:portal_dashboard')
        else:
            messages.error(request, "Invalid credentials or not authorized.")
    return render(request, 'portal/login.html')

def portal_logout(request):
    logout(request)
    return redirect('fmohapp:portal_login')


@login_required
@user_passes_test(staff_check)
def portal_dashboard(request):
    # A simple dashboard with counts or quick links
    context = {
        'press_count': PressRelease.objects.count(),
        'news_count': Newsletter.objects.count(),
        'outbreak_count': DiseaseOutbreak.objects.count(),
        'media_count': MediaGallery.objects.count(),
    }
    return render(request, 'portal/dashboard.html', context)

@login_required
@user_passes_test(staff_check)
def press_list(request):
    press_releases = PressRelease.objects.all().order_by('-date_published')
    return render(request, 'portal/press_list.html', {'press_releases': press_releases})


@login_required
@user_passes_test(staff_check)
def press_create(request):
    if request.method == 'POST':
        form = PressReleaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Press release created successfully.")
            return redirect('fmohapp:press_list')
    else:
        form = PressReleaseForm()
    return render(request, 'portal/press_form.html', {'form': form, 'title': 'Create Press Release'})

@login_required
@user_passes_test(staff_check)
def press_edit(request, pk):
    press = get_object_or_404(PressRelease, pk=pk)
    if request.method == 'POST':
        form = PressReleaseForm(request.POST, request.FILES, instance=press)
        if form.is_valid():
            form.save()
            messages.success(request, "Press release updated successfully.")
            return redirect('fmohapp:press_list')
    else:
        form = PressReleaseForm(instance=press)
    return render(request, 'portal/press_form.html', {'form': form, 'title': 'Edit Press Release'})

@login_required
@user_passes_test(staff_check)
def press_delete(request, pk):
    press = get_object_or_404(PressRelease, pk=pk)
    if request.method == 'POST':
        press.delete()
        messages.success(request, "Press release deleted successfully.")
        return redirect('fmohapp:press_list')
    return render(request, 'portal/press_confirm_delete.html', {'press': press})


##########################################
# NEWSLETTER VIEWS
##########################################
@login_required
@user_passes_test(staff_check)
def newsletter_list(request):
    items = Newsletter.objects.all().order_by('-date')
    return render(request, 'portal/newsletter_list.html', {'items': items})

@login_required
@user_passes_test(staff_check)
def newsletter_create(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Newsletter created successfully.")
            return redirect('fmohapp:newsletter_list')
    else:
        form = NewsletterForm()
    return render(request, 'portal/newsletter_form.html', {'form': form, 'title': 'Create Newsletter'})

@login_required
@user_passes_test(staff_check)
def newsletter_edit(request, pk):
    item = get_object_or_404(Newsletter, pk=pk)
    if request.method == 'POST':
        form = NewsletterForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Newsletter updated successfully.")
            return redirect('fmohapp:newsletter_list')
    else:
        form = NewsletterForm(instance=item)
    return render(request, 'portal/newsletter_form.html', {'form': form, 'title': 'Edit Newsletter'})

@login_required
@user_passes_test(staff_check)
def newsletter_delete(request, pk):
    item = get_object_or_404(Newsletter, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Newsletter deleted successfully.")
        return redirect('fmohapp:newsletter_list')
    return render(request, 'portal/newsletter_confirm_delete.html', {'item': item})


##########################################
# DISEASE OUTBREAK VIEWS
##########################################
@login_required
@user_passes_test(staff_check)
def outbreak_list(request):
    outbreaks = DiseaseOutbreak.objects.all().order_by('-alert_date')
    return render(request, 'portal/outbreak_list.html', {'outbreaks': outbreaks})

@login_required
@user_passes_test(staff_check)
def outbreak_create(request):
    if request.method == 'POST':
        form = DiseaseOutbreakForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Disease outbreak created successfully.")
            return redirect('fmohapp:outbreak_list')
    else:
        form = DiseaseOutbreakForm()
    return render(request, 'portal/outbreak_form.html', {'form': form, 'title': 'Create Outbreak'})

@login_required
@user_passes_test(staff_check)
def outbreak_edit(request, pk):
    outbreak = get_object_or_404(DiseaseOutbreak, pk=pk)
    if request.method == 'POST':
        form = DiseaseOutbreakForm(request.POST, instance=outbreak)
        if form.is_valid():
            form.save()
            messages.success(request, "Disease outbreak updated successfully.")
            return redirect('fmohapp:outbreak_list')
    else:
        form = DiseaseOutbreakForm(instance=outbreak)
    return render(request, 'portal/outbreak_form.html', {'form': form, 'title': 'Edit Outbreak'})

@login_required
@user_passes_test(staff_check)
def outbreak_delete(request, pk):
    outbreak = get_object_or_404(DiseaseOutbreak, pk=pk)
    if request.method == 'POST':
        outbreak.delete()
        messages.success(request, "Disease outbreak deleted successfully.")
        return redirect('fmohapp:outbreak_list')
    return render(request, 'portal/outbreak_confirm_delete.html', {'outbreak': outbreak})


##########################################
# MEDIA GALLERY VIEWS
##########################################
@login_required
@user_passes_test(staff_check)
def media_list(request):
    media_items = MediaGallery.objects.all().order_by('-uploaded_at')
    return render(request, 'portal/media_list.html', {'media_items': media_items})

@login_required
@user_passes_test(staff_check)
def media_create(request):
    if request.method == 'POST':
        form = MediaGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Media item created successfully.")
            return redirect('fmohapp:media_list')
    else:
        form = MediaGalleryForm()
    return render(request, 'portal/media_form.html', {'form': form, 'title': 'Create Media'})

@login_required
@user_passes_test(staff_check)
def media_edit(request, pk):
    item = get_object_or_404(MediaGallery, pk=pk)
    if request.method == 'POST':
        form = MediaGalleryForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Media item updated successfully.")
            return redirect('fmohapp:media_list')
    else:
        form = MediaGalleryForm(instance=item)
    return render(request, 'portal/media_form.html', {'form': form, 'title': 'Edit Media'})

@login_required
@user_passes_test(staff_check)
def media_delete(request, pk):
    item = get_object_or_404(MediaGallery, pk=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, "Media item deleted successfully.")
        return redirect('fmohapp:media_list')
    return render(request, 'portal/media_confirm_delete.html', {'item': item})

#create an ajax view to get the latest outbreak


from django.http import JsonResponse
import logging
from fmohapp.models import DiseaseOutbreak

logger = logging.getLogger(__name__)

def latest_disease_outbreak_ajax(request):
    """
    AJAX view to retrieve the latest disease outbreak.
    
    Returns:
        JsonResponse: The latest outbreak data in JSON format.
    """
    if request.method == 'GET':
        try:
            latest_outbreak = DiseaseOutbreak.objects.latest('alert_date')
            data = {
                'id': latest_outbreak.id,
                'title': latest_outbreak.title,
                'slug': latest_outbreak.slug,
                'alert_date': latest_outbreak.alert_date.strftime('%Y-%m-%d %H:%M:%S'),
                'description': latest_outbreak.description,
                'severity': latest_outbreak.severity,
                'is_active': latest_outbreak.is_active,
            }
            return JsonResponse(data)
        except DiseaseOutbreak.DoesNotExist:
            return JsonResponse({'error': 'No outbreaks found'}, status=404)
        except Exception as e:
            logger.error(f"Error fetching latest disease outbreak: {e}")
            return JsonResponse({'error': 'An internal error occurred'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
