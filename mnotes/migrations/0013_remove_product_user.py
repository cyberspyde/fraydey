# Generated by Django 3.2.8 on 2021-10-22 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0012_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
