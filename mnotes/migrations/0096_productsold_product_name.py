# Generated by Django 3.2.8 on 2021-11-21 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0095_auto_20211121_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsold',
            name='product_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
