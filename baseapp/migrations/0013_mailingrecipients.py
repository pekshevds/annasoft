# Generated by Django 4.1.2 on 2024-10-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0012_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailingRecipients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Email для рассылки',
                'verbose_name_plural': 'Email для рассылки',
            },
        ),
    ]
