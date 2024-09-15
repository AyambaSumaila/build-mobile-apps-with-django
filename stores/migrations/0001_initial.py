# Generated by Django 5.1.1 on 2024-09-13 07:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizzas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('street', models.CharField(blank=True, max_length=400)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, max_length=200)),
                ('zip_code', models.IntegerField(blank=True, default=0, max_length=20)),
                ('website', models.URLField(blank=True)),
                ('phone_number', models.CharField(blank=True, help_text='Format: +999999999', max_length=17, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')])),
                ('description', models.TextField(blank=True)),
                ('logo_image', models.ImageField(blank=True, upload_to='Images/logo.png')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
