# Generated by Django 3.1.5 on 2021-02-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0007_auto_20210219_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_actual',
            field=models.TimeField(blank=True, null=True, verbose_name='Время выполнения, факт:'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_scheduled',
            field=models.TimeField(blank=True, null=True, verbose_name='Время выполнения, план:'),
        ),
    ]
