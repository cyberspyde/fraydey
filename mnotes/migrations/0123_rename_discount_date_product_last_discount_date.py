# Generated by Django 3.2.8 on 2022-02-12 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0122_product_discount_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discount_date',
            new_name='last_discount_date',
        ),
    ]