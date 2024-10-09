from django.shortcuts import render, redirect
import smtplib, ssl

from decouple import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from .models import Service
from .models import Article
from .models import Pages, Goods
from authapp.forms import ContactForm


def show_index(request):
	context = {}
	try:
			context['page'] = Pages.objects.get(title__icontains='Главная')
	except:
			context['page'] = None
	return render(request, 'baseapp/e_commerce_and_1c.html', context)


def show_our_tools(request):
	context = {}
	try:
			context['page'] = Pages.objects.get(title__icontains='Наши инструменты')
	except:
			context['page'] = None
	return render(request, 'baseapp/our_tools.html', context)


def show_about(request):
	context = {}	
	try:
			context['page'] = Pages.objects.get(title__icontains='О нас')
	except:
			context['page'] = None
	return render(request, 'baseapp/index.html', context)


def show_article(request, id):
	context = {}
	context['article'] = Article.objects.get(id=id)
	return render(request, f'baseapp/articles/article_{id}.html', context)


def show_articles(request):
	context = {}
	context['articles'] = Article.objects.all()
	return render(request, 'baseapp/articles.html', context)


def show_service(request, id):
	context = {}
	context['service'] = Service.objects.get(id=id)
	return render(request, f'baseapp/services/service_{id}.html', context)


def show_work_with_us(request):
	context = {}
	try:
			context['page'] = Pages.objects.get(title__icontains='Работа у нас')
	except:
			context['page'] = None
	return render(request, 'baseapp/work_with_us.html', context)

def send_contact_form(request):
	if request.method == 'POST':
		contactForm = ContactForm(request.POST)
		if contactForm.is_valid():
			first_name = contactForm.cleaned_data['firstName']
			phone = contactForm.cleaned_data['phone']
			comment = contactForm.cleaned_data['comment']
			accessData = contactForm.cleaned_data['accessData']
			send_mail(first_name, phone, comment, accessData)
			return redirect('send_form_success')
		else:
			return redirect('send_form_error')

def send_form_success(request):
	return render(request, 'baseapp/send_form_success.html')

def send_form_error(request):
	return render(request, 'baseapp/send_form_error.html')

def trade_1c(request):
	context = {
		"goods_list": Goods.objects.all()
	}
	try:
			context['page'] = Pages.objects.get(title__icontains='Купить 1С')
	except:
			context['page'] = None
	return render(request, 'baseapp/1c_trade.html', context)

def show_privacy(request):
	context = {}
	try:
			context['page'] = Pages.objects.get(title__icontains='Политика конфиденциальности')
	except:
			context['page'] = None
	return render(request, 'baseapp/privacy.html', context)


def show_generator_page(request):
	context = {}
	try:
			context['page'] = Pages.objects.get(title__icontains='Генератор')
	except:
			context['page'] = None
	return render(request, 'baseapp/generator.html', context)


def send_mail(first_name, phone, comment, accessData):
	HOST = "smtp.mail.ru"
	sender_email = config('MAIL_USER')
	receiver_email = ['info@annasoft.ru', 'm.dyshlik@annasoft.ru']
	password = config('MAIL_PASSWORD')
	message = MIMEMultipart("alternative")
	message["Subject"] = "Свяжитесь с {}. Контакты: {} ".format(first_name, phone) 
	message["From"] = sender_email
	message["To"] = ','.join(receiver_email)
	text_body = """\
	"""
	html = """\
	<html>
      <body>
        <H3>Свяжитесь с {0}. Контакты: {1}</H3>
        <H3>Контакты:</H3>
        <p>Телефон: {1}</p>
        <p></p>
        <p>Комментарий:</p>
        <p>{2}</p>
      </body>
    </html>
	""".format(first_name, phone, comment)
	part1 = MIMEText(text_body, "plain")
	part2 = MIMEText(html, "html")
	message.attach(part1)
	message.attach(part2)
	context = ssl.create_default_context()
	server = smtplib.SMTP(HOST, 587)
	server.starttls()
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email , message.as_string())
	server.quit()
