# Generated by Django 3.2.8 on 2021-12-11 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0116_alter_customer_customer_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyondebt',
            old_name='product_count',
            new_name='product_bought_count',
        ),
        migrations.RenameField(
            model_name='buyondebt',
            old_name='product_price',
            new_name='product_bought_price',
        ),
    ]
