# Generated by Django 3.2.8 on 2021-11-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0100_auto_20211122_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
