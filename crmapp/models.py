from django.db import models
from django.contrib.auth.models import User

from django import forms
from django.forms import ModelForm

# Create your models here.

DEFAULT_SEX = 'M'
SEX = (
	(DEFAULT_SEX, 'Мужской'),
	('F', 'Женский'),
	)


DEFAULT_TASK_STATUS = 'A'
TASK_STATUS = (
	(DEFAULT_TASK_STATUS, 'Запланирована'),
	('B', 'Выполняется'),
	('C', 'Проверяется'),
	('D', 'Выполнена'),
	)


class Person(models.Model):

	""" Физические лица """
	first_name = models.CharField(max_length=255, verbose_name="Имя")
	middle_name = models.CharField(max_length=255, verbose_name="Отчество", default="", blank=True)
	last_name = models.CharField(max_length=1024, verbose_name="Фамилия", default="", blank=True)
	birthdate = models.DateField(verbose_name="Дата рождения", null=True, blank=True)
	sex = models.CharField(max_length=1, verbose_name="Пол", 
										choices=SEX, default=DEFAULT_SEX)

	email = models.EmailField(max_length=254, verbose_name="Адрес e-mail", default="", blank=True)

	address1 = models.CharField(max_length=1024, verbose_name="Адрес по прописке", default="", blank=True)
	address2 = models.CharField(max_length=1024, verbose_name="Адрес проживания", default="", blank=True)

	phone1 = models.CharField(max_length=25, verbose_name="Телефон", default="", blank=True)
	phone2 = models.CharField(max_length=25, verbose_name="Телефон", default="", blank=True)

	description = models.TextField(verbose_name="Краткая характеристика", default="", blank=True)

	def __str__(self):
		return f'{self.last_name} {self.first_name} {self.middle_name}'

	def get_birthdate(self):
		return f'{self.birthdate.strftime("%Y-%m-%d")}'

	class Meta:
		verbose_name = 'Физическое лицо'
		verbose_name_plural = 'Физические лица'
		ordering = ['last_name']


class PersonForm(ModelForm):

	id = forms.IntegerField(widget=forms.TextInput(attrs={
												'type': 'hidden',
												'class': 'form-control',
												}))
	first_name = forms.CharField(max_length=255)
	middle_name = forms.CharField(max_length=255, required=False)
	last_name = forms.CharField(max_length=1024, required=False)
	birthdate = forms.DateField(required=False)#, attrs={'type': 'date'}
	sex = forms.CharField(max_length=1, widget=forms.Select(choices=SEX))

	email = forms.EmailField(max_length=254, required=False)

	address1 = forms.CharField(max_length=1024, required=False)
	address2 = forms.CharField(max_length=1024, required=False)

	phone1 = forms.CharField(max_length=25, required=False)
	phone2 = forms.CharField(max_length=25, required=False)

	description = forms.CharField(max_length=1024, required=False)

	class Meta:
		model = Person
		fields = [
			'id',
			'first_name',
			'middle_name',
			'birthdate',
			'sex',
			'email',
			'address1',
			'address2',
			'phone1',
			'phone2',
			'description',
			]

		widgets = {
			'description': forms.Textarea(),			
		}


class Customer(models.Model):
	
	""" Заказчики """
	name = models.CharField(max_length=255, verbose_name="Наименование")
	full_name = models.CharField(max_length=1024, verbose_name="Полное наименование", default="", null=True, blank=True)
	
	inn = models.CharField(max_length=12, verbose_name="ИНН", default="", blank=True)
	kpp = models.CharField(max_length=9, verbose_name="КПП", default="", blank=True)

	email = models.EmailField(max_length=254, verbose_name="Адрес e-mail", default="", blank=True)

	address1 = models.CharField(max_length=1024, verbose_name="Адрес юридический", default="", blank=True)
	address2 = models.CharField(max_length=1024, verbose_name="Адрес фактический", default="", blank=True)

	phone1 = models.CharField(max_length=25, verbose_name="Телефон", default="", blank=True)
	phone2 = models.CharField(max_length=25, verbose_name="Телефон", default="", blank=True)

	description = models.TextField(verbose_name="Краткая характеристика", default="", blank=True)

	person = models.ForeignKey(Person, verbose_name="Физическое лицо", on_delete=models.PROTECT, null=True, blank=True)

	is_performer = models.BooleanField(verbose_name="Исполнитель по умолчанию", default=False)

	def __str__(self):
		return f'{self.name}'


	def get_employes(self):
		return Employee.objects.filter(customer=self)


	class Meta:
		verbose_name = 'Заказчик'
		verbose_name_plural = 'Заказчики'
		ordering = ['name']


class Position(models.Model):
	
	""" Должности """	
	name = models.CharField(max_length=1024, verbose_name="Наименование")	

	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name = 'Должность'
		verbose_name_plural = 'Должности'
		ordering = ['name']


