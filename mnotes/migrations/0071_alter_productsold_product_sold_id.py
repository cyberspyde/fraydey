# Generated by Django 3.2.8 on 2021-11-01 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0070_alter_productsold_product_sold_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsold',
            name='product_sold_id',
            field=models.IntegerField(default=0),
        ),
    ]
