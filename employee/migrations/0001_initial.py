# Generated by Django 4.2.1 on 2023-05-22 10:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email_number', models.EmailField(max_length=150)),
                ('password', models.CharField(max_length=15)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.MaxLengthValidator(10)])),
                ('job_title', models.CharField(max_length=150)),
                ('descr', models.TextField(max_length=500)),
            ],
        ),
    ]
