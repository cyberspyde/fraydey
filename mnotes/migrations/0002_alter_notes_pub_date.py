# Generated by Django 3.2.8 on 2021-10-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date published'),
        ),
    ]
