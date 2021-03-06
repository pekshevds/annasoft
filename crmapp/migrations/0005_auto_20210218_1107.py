# Generated by Django 3.1.5 on 2021-02-18 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0004_auto_20210218_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address1',
            field=models.CharField(blank=True, default='', max_length=1024, verbose_name='Адрес юридический'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=1024, verbose_name='Адрес фактический'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Краткая характеристика'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='Адрес e-mail'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='inn',
            field=models.CharField(blank=True, default='', max_length=12, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='kpp',
            field=models.CharField(blank=True, default='', max_length=9, verbose_name='КПП'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone1',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone2',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='person',
            name='address1',
            field=models.CharField(blank=True, default='', max_length=1024, verbose_name='Адрес по прописке'),
        ),
        migrations.AlterField(
            model_name='person',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=1024, verbose_name='Адрес проживания'),
        ),
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Краткая характеристика'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, verbose_name='Адрес e-mail'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=1024, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='person',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone1',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone2',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
    ]
