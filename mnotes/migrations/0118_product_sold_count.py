# Generated by Django 3.2.8 on 2022-01-03 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0117_auto_20211211_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold_count',
            field=models.IntegerField(default=0),
        ),
    ]