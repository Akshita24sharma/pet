# Generated by Django 5.0.2 on 2024-05-03 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('experience', models.PositiveSmallIntegerField()),
                ('phone', models.PositiveBigIntegerField()),
                ('address', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]