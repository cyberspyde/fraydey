# Generated by Django 3.2.8 on 2021-10-23 21:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0034_auto_20211023_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='the_choices',
        ),
        migrations.AddField(
            model_name='product',
            name='product_color',
            field=models.CharField(default='Qizil', max_length=300),
        ),
        migrations.AddField(
            model_name='product',
            name='product_season',
            field=models.CharField(default='Qishki', max_length=300),
        ),
        migrations.AddField(
            model_name='product',
            name='product_size',
            field=models.CharField(default='L', max_length=300),
        ),
        migrations.AlterField(
            model_name='notes',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 21, 40, 33, 312693)),
        ),
        migrations.AlterField(
            model_name='product',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 23, 21, 40, 33, 312693)),
        ),
        migrations.DeleteModel(
            name='Choices',
        ),
    ]
