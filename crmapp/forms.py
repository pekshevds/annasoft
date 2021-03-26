from django import forms
from .models import Customer
from .models import Employee

from .core import get_default_performer

class report_001_Form(forms.Form):

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



class report_002_Form(report_001_Form):
	def __init__(self, *args, **kwargs):
		super(report_002_Form, self).__init__(*args, **kwargs)


class report_003_Form(forms.Form):

	employee = forms.ModelChoiceField(queryset=Employee.objects.filter(customer=get_default_performer()),
		 widget=forms.Select(attrs={
		'class': 'form-control',
		'placeholder': 'Исполнитель',
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