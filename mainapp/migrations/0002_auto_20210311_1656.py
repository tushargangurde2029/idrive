# Generated by Django 3.1.7 on 2021-03-11 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='user',
        ),
        migrations.AddField(
            model_name='user_data',
            name='email',
            field=models.CharField(default='xxx@gmail.com', max_length=30),
        ),
    ]
