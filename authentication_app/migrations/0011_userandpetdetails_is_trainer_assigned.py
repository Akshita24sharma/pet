# Generated by Django 5.0.4 on 2024-05-09 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_app', '0010_remove_userandpetdetails_type_of_training_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userandpetdetails',
            name='is_trainer_assigned',
            field=models.BooleanField(default=False),
        ),
    ]
