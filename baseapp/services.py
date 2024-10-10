import smtplib, ssl

from decouple import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from authapp.forms import ContactForm
from baseapp.models import MailingRecipients

def send_mail(contact_data: ContactForm):
	HOST = "smtp.mail.ru"
	sender_email = config('MAIL_USER')
	receiver_email = list(MailingRecipients.objects.values_list('email', flat=True))
	if len(receiver_email) > 0:
		password = config('MAIL_PASSWORD')
		message = MIMEMultipart("alternative")
		message["Subject"] = "Свяжитесь с {}. Контакты: {} ".format(contact_data.get('firstName'), contact_data.get('phone')) 
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
        """.format(contact_data.get('firstName'), contact_data.get('phone'), contact_data.get('comment'))
		part1 = MIMEText(text_body, "plain")
		part2 = MIMEText(html, "html")
		message.attach(part1)
		message.attach(part2)
		ssl.create_default_context()
		server = smtplib.SMTP(HOST, 587)
		server.starttls()
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email , message.as_string())
		server.quit()