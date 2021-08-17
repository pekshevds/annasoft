from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
# from captcha.fields import CaptchaField
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox

class UserForm(forms.Form):

	username = forms.CharField(max_length=191, required=True)	
	password = forms.CharField(max_length=40, required=True)


class ContactForm(forms.Form):
	
	firstName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Имя',
			'id': 'exampleInputName',

		}))
	lastName = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Фамилия',
			'id': 'exampleInputLname',
		}))
	Email = forms.EmailField(max_length=30, widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'email',
			'id': 'exampleInputEmail',
		}))
	phone = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Телефон',
			'id': 'exampleInputPhone',
		}))
	comment = forms.CharField(max_length=2048, required=False, widget=forms.Textarea(attrs={
			'class': 'form-control',
			'placeholder': 'Комментарий',
			'id': 'exampleInputEnquiry-Description',
		}))
	accessData = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
			'class': 'custom-control-input',
			'id': 'customCheck1',
			'rows': '5',
		}))
	# captcha = CaptchaField(label='Введите данные с картинки')
	# captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
	captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
