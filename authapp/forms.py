from django import forms

class UserForm(forms.Form):

	username = forms.CharField(max_length=191, required=True)	
	password = forms.CharField(max_length=40, required=True)