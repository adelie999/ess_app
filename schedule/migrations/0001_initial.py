# Generated by Django 2.1.2 on 2019-05-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('start_date', models.DateTimeField(verbose_name='開始日')),
                ('end_date', models.DateTimeField(verbose_name='終了日')),
                ('description', models.TextField(verbose_name='予定の内容')),
                ('created_at', models.DateTimeField(verbose_name='作成日')),
                ('updated_at', models.DateTimeField(verbose_name='更新日')),
            ],
        ),
    ]
