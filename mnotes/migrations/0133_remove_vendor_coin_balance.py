# Generated by Django 4.0.6 on 2022-07-21 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0132_alter_vendor_coin_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='coin_balance',
        ),
    ]