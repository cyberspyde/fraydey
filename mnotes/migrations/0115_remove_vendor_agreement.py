# Generated by Django 3.2.8 on 2021-12-03 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0114_vendor_agreement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='agreement',
        ),
    ]
