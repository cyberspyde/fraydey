# Generated by Django 3.2.8 on 2022-01-03 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0119_remove_productsold_soldproductid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsold',
            name='product_sold_id',
        ),
    ]