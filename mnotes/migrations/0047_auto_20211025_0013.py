# Generated by Django 3.2.8 on 2021-10-25 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0046_remove_notes_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_count',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_price',
        ),
    ]