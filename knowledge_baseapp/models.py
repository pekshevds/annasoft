from django.db import models
from crmapp.models import Customer
from simple_history.models import HistoricalRecords


class Section(models.Model):

	title = models.CharField(max_length=255, verbose_name="Заголовок")
	history = HistoricalRecords()

	def get_records(self):
		return Record.objects.filter(section=self)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Раздел'
		verbose_name_plural = 'Разделы'


class Record(models.Model):

	title = models.CharField(max_length=255, verbose_name="Заголовок")
	description = models.TextField(verbose_name="Описание", default="", blank=True)
	customer = models.ForeignKey(Customer, verbose_name="Заказчик", on_delete=models.PROTECT, blank=True)
	section = models.ForeignKey(Section, verbose_name="Раздел", on_delete=models.PROTECT, blank=True)
	history = HistoricalRecords()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Запись'
		verbose_name_plural = 'Записи'