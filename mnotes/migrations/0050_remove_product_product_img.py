# Generated by Django 3.2.8 on 2021-10-25 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0049_alter_product_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_img',
        ),
    ]