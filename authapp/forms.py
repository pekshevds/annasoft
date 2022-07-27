from django import forms
from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox
from captcha.widgets import ReCaptchaV2Invisible
# from captcha.fields import CaptchaField
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox

class UserForm(forms.Form):

	username = forms.CharField(max_length=191, required=True)	
	password = forms.CharField(max_length=40, required=True)


class ContactForm(forms.Form):
	
	firstName = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Имя *',
			'id': 'exampleInputName',

		}))
	phone = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Телефон *',
			'id': 'exampleInputPhone',
			'onKeyPress': 'inputFilter()',
		}))
	comment = forms.CharField(max_length=2048, required=False, widget=forms.Textarea(attrs={
			'class': 'form-control',
			'placeholder': 'Укажите тему обращения *',
			'id': 'exampleInputEnquiry-Description',
		}))
	accessData = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
			'class': 'custom-control-input',
			'id': 'customCheck1',
		}))
	# captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
