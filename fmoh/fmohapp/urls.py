from django.contrib import admin
from django.urls import path
from . import views  # Import all views at once
from .admin_urls import admin_urlpatterns
app_name = 'fmohapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('anti-corruption/', views.anti_corruption, name='anti_corruption'),
    path('base/', views.base, name='base'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('contact/', views.contact, name='contact'),
    # Rename "departments template.html" to "departments_template.html" if possible
    path('departments_template/', views.departments_template, name='departments_template'),
    path('directors/', views.directors, name='directors'),
    path('family_health/', views.family_health, name='family_health'),
    path('foodanddrugs_services/', views.foodanddrugs_services, name='foodanddrugs_services'),
    path('footer/', views.footer, name='footer'),
    path('general_services/', views.general_services, name='general_services'),
    path('header/', views.header, name='header'),
    path('hospital_services/', views.hospital_services, name='hospital_services'),
    path('ict/', views.ict, name='ict'),
    path('legal_services/', views.legal_services, name='legal_services'),
    # If you actually have mainmenu.html
    # path('mainmenu/', views.mainmenu, name='mainmenu'),
    path('port_health/', views.port_health, name='port_health'),
    path('procurement/', views.procurement, name='procurement'),
    path('public_health/', views.public_health, name='public_health'),
    path('reform_coordination/', views.reform_coordination, name='reform_coordination'),
    path('servicom/', views.servicom, name='servicom'),
    path('special_projects/', views.special_projects, name='special_projects'),
    path('the-permanent-secretary/', views.the_permanent_secretary, name='the_permanent_secretary'),
    path('faq/', views.faq, name='faq'),
    path('information/', views.information, name='information'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('cancer_control_program/', views.cancer_control_program, name='cancer_control_program'),
    path('food_and_drugs_programs/', views.food_and_drugs_programs, name='food_and_drugs_programs'),
    path('hospitals/', views.hospitals, name='hospitals'),
    path('specialty-hospitals/', views.specialty_hospitals, name='specialty_hospitals'),
    path('federal_medical_centres/', views.federal_medical_centres, name='federal_medical_centres'),
    path('teaching_hospitals/', views.teaching_hospitals, name='teaching_hospitals'),
    path('hprs_policy_documents/', views.hprs_policy_documents, name='hprs_policy_documents'),
    path('policy_documents/', views.policy_documents, name='policy_documents'),
    path('family_health_policy/', views.family_health_policy, name='family_health_policy'),
    path('public_health_policy/', views.public_health_policy, name='public_health_policy'),
    path('hospital_services_policy/', views.hospital_services_policy, name='hospital_services_policy'),
    path('reports/', views.reports, name='reports'),
    path('publications/', views.publications, name='publications'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('disease-outbreaks/', views.disease_outbreaks, name='disease_outbreaks'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('nchmemos/', views.nchmemos, name='nchmemos'),
    path('press_releases/', views.press_releases, name='press_releases'),
    path('pressrelease1/', views.pressrelease1, name='pressrelease1'),
    path('pressrelease2/', views.pressrelease2, name='pressrelease2'),
    path('pressrelease3/', views.pressrelease3, name='pressrelease3'),
    path('picturegallerry/', views.picturegallery, name='picturegallery'),
    path('videogallerry/', views.videogallery, name='videogallery'),

]
urlpatterns += admin_urlpatterns
