from django.db import models

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
	middle_name = models.CharField(max_length=255, verbose_name="Отчество", default="", null=True, blank=True)
	last_name = models.CharField(max_length=1024, verbose_name="Фамилия", default="", null=True, blank=True)
	birthdate = models.DateField(verbose_name="Дата рождения", null=True, blank=True)
	sex = models.CharField(max_length=1, verbose_name="Пол", 
										choices=SEX, default=DEFAULT_SEX)

	email = models.EmailField(max_length=254, verbose_name="Адрес e-mail", default="", null=True, blank=True)

	address1 = models.CharField(max_length=1024, verbose_name="Адрес по прописке", default="", null=True, blank=True)
	address2 = models.CharField(max_length=1024, verbose_name="Адрес проживания", default="", null=True, blank=True)

	phone1 = models.CharField(max_length=25, verbose_name="Телефон", default="", null=True, blank=True)
	phone2 = models.CharField(max_length=25, verbose_name="Телефон", default="", null=True, blank=True)

	description = models.TextField(verbose_name="Краткая характеристика", default="", null=True, blank=True)


	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	class Meta:        
		verbose_name = 'Физическое лицо'
		verbose_name_plural = 'Физические лица'


class Customer(models.Model):
	
	""" Заказчики """
	name = models.CharField(max_length=255, verbose_name="Наименование")
	full_name = models.CharField(max_length=1024, verbose_name="Полное наименование", default="", null=True, blank=True)
	
	inn = models.CharField(max_length=12, verbose_name="ИНН", default="", null=True, blank=True)
	kpp = models.CharField(max_length=9, verbose_name="КПП", default="", null=True, blank=True)

	email = models.EmailField(max_length=254, verbose_name="Адрес e-mail", default="", null=True, blank=True)

	address1 = models.CharField(max_length=1024, verbose_name="Адрес юридический", default="", null=True, blank=True)
	address2 = models.CharField(max_length=1024, verbose_name="Адрес фактический", default="", null=True, blank=True)

	phone1 = models.CharField(max_length=25, verbose_name="Телефон", default="", null=True, blank=True)
	phone2 = models.CharField(max_length=25, verbose_name="Телефон", default="", null=True, blank=True)

	description = models.TextField(verbose_name="Краткая характеристика", default="", null=True, blank=True)

	person = models.ForeignKey(Person, verbose_name="Физическое лицо", on_delete=models.PROTECT, null=True, blank=True)

	def __str__(self):
		return f'{self.name}'

	class Meta:        
		verbose_name = 'Заказчик'
		verbose_name_plural = 'Заказчики'


class Position(models.Model):
	
	""" Должности """	
	name = models.CharField(max_length=1024, verbose_name="Наименование")	

	def __str__(self):
		return f'{self.name}'

	class Meta:        
		verbose_name = 'Должность'
		verbose_name_plural = 'Должности'


class Employee(models.Model):

	""" Сотрудники заказчиков """
	customer = models.ForeignKey(Customer, verbose_name="Заказчик", on_delete=models.PROTECT)

	name = models.CharField(max_length=1024, verbose_name="Наименование")
	position = models.ForeignKey(Position, verbose_name="Должность", on_delete=models.PROTECT, null=True, blank=True)
		
	email = models.EmailField(max_length=254, verbose_name="Адрес e-mail", default="", null=True, blank=True)

	address1 = models.CharField(max_length=1024, verbose_name="Адрес юридический", default="", null=True, blank=True)
	address2 = models.CharField(max_length=1024, verbose_name="Адрес фактический", default="", null=True, blank=True)

	phone1 = models.CharField(max_length=25, verbose_name="Телефон", default="", null=True, blank=True)
	phone2 = models.CharField(max_length=25, verbose_name="Телефон", default="", null=True, blank=True)

	person = models.ForeignKey(Person, verbose_name="Физическое лицо", on_delete=models.PROTECT, null=True, blank=True)

	def __str__(self):
		return f'{self.name}'

	class Meta:        
		verbose_name = 'Сотрудник заказчика'
		verbose_name_plural = 'Сотрудники заказчика'


class Task(models.Model):

	date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
	task_status = models.CharField(max_length=1, verbose_name="Статус", 
										choices=TASK_STATUS, default=DEFAULT_TASK_STATUS)

	customer = models.ForeignKey(Customer, verbose_name="Заказчик", related_name="customer", on_delete=models.PROTECT)
	from_customer = models.ForeignKey(Employee, verbose_name="От заказчика", related_name="from_customer", on_delete=models.PROTECT)

	performer = models.ForeignKey(Customer, verbose_name="Исполнитель", related_name="performer", on_delete=models.PROTECT)
	from_performer = models.ForeignKey(Employee, verbose_name="От исполнителя", related_name="from_performer", on_delete=models.PROTECT)

	dead_line = models.DateField(verbose_name="Исполнить до", null=True, blank=True)
	description = models.TextField(verbose_name="Описание", null=True, blank=True)

	def __str__(self):
		return f'Задача №{self.id} от {self.date.strftime("%d.%m.%Y")}'

	def get_from_customer_list(self):
		return Employee.objects.filter(customer=self.customer)

	def get_from_performer_list(self):
		return Employee.objects.filter(customer=self.performer)

	class Meta:        
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'