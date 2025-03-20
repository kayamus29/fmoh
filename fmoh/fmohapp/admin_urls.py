from django.contrib import admin
from django.urls import path
from . import portal_views
admin_urlpatterns = [
path('portal/login/', portal_views.portal_login, name='portal_login'),
    path('portal/logout/', portal_views.portal_logout, name='portal_logout'),
    path('portal/dashboard/', portal_views.portal_dashboard, name='portal_dashboard'),

    # Press Release
    path('portal/press/', portal_views.press_list, name='press_list'),
    path('portal/press/create/', portal_views.press_create, name='press_create'),
    path('portal/press/edit/<int:pk>/', portal_views.press_edit, name='press_edit'),
    path('portal/press/delete/<int:pk>/', portal_views.press_delete, name='press_delete'),

    # ------------------------------
    # NEWSLETTER
    # ------------------------------
    path('portal/newsletter/', portal_views.newsletter_list, name='newsletter_list'),
    path('portal/newsletter/create/', portal_views.newsletter_create, name='newsletter_create'),
    path('portal/newsletter/edit/<int:pk>/', portal_views.newsletter_edit, name='newsletter_edit'),
    path('portal/newsletter/delete/<int:pk>/', portal_views.newsletter_delete, name='newsletter_delete'),

    # ------------------------------
    # DISEASE OUTBREAK
    # ------------------------------
    path('portal/outbreaks/', portal_views.outbreak_list, name='outbreak_list'),
    path('portal/outbreaks/create/', portal_views.outbreak_create, name='outbreak_create'),
    path('portal/outbreaks/edit/<int:pk>/', portal_views.outbreak_edit, name='outbreak_edit'),
    path('portal/outbreaks/delete/<int:pk>/', portal_views.outbreak_delete, name='outbreak_delete'),

    # ------------------------------
    # MEDIA GALLERY
    # ------------------------------
    path('portal/media/', portal_views.media_list, name='media_list'),
    path('portal/media/create/', portal_views.media_create, name='media_create'),
    path('portal/media/edit/<int:pk>/', portal_views.media_edit, name='media_edit'),
    path('portal/media/delete/<int:pk>/', portal_views.media_delete, name='media_delete'),
    path('latest-disease-outbreak-ajax/',portal_views.latest_disease_outbreak_ajax ,name='latest_disease_outbreak_ajax')
] 

