from django import forms

class UserForm(forms.Form):

	username = forms.CharField(max_length=191, required=True)	
	password = forms.CharField(max_length=40, required=True)


class ContactForm(forms.Form):
	
	firstName = forms.CharField(max_length=30)
	lastName = forms.CharField(max_length=30, required=False)
	Email = forms.EmailField(max_length=30)
	phone = forms.CharField(max_length=30, required=False)
	comment = forms.CharField(max_length=2048, required=False)
	accessData = forms.BooleanField(required=False)
