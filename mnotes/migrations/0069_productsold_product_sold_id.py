# Generated by Django 3.2.8 on 2021-10-31 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0068_alter_productsold_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsold',
            name='product_sold_id',
            field=models.IntegerField(default=0),
        ),
    ]
