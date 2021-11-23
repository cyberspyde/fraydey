# Generated by Django 3.2.8 on 2021-10-22 22:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0021_auto_20211022_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.AlterField(
            model_name='notes',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 22, 56, 52, 20859)),
        ),
        migrations.AlterField(
            model_name='product',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 22, 56, 52, 20859)),
        ),
    ]
