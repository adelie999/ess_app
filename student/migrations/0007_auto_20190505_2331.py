# Generated by Django 2.1.2 on 2019-05-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20190505_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='photo_path',
            field=models.ImageField(upload_to='images/', verbose_name='写真のパス'),
        ),
    ]
