# Generated by Django 4.1.2 on 2023-09-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FN_accounting', '0011_point_of_sale_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point_of_sale',
            name='title',
            field=models.CharField(blank=True, default='', max_length=512, null=True, verbose_name='Адрес точки продаж'),
        ),
    ]
