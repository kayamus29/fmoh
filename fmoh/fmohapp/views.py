from django.shortcuts import render
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from .forms import PublicFeedbackForm
from .models import DiseaseOutbreak

# Existing views remain unchanged...

def feedback_view(request):
    if request.method == 'POST':
        form = PublicFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to a thank-you page
    else:
        form = PublicFeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def disease_outbreaks(request):
    alerts = DiseaseOutbreak.objects.filter(is_active=True).order_by('-date_reported')
    return render(request, 'disease_outbreaks.html', {'alerts': alerts})

def thank_you(request):
    return render(request, 'thank_you.html', {'message': _('Thank you for your feedback!')})
# 404.html is typically handled as a special error handler in Django.
# If you want a direct view function for demonstration, you can do:


def anti_corruption(request):
    return render(request, 'anti_corruption.html')

def base(request):
    return render(request, 'base.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def contact(request):
    return render(request, 'contact.html')

# "departments template.html" has a space in the filename.
# If possible, consider renaming it to something like "departments_template.html".
def departments_template(request):
    return render(request, 'departments_template.html')

def directors(request):
    return render(request, 'directors.html')

def family_health(request):
    return render(request, 'family_health.html')

def foodanddrugs_services(request):
    return render(request, 'foodanddrugs_services.html')

def footer(request):
    return render(request, 'footer.html')

def general_services(request):
    return render(request, 'general_services.html')

def header(request):
    return render(request, 'header.html')

def hospital_services(request):
    return render(request, 'hospital_services.html')

def ict(request):
    return render(request, 'ict.html')

def index(request):
    return render(request, 'index.html')

def legal_services(request):
    return render(request, 'legal_services.html')

# If you have a 'mainmenu.html' file:
def mainmenu(request):
    return render(request, 'mainmenu.html')

def port_health(request):
    return render(request, 'port_health.html')

def procurement(request):
    return render(request, 'procurement.html')

def public_health(request):
    return render(request, 'public_health.html')

def reform_coordination(request):
    return render(request, 'reform_coordination.html')

def servicom(request):
    return render(request, 'servicom.html')

def special_projects(request):
    return render(request, 'special_projects.html')

def the_permanent_secretary(request):
    return render(request, 'the-permanent-secretary.html')

def information(request):
    return render(request, 'information.html')

def faq(request):
    return render(request, 'information.html')

def nutrition(request):
    return render(request, 'nutrition.html')

def cancer_control_program(request):
    return render(request, 'cancer_control_program.html')

def food_and_drugs_programs(request):
    return render(request, 'food_and_drugs_programs.html')

def hospitals(request):
    return render(request, 'hospitals.html')

def specialty_hospitals(request):
    return render(request, 'specialty_hospitals.html')

def federal_medical_centres(request):
    return render(request, 'federal_medical_centres.html')

def teaching_hospitals(request):
    return render(request, 'teaching_hospitals.html')

def hprs_policy_documents(request):
    return render(request, 'hprs_policy_documents.html')

def policy_documents(request):
    return render(request, 'policy_documents.html')

def family_health_policy(request):
    return render(request, 'family_health_policy.html')

def public_health_policy(request):
    return render(request, 'public_health_policy.html')

def hospital_services_policy(request):
    return render(request, 'hospital_services_policy.html')

def reports(request):
    return render(request, 'reports.html')

def publications(request):
    return render(request, 'publications.html')

def newsletter(request):
    return render(request, 'newsletter.html')
def nchmemos(request):
    return render(request, 'nchmemos.html')

def press_releases(request):
    return render(request, 'press_releases.html')

def pressrelease1(request):
    return render(request, 'pressrelease1.html')

def pressrelease2(request):
    return render(request, 'pressrelease2.html')

def pressrelease3(request):
    return render(request, 'pressrelease3.html')

def picturegallery(request):
    return render(request, 'picturegallery.html')

def videogallery(request):
    return render(request, 'videogallery.html')