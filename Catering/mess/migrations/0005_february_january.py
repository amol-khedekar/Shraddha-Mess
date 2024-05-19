# Generated by Django 3.0.4 on 2020-03-27 17:16

from django.db import migrations, models
import django.utils.timezone
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0004_auto_20200327_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='February',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('attendance', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=66, size=6)),
                ('plates', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='January',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('attendance', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=66, size=6)),
                ('plates', models.IntegerField()),
            ],
        ),
    ]
