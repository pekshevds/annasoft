# Generated by Django 3.1.7 on 2021-07-13 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0022_auto_20210713_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='crmapp.customer', verbose_name='Заказчик'),
        ),
    ]