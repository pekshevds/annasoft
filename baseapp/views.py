from django.shortcuts import render
from .models import Service
from .models import Article
from .core import get_context
from authapp.forms import ContactForm

from decouple import config

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

	context = get_context()

	if request.method == 'POST':

		contactForm = ContactForm(request.POST)

		if contactForm.is_valid():

			first_name = contactForm.cleaned_data['firstName']
			lastName = contactForm.cleaned_data['lastName']
			Email = contactForm.cleaned_data['Email']
			phone = contactForm.cleaned_data['phone']
			comment = contactForm.cleaned_data['comment']
			accessData = contactForm.cleaned_data['accessData']

			send_mail(first_name, lastName, Email, phone, comment, accessData)

			return render(request, 'baseapp/send_form_success.html', context)


def trade_1c(request):
	return render(request, 'baseapp/1c_trade.html', get_context())

def show_privacy(request):
	return render(request, 'baseapp/privacy.html', get_context())




def send_mail(first_name, lastName, Email, phone, comment, accessData):

	HOST = "mail.hosting.reg.ru"
	sender_email = config('MAIL_USER')
	receiver_email = ['info@annasoft.ru', 'm.dyshlik@annasoft.ru']
	password = config('MAIL_PASSWORD')

	message = MIMEMultipart("alternative")
	message["Subject"] = "Свяжитесь с {} {}. Контакты: {} {} ".format(first_name, lastName, phone, Email) 
	message["From"] = sender_email
	message["To"] = ','.join(receiver_email)

	text_body = """\
	"""

	html = """\
	<html>
      <body>
        <H3>Свяжитесь с {0} {1}. Контакты: {2} {3}</H3>
        <H3>Контакты:</H3>
        <p>Телефон: {2}</p>
        <p>Email: {3}</p>
        <p></p>
        <p>Комментарий:</p>
        <p>{4}</p>
      </body>
    </html>
	""".format(first_name, lastName, phone, Email, comment)

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
