# Generated by Django 3.2.8 on 2021-10-31 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0066_productsold_product_sold_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsold',
            name='product_sold_id',
        ),
    ]