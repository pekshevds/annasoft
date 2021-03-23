# Generated by Django 3.1.5 on 2021-03-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0017_auto_20210323_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time_actual_h',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Время выполнения, норма (час):'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_actual_m',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Время выполнения, норма (мин.):'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_scheduled_h',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Время выполнения, факт (час):'),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_scheduled_m',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Время выполнения, факт (мин.):'),
        ),
    ]
