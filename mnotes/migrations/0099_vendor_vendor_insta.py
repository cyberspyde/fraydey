# Generated by Django 3.2.8 on 2021-11-22 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0098_vendor_store_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_insta',
            field=models.CharField(default='', max_length=200),
        ),
    ]
