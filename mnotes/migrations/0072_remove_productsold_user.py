# Generated by Django 3.2.8 on 2021-11-01 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0071_alter_productsold_product_sold_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsold',
            name='user',
        ),
    ]