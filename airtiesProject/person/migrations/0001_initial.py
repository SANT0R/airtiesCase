# Generated by Django 3.2.6 on 2021-08-19 20:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50, null=True, verbose_name='Ad')),
                ('lastName', models.CharField(max_length=50, null=True, verbose_name='Soyad')),
                ('phone', models.CharField(max_length=50, null=True, verbose_name='Telefon')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='Email')),
                ('createdDate', models.DateField(default=datetime.datetime.now, null=True, verbose_name='Oluşturulma Tarihi')),
            ],
        ),
    ]
