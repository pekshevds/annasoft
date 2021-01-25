from django.shortcuts import render
from .models import Service
from .models import Article
from .core import get_context

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
