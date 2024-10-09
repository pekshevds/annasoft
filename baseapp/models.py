from django.db import models

# Create your models here.

def get_image_name(instance, filename):
    new_name = ('%s' + '.' + filename.split('.')[-1]) % str(instance.id)
    return new_name


class Category(models.Model):
	name = models.CharField(max_length=150, verbose_name="Наименование", null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class Service(models.Model):
	title = models.CharField(max_length=150, verbose_name="Заголовок", null=True)
	pre_content = models.CharField(max_length=255, verbose_name="Краткое содержание", null=True)
	picture = models.ImageField(upload_to=get_image_name, verbose_name='Изображение 900х550', default=None, null=True, blank=True)

	meta_title 			= models.CharField(max_length=150, verbose_name='meta title', blank=True, null=True)
	meta_description 	= models.TextField(max_length=1024, verbose_name='meta description', blank=True, null=True)
	meta_keywords 		= models.TextField(max_length=1024, verbose_name='meta keywords', blank=True, null=True)

		
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуги'


class Article(models.Model):
	category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.PROTECT, blank=True, null=True)
	title = models.CharField(max_length=150, verbose_name="Заголовок", null=True)
	date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
	picture = models.ImageField(upload_to=get_image_name, verbose_name='Изображение 900х537', default=None, null=True, blank=True)
		
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'


class Pages(models.Model):

	title 				= models.CharField(max_length=150, verbose_name="Заголовок", null=True)
	meta_title 			= models.CharField(max_length=150, verbose_name='meta title', blank=True, null=True)
	meta_description 	= models.TextField(max_length=1024, verbose_name='meta description', blank=True, null=True)
	meta_keywords 		= models.TextField(max_length=1024, verbose_name='meta keywords', blank=True, null=True)
		
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'SEO'
		verbose_name_plural = 'SEO'


# Контакты компании
class CompanyContactData(models.Model):

	address = models.CharField(max_length=150, verbose_name="Адрес организации", help_text="Адрес указывается без города")
	mobile_phone = models.CharField(max_length=150, verbose_name="Мобильный телефон", help_text="Указывайте телефон начиная с 7")
	phone = models.CharField(max_length=150, verbose_name="Телефон", help_text="Указывайте телефон начиная с 7")
	working_rules = models.CharField(max_length=150, verbose_name="Режим работы", help_text="Пон-Пят: 9:00 - 18:00")
	telegram_name = models.CharField(max_length=150, verbose_name="Имя пользователя телеграм")
	email = models.CharField(max_length=150, verbose_name="Email")

	def __str__(self):
		return self.address
	
	def save(self, **kwargs):
		super().save(**kwargs)
		if len(CompanyContactData.objects.all()) > 1:
			CompanyContactData.objects.all().last().delete()
			
	class Meta:
		verbose_name = 'Контактные данные организации'
		verbose_name_plural = 'Контактные данные организации'

# Товары
class Goods(models.Model):

	title = models.CharField(max_length=150, verbose_name="Наименование")
	description = models.TextField(max_length=1024, verbose_name='Описание товара')
	price_base = models.IntegerField(verbose_name='Цена базовой версии', blank=True, null=True)
	price = models.IntegerField(verbose_name='Цена версии Проф')
	image = models.ImageField(upload_to=get_image_name, verbose_name='Изображение 900х550')

	def __str__(self) -> str:
		return self.title
	
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'