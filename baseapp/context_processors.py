import datetime

from authapp.forms import ContactForm
from baseapp.models import Service, Article, CompanyContactData

def actual_year(request):
    return {'actual_year': datetime.datetime.now().strftime("%Y")}

def contact_form(request):
    return {'contact_form': ContactForm()}

def services(request):
    return {'services': Service.objects.all()[:6]}

def articles(request):
    return {'articles': Article.objects.all()[:3]}

def company_contact_data(request):
    return {'company_contact_data': CompanyContactData.objects.all().first()}