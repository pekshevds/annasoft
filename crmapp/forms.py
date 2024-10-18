from django import forms
from django.forms import ModelForm

from .models import (
	Customer,
	Employee,
	Task,
	Person,
	Position
)

DEFAULT_SEX = 'M'
SEX = (
	(DEFAULT_SEX, 'Мужской'),
	('F', 'Женский'),
	)

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

	employee = forms.ModelChoiceField(queryset=Employee.objects.filter(customer=Customer.objects.filter(is_performer=True).first()),
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


class TaskForm(forms.Form):

	id = forms.IntegerField(widget=forms.HiddenInput(attrs={
		'class': 'form-control',
	}), initial=0)
		
	customer = forms.IntegerField(widget=forms.HiddenInput(attrs={
		'class': 'form-control',
	}), initial=0)

	customer_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Заказчик',
		'readonly': 'readonly',
	}), initial=0)

	from_customer = forms.ModelChoiceField(queryset=Employee.objects.all(),
		 widget=forms.Select(attrs={
		'class': 'form-control',
		'placeholder': 'От заказчика',
	}), required=False)
	
	performer = forms.IntegerField(widget=forms.HiddenInput(attrs={
		'class': 'form-control',
	}), initial=0)

	performer_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Исполнитель',
		'readonly': 'readonly',
	}), initial=0)
	
	from_performer = forms.ModelChoiceField(queryset=Employee.objects.filter(customer=Customer.objects.filter(is_performer=True).first()),
		 widget=forms.Select(attrs={
		'class': 'form-control',
		'placeholder': 'От исполнителя',
	}), required=False)
	
	dead_line = forms.DateField(required=True, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'type': 'date',
		'placeholder': 'Исполнить до',
	}))

	time_scheduled_h = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
		'class': 'form-control',
		'placeholder': 'Время выполнения, факт (час):',
	}), initial=0)

	time_scheduled_m = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
		'class': 'form-control',
		'placeholder': 'Время выполнения, факт (мин.):',
	}), initial=0)

	time_actual_h = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
		'class': 'form-control',
		'placeholder': 'Время выполнения, норма (час)',
	}), initial=0)

	time_actual_m = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
		'class': 'form-control',
		'placeholder': 'Время выполнения, норма (мин.)',
	}), initial=0)

	description = forms.CharField(max_length=1024, required=False, widget=forms.Textarea(attrs={
		'class': 'form-control',
		'rows': '5',
		'placeholder': 'Описание',
	}))

	for_payment = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
		'class': 'custom-control-input',
		'id' : 'for_payment'
	}))

	def __init__(self, *args, **kwargs):

		customer = kwargs.pop('customer', None)
		performer = kwargs.pop('performer', None)

		super(TaskForm, self).__init__(*args, **kwargs)
		
		if customer:
			self.fields['from_customer'].queryset = Employee.objects.filter(customer=customer)
		if performer:
			self.fields['from_performer'].queryset = Employee.objects.filter(customer=performer)


	class Meta:
		model = Task
		fields = [
			'id',
			'customer',
			'from_customer',
			'performer',
			'from_performer',
			'dead_line',
			'time_scheduled_h',
			'time_scheduled_m',
			'time_actual_h',
			'time_actual_m',
			'description',
			]

class CustomerForm(ModelForm):

	id = forms.IntegerField(widget=forms.HiddenInput(attrs={
		'class': 'form-control',
	}), initial=0)

	name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Наименование',
	}))

	full_name = forms.CharField(max_length=1024, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Наименование полное',
	}))

	inn = forms.CharField(max_length=12, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'ИНН',
	}))

	kpp = forms.CharField(max_length=9, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'КПП',
	}))
	
	email = forms.EmailField(max_length=254, required=False, widget=forms.EmailInput(attrs={
		'class': 'form-control',
		'placeholder': 'E-mail',
	}))

	address1 = forms.CharField(max_length=1024, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Адрес',
	}))

	address2 = forms.CharField(max_length=1024, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Адрес',
	}))

	phone1 = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Телефон',
		}))

	phone2 = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Телефон',
	}))

	description = forms.CharField(max_length=1024, required=False, widget=forms.Textarea(attrs={
		'class': 'form-control',
		'rows': '5',
		'placeholder': 'Описание',
	}))

	class Meta:
		model = Customer
		fields = [
			'id',
			'name',
			'full_name',
			'inn',
			'kpp',			
			'email',
			'address1',
			'address2',
			'phone1',
			'phone2',
			'description',
			]

class PersonForm(ModelForm):

	id = forms.IntegerField(widget=forms.HiddenInput(attrs={
		'class': 'form-control',
	}), initial=0)

	first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Имя',
	}))

	middle_name = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Отчество',
	}))

	last_name = forms.CharField(max_length=1024, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Фамилия',
	}))

	birthdate = forms.DateField(required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'type': 'date',
		'placeholder': 'Дата рождения',
	}))

	sex = forms.CharField(max_length=1, widget=forms.Select(choices=SEX, attrs={
		'class': 'form-control',
		'placeholder': 'Пол',
	}), initial=DEFAULT_SEX)

	email = forms.EmailField(max_length=254, required=False, widget=forms.EmailInput(attrs={
		'class': 'form-control',
		'placeholder': 'E-mail',
	}))

	address1 = forms.CharField(max_length=1024, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Адрес',
	}))

	address2 = forms.CharField(max_length=1024, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Адрес',
	}))

	phone1 = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Телефон',
		}))

	phone2 = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Телефон',
	}))

	description = forms.CharField(max_length=1024, required=False, widget=forms.Textarea(attrs={
		'class': 'form-control',
		'rows': '5',
		'placeholder': 'Описание',
	}))

	class Meta:
		model = Person
		fields = [
			'id',
			'first_name',
			'middle_name',
			'last_name',
			'birthdate',
			'sex',
			'email',
			'address1',
			'address2',
			'phone1',
			'phone2',
			'description',
			]


class EmployeeForm(ModelForm):

	id = forms.IntegerField(widget=forms.HiddenInput(attrs={
		'class': 'form-control',
	}), initial=0)

	name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Наименование',
	}))

	customer = forms.ModelChoiceField(queryset=Customer.objects.all(),
		 widget=forms.Select(attrs={
		'class': 'form-control',
		'placeholder': 'Заказчик',
		'readonly': 'readonly',
	}))

	position = forms.ModelChoiceField(queryset=Position.objects.all(),
		 widget=forms.Select(attrs={
		'class': 'form-control',
		'placeholder': 'Должность',
	}))

	person = forms.ModelChoiceField(queryset=Person.objects.all(),
		 widget=forms.Select(attrs={
		'class': 'form-control',
		'placeholder': 'Физ.лицо',
	}))
	
	email = forms.EmailField(max_length=254, required=False, widget=forms.EmailInput(attrs={
		'class': 'form-control',
		'placeholder': 'E-mail',
	}))

	address1 = forms.CharField(max_length=1024, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Адрес',
	}))

	address2 = forms.CharField(max_length=1024, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Адрес',
	}))

	phone1 = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Телефон',
		}))

	phone2 = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Телефон',
	}))

	description = forms.CharField(max_length=1024, required=False, widget=forms.Textarea(attrs={
		'class': 'form-control',
		'rows': '5',
		'placeholder': 'Описание',
	}))

	class Meta:
		model = Employee
		fields = [
			'id',
			'name',
			'email',
			'address1',
			'address2',
			'phone1',
			'phone2',
			'description',
			]
