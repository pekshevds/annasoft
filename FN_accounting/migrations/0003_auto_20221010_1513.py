# Generated by Django 3.1.7 on 2022-10-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FN_accounting', '0002_auto_20221010_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fn',
            options={'verbose_name': 'Фискальных накопителей'},
        ),
        migrations.AlterModelOptions(
            name='fn_type',
            options={'verbose_name': 'Типы фискальных накопителей'},
        ),
        migrations.AlterModelOptions(
            name='kkt',
            options={'verbose_name': 'ККТ'},
        ),
        migrations.AlterModelOptions(
            name='point_of_sale',
            options={'verbose_name': 'точки продаж'},
        ),
        migrations.AddField(
            model_name='fn',
            name='uid',
            field=models.SlugField(default='', max_length=36, unique=True, verbose_name='Идентификатор'),
        ),
        migrations.AddField(
            model_name='fn_type',
            name='uid',
            field=models.SlugField(default='', max_length=36, unique=True, verbose_name='Идентификатор'),
        ),
        migrations.AddField(
            model_name='kkt',
            name='uid',
            field=models.SlugField(default='', max_length=36, unique=True, verbose_name='Идентификатор'),
        ),
        migrations.AddField(
            model_name='point_of_sale',
            name='uid',
            field=models.SlugField(default='', max_length=36, unique=True, verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='fn',
            name='installation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата установки'),
        ),
    ]