class Employee(models.Model):

	""" Сотрудники заказчиков """
	customer = models.ForeignKey(Customer, verbose_name="Заказчик", on_delete=models.PROTECT)

	name = models.CharField(max_length=1024, verbose_name="Наименование")
	position = models.ForeignKey(Position, verbose_name="Должность", on_delete=models.PROTECT, null=True, blank=True)
		
	email = models.EmailField(max_length=254, verbose_name="Адрес e-mail", default="", blank=True)

	address1 = models.CharField(max_length=1024, verbose_name="Адрес юридический", default="", blank=True)
	address2 = models.CharField(max_length=1024, verbose_name="Адрес фактический", default="", blank=True)

	phone1 = models.CharField(max_length=25, verbose_name="Телефон", default="", blank=True)
	phone2 = models.CharField(max_length=25, verbose_name="Телефон", default="", blank=True)

	person = models.ForeignKey(Person, verbose_name="Физическое лицо", on_delete=models.PROTECT, null=True, blank=True)

	user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.PROTECT, null=True, blank=True)

	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name = 'Сотрудник заказчика'
		verbose_name_plural = 'Сотрудники заказчика'
		ordering = ['name']


class Task(models.Model):

	date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
	task_status = models.CharField(max_length=1, verbose_name="Статус", 
										choices=TASK_STATUS, default=DEFAULT_TASK_STATUS)

	customer = models.ForeignKey(Customer, verbose_name="Заказчик", related_name="customer", on_delete=models.PROTECT)
	from_customer = models.ForeignKey(Employee, verbose_name="От заказчика", related_name="from_customer", on_delete=models.PROTECT, null=True)

	performer = models.ForeignKey(Customer, verbose_name="Исполнитель", related_name="performer", on_delete=models.PROTECT)
	from_performer = models.ForeignKey(Employee, verbose_name="От исполнителя", related_name="from_performer", on_delete=models.PROTECT, null=True)

	dead_line = models.DateField(verbose_name="Исполнить до", null=True, blank=True)
	description = models.TextField(verbose_name="Описание", default="", blank=True)

	time_scheduled_h = models.PositiveSmallIntegerField(verbose_name="Время выполнения, факт (час):", default=0, blank=True)
	time_scheduled_m = models.PositiveSmallIntegerField(verbose_name="Время выполнения, факт (мин.):", default=0, blank=True)
	time_actual_h = models.PositiveSmallIntegerField(verbose_name="Время выполнения, норма (час):", default=0, blank=True)
	time_actual_m = models.PositiveSmallIntegerField(verbose_name="Время выполнения, норма (мин.):", default=0, blank=True)

	date_of_completion = models.DateTimeField(verbose_name="Дата исполнения", null=True, blank=True)


	def __str__(self):
		return f'Задача №{self.id} от {self.date.strftime("%d.%m.%Y")}'

	def save(self, *args, **kwargs):
		super(Task, self).save(*args, **kwargs)


	def get_dead_line(self):
		return f'{self.dead_line.strftime("%Y-%m-%d")}'

	def get_dead_line_ru(self):
		return f'{self.dead_line.strftime("%d.%m.%Y")}'

	def get_date_of_completion(self):
		return f'{self.date_of_completion.strftime("%Y-%m-%d")}'

	def get_date_of_completion_ru(self):
		return f'{self.date_of_completion.strftime("%d.%m.%Y")}'


	def is_danger(self):		
		if self.task_status == "D":
			
			if self.date_of_completion.date()>self.dead_line:
				return True
		return False


	def get_time_scheduled(self):
		return self.time_scheduled_h * 60 + self.time_scheduled_m

	def get_time_actual(self):
		return self.time_actual_h * 60 + self.time_actual_m

	def get_profit(self):
		return self.get_time_actual() - self.get_time_scheduled()


	def get_predescription(self):
		if len(self.description) <= 50:
			return self.description
		return self.description[:50] + "..."

	def get_from_customer_list(self):
		return Employee.objects.filter(customer=self.customer)

	def get_from_performer_list(self):
		return Employee.objects.filter(customer=self.performer)

	def is_ready(self):
		if self.task_status == 'B' or self.task_status == 'C':
			return True
		return False


	class Meta:
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'
		ordering = ['dead_line']


class Record(models.Model):#record of status change log

	date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
	task = models.ForeignKey(Task, verbose_name="Задача", related_name="task", on_delete=models.PROTECT)
	task_status = models.CharField(max_length=1, verbose_name="Статус", 
										choices=TASK_STATUS, default=DEFAULT_TASK_STATUS)
	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT, null=True, blank=True)


	class Meta:
		verbose_name = 'Запись'
		verbose_name_plural = 'Журнал изменения статусов'
		ordering = ['date']