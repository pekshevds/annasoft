from django.db import models
from crmapp.models import Customer
import uuid

def get_uuid4():
    return str(uuid.uuid4())

class Point_of_sale(models.Model):

    uid = models.SlugField(max_length=36, verbose_name='Идентификатор', unique=True, null=True, blank=True)
    customer = models.ForeignKey(Customer, verbose_name="Заказчик", on_delete=models.PROTECT, default=None, null=True, blank=True)
    title = models.CharField(max_length=512, verbose_name="Адрес точки продаж", default="", null=True, blank=True)
    postcode = models.CharField(max_length=6, verbose_name="Индекс", default="", null=True, blank=True)
    region = models.CharField(max_length=50, verbose_name="Регион", default="", null=True, blank=True)
    area = models.CharField(max_length=50, verbose_name="Район", default="", null=True, blank=True)
    city = models.CharField(max_length=50, verbose_name="Город", default="", null=True, blank=True)
    locality = models.CharField(max_length=50, verbose_name="Населенный пункт", default="", null=True, blank=True)
    street = models.CharField(max_length=50, verbose_name="Улица", default="", null=True, blank=True)
    house = models.CharField(max_length=5, verbose_name="Дом", default="", null=True, blank=True)

    def __str__(self):

        return '{}'.format(self.title)

    def save(self, *args, **kwargs):

        if not self.uid:
            self.uid = get_uuid4()
        if self.city:
            self.title = "{0}, {1}, {2}, {3}, {4}".format(self.postcode, self.region, self.city, self.street, self.house)
        else:
            self.title = "{0}, {1}, {2}, {3}, {4}, {5}".format(self.postcode, self.region, self.area, self.locality, self.street, self.house)           
        
        super(Point_of_sale, self).save(*args, **kwargs)    

    class Meta:
        verbose_name = 'Точка продаж'
        verbose_name_plural = 'Точки продаж'


class FN_type(models.Model):

    uid = models.SlugField(max_length=36, verbose_name='Идентификатор', unique=True, null=True, blank=True)
    title = models.CharField(max_length=16, verbose_name="Наименование")
    validity = models.IntegerField(verbose_name="Срок действия")

    def __str__(self):

        return '{}'.format(self.title)

    def save(self, *args, **kwargs):

        if not self.uid:
            self.uid = get_uuid4()

        super(FN_type, self).save(*args, **kwargs)    

    class Meta:
        verbose_name = 'Тип фискального накопителя'
        verbose_name_plural = 'Типы фискальных накопителей'   


class FN(models.Model):

    uid = models.SlugField(max_length=36, verbose_name='Идентификатор', unique=True, null=True, blank=True)
    fn_model = models.CharField(max_length=16, verbose_name="Модель накопителя")
    fn_mn = models.CharField(max_length=16, verbose_name="Заводской номер ФН")
    fn_type = models.ForeignKey(FN_type, verbose_name="Тип ФН", on_delete=models.PROTECT, default=None, null=True, blank=True)
    installation_date = models.DateField(verbose_name="Дата установки", null=True, blank=True)
    active = models.BooleanField(verbose_name='Активный', default=False)

    def __str__(self):

        return '{}'.format(self.fn_mn)

    def save(self, *args, **kwargs):

        if not self.uid:
            self.uid = get_uuid4()

        super(FN, self).save(*args, **kwargs)    

    class Meta:
        verbose_name = 'Фискальный накопитель'
        verbose_name_plural = 'Фискальные накопители'


class KKT(models.Model):

    uid = models.SlugField(max_length=36, verbose_name='Идентификатор', unique=True, null=True, blank=True)
    customer = models.ForeignKey(Customer, verbose_name="Заказчик", on_delete=models.PROTECT, default=None, null=True, blank=True)
    rn_kkt = models.CharField(max_length=16, verbose_name="Регистрационный номер ККТ")
    mn_kkt = models.CharField(max_length=14, verbose_name="Заводской номер ККТ")
    model_kkt = models.CharField(max_length=16, verbose_name="Модель ККТ")
    fiscalization_date = models.DateField(verbose_name="Дата фискализации", null=True, blank=True)
    point_of_sale = models.ForeignKey(Point_of_sale, verbose_name="Точка продаж", on_delete=models.PROTECT, default=None, null=True, blank=True)
    fn = models.ForeignKey(FN, verbose_name="Фискальный накопитель", on_delete=models.PROTECT, default=None, null=True, blank=True)

    def __str__(self):

        return '{}'.format(self.rn_kkt)

    def save(self, *args, **kwargs):

        if not self.uid:
            self.uid = get_uuid4()

        super(KKT, self).save(*args, **kwargs)    

    class Meta:
        verbose_name = 'ККТ'
        verbose_name_plural = 'ККТ'



