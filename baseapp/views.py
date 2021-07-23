from django.shortcuts import render
from .models import Service
from .models import Article
from .core import get_context
from authapp.forms import ContactForm

def show_index(request):
	return render(request, 'baseapp/index.html', get_context())


def show_our_tools(request):
	return render(request, 'baseapp/our_tools.html', get_context())


def show_about(request):
	return render(request, 'baseapp/about.html', get_context())


def show_article(request, id):

	context = get_context()
	context['article'] = Article.objects.get(id=id)
	return render(request, f'baseapp/articles/article_{id}.html', context)


def show_articles(request):
	context = get_context()
	context['articles'] = Article.objects.all()
	return render(request, 'baseapp/articles.html', context)


def show_service(request, id):

	context = get_context()
	context['service'] = Service.objects.get(id=id)
	return render(request, f'baseapp/services/service_{id}.html', context)


def show_services(request):
	return render(request, 'baseapp/services.html', get_context())

def show_e_commerce_and_1c(request):
	return render(request, 'baseapp/e_commerce_and_1c.html', get_context())


def show_work_with_us(request):
	return render(request, 'baseapp/work_with_us.html', get_context())

def send_contact_form(request):

	if request.user.is_authenticated:

		if request.method == 'POST':

			contactForm = ContactForm(request.POST)

			if contactForm.is_valid():

				first_name = contactForm.cleaned_data['firstName']
				lastName = contactForm.cleaned_data['lastName']
				Email = contactForm.cleaned_data['Email']
				phone = contactForm.cleaned_data['phone']
				comment = contactForm.cleaned_data['comment']
				accessData = contactForm.cleaned_data['accessData']

				