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