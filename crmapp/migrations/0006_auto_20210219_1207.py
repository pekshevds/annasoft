# Generated by Django 3.1.5 on 2021-02-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0005_auto_20210218_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='time_actual',
            field=models.FloatField(blank=True, default=1, verbose_name='Время выполнения, факт:'),
        ),
        migrations.AddField(
            model_name='task',
            name='time_scheduled',
            field=models.FloatField(blank=True, default=1, verbose_name='Время выполнения, план:'),
        ),
    ]
