# Generated by Django 3.1.5 on 2021-03-23 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0016_auto_20210322_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='crmapp.task', verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='task',
            name='from_customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='from_customer', to='crmapp.employee', verbose_name='От заказчика'),
        ),
        migrations.AlterField(
            model_name='task',
            name='from_performer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='from_performer', to='crmapp.employee', verbose_name='От исполнителя'),
        ),
    ]
