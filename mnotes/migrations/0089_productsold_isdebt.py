# Generated by Django 3.2.8 on 2021-11-10 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0088_alter_buyondebt_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsold',
            name='isdebt',
            field=models.BooleanField(default=False),
        ),
    ]
