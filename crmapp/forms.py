from django import forms
from .models import Customer

class show_report_001_Form(forms.Form):

	customer = forms.ModelChoiceField(queryset=Customer.objects.all(),
		 widget=forms.Select(attrs={
		'class': 'form-control',
		'placeholder': 'Заказчик',
	}), required=False)
	
	param_from = forms.DateField(required=True, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'type': 'date',
		'placeholder': 'Период с',
	}))

	param_to = forms.DateField(required=True, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'type': 'date',
		'placeholder': 'по',
	}))