# Generated by Django 3.2.8 on 2021-11-11 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0092_auto_20211110_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsold',
            name='isfullypaid',
        ),
        migrations.RemoveField(
            model_name='productsold',
            name='ispartlypaid',
        ),
        migrations.RemoveField(
            model_name='productsold',
            name='left_amount',
        ),
        migrations.RemoveField(
            model_name='productsold',
            name='paid_amount',
        ),
        migrations.AddField(
            model_name='sellondebt',
            name='isfullypaid',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sellondebt',
            name='ispartlypaid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sellondebt',
            name='left_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sellondebt',
            name='paid_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='buyondebt',
            name='isfullypaid',
            field=models.BooleanField(default=False),
        ),
    ]