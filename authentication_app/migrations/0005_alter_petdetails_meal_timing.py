# Generated by Django 5.0.2 on 2024-05-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_app', '0004_userdetails_petdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petdetails',
            name='meal_timing',
            field=models.CharField(max_length=200),
        ),
    ]
