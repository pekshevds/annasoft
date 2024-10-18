from django.db import models
from django.contrib.auth.models import User

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
	('E', 'Отменена'),
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
	customer = models.ForeignKey(Customer, verbose_name="Заказчик", on_delete=models.PROTECT, default=None, null=True, blank=True)

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

	def get_fio_person(self):

		from_performer = self.person
		fio = from_performer.last_name + ' ' + from_performer.first_name[0] + '. ' + from_performer.middle_name[0] + '.'
		return fio	
	
	def customer_is_performer(self):
		return self.customer.is_performer

	class Meta:
		verbose_name = 'Сотрудник заказчика'
		verbose_name_plural = 'Сотрудники заказчика'
		ordering = ['name']


class Task(models.Model):

	date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
	task_status = models.CharField(max_length=1, verbose_name="Статус", 
										choices=TASK_STATUS, default=DEFAULT_TASK_STATUS)

	customer = models.ForeignKey(Customer, verbose_name="Заказчик", related_name="customer", on_delete=models.PROTECT, default=None, null=True, blank=True)
	from_customer = models.ForeignKey(Employee, verbose_name="От заказчика", related_name="from_customer", on_delete=models.PROTECT, null=True, blank=True)

	performer = models.ForeignKey(Customer, verbose_name="Исполнитель", related_name="performer", on_delete=models.PROTECT)
	from_performer = models.ForeignKey(Employee, verbose_name="От исполнителя", related_name="from_performer", on_delete=models.PROTECT, null=True, blank=True)

	dead_line = models.DateField(verbose_name="Исполнить до", null=True, blank=True)
	description = models.TextField(verbose_name="Описание", default="", blank=True)

	time_scheduled_h = models.PositiveSmallIntegerField(verbose_name="Время выполнения, факт (час):", default=0, null=True, blank=True)
	time_scheduled_m = models.PositiveSmallIntegerField(verbose_name="Время выполнения, факт (мин.):", default=0, null=True, blank=True)
	time_actual_h = models.PositiveSmallIntegerField(verbose_name="Время выполнения, норма (час):", default=0, null=True, blank=True)
	time_actual_m = models.PositiveSmallIntegerField(verbose_name="Время выполнения, норма (мин.):", default=0, null=True, blank=True)

	date_of_completion = models.DateTimeField(verbose_name="Дата исполнения", null=True, blank=True)

	for_payment = models.BooleanField(verbose_name="Оплачивается", default=False)




	def __str__(self):

		if self.date:
			return f'{self.id} от {self.date.strftime("%d.%m.%Y")}'
		return f'Задача № от '

	def save(self, *args, **kwargs):
		
		if self.time_scheduled_h is None:
			self.time_scheduled_h = 0

		if self.time_scheduled_m is None:
			self.time_scheduled_m = 0

		if self.time_actual_h is None:
			self.time_actual_h = 0

		if self.time_actual_m is None:
			self.time_actual_m = 0
		
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

	def get_time_scheduled_h(self):
		return self.time_scheduled_h + round(self.time_scheduled_m/60, 1)

	def get_time_actual(self):
		return self.time_actual_h * 60 + self.time_actual_m

	def get_time_actual_h(self):
		return self.time_actual_h + round(self.time_actual_m/60, 1)

	def get_profit(self):
		return round(self.get_time_actual_h() - self.get_time_scheduled_h(), 1)


	def get_predescription(self):
		if len(self.description) <= 80:
			return self.description
		return self.description[:80] + "..."

	def get_from_customer_list(self):
		return Employee.objects.filter(customer=self.customer)

	def get_from_performer_list(self):
		return Employee.objects.filter(customer=self.performer)

	def is_ready(self):
		if self.task_status == 'B' or self.task_status == 'C':
			return True
		return False

	def get_fio_from_performer(self):

		from_performer = Employee.objects.filter(id=self.from_performer.id).first().person
		fio = from_performer.last_name + ' ' + from_performer.first_name[0] + '. ' + from_performer.middle_name[0] + '.'

		return fio



	class Meta:
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'
		ordering = ['dead_line']


class Record(models.Model):#record of status change log

	date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
	task = models.ForeignKey(Task, verbose_name="Задача", related_name="task", on_delete=models.CASCADE)
	task_status = models.CharField(max_length=1, verbose_name="Статус", 
										choices=TASK_STATUS, default=DEFAULT_TASK_STATUS)
	user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT, null=True, blank=True)


	class Meta:
		verbose_name = 'Запись'
		verbose_name_plural = 'Журнал изменения статусов'
		ordering = ['date']