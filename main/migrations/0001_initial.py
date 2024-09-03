# Generated by Django 5.1 on 2024-08-25 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('country', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
