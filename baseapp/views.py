from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.generic import View

from authapp.forms import ContactForm
from baseapp.services import send_mail
from baseapp.models import (
	Service,
	Article,
	Pages,
	Goods
)


class IndexView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		context = {
			"page": Pages.objects.filter(title__icontains='Главная').first()
		}
		return render(request, 'baseapp/index.html', context)


class OurToolsView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		context = {
			"page": Pages.objects.filter(title__icontains='Наши инструменты').first()
		}
		return render(request, 'baseapp/our_tools.html', context)


class AboutView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		context = {
			"page": Pages.objects.filter(title__icontains='О нас').first()
		}
		return render(request, 'baseapp/about.html', context)


class WorkWithUsView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		context = {
			"page": Pages.objects.filter(title__icontains='Работа у нас').first()
		}
		return render(request, 'baseapp/work_with_us.html', context)


class Sale1CView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		context = {
			"page": Pages.objects.filter(title__icontains='Купить 1С').first(),
			"goods_list": Goods.objects.all()
		}
		return render(request, 'baseapp/1c_trade.html', context)


class PrivacyView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		context = {
			"page": Pages.objects.filter(title__icontains='Политика конфиденциальности').first(),
			"goods_list": Goods.objects.all()
		}
		return render(request, 'baseapp/privacy.html', context)


class GeneratorView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		context = {
			"page": Pages.objects.filter(title__icontains='Генератор').first(),
			"goods_list": Goods.objects.all()
		}
		return render(request, 'baseapp/generator.html', context)

class ServiceView(View):
	def get(self, request: HttpRequest, id: str) -> HttpResponse:
		context = {
			'service': get_object_or_404(Service, pk=id)
		}
		return render(request, f'baseapp/services/service_{id}.html', context)


class ArticleView(View):
	def get(self, request: HttpRequest, id: str) -> HttpResponse:
		context = {
			'article': get_object_or_404(Article, pk=id)
		}
		return render(request, f'baseapp/articles/article_{id}.html', context)


class ArticleListView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		context = {
			'articles': Article.objects.all()
		}
		return render(request, f'baseapp/articles.html', context)


class SendContactFormView(View):
	def post(self, request: HttpRequest) -> HttpResponse:
		contactForm = ContactForm(request.POST)
		if contactForm.is_valid():
			print(contactForm.cleaned_data)
			try:
				send_mail(contactForm.cleaned_data)
				return redirect('send_form_success')
			except:
				return redirect('send_form_error')		
		else:
			return redirect('send_form_error')


class ContactFormSuccessView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		return render(request, 'baseapp/send_form_success.html')


class ContactFormErrorView(View):
	def get(self, request: HttpRequest) -> HttpResponse:
		return render(request, 'baseapp/send_form_error.html')
