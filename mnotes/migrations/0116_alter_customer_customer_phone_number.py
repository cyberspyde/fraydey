# Generated by Django 3.2.8 on 2021-12-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0115_remove_vendor_agreement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
