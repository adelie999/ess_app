# Generated by Django 2.1.2 on 2019-05-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='photo_path',
            field=models.ImageField(upload_to='photo/', verbose_name='写真のパス'),
        ),
    ]
