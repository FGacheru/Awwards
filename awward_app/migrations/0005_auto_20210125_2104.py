# Generated by Django 3.1.3 on 2021-01-25 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awward_app', '0004_auto_20210125_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
