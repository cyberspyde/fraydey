# Generated by Django 3.2.8 on 2021-11-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0086_alter_product_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='Mahsulot nomi', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price_initial',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price_told',
            field=models.IntegerField(default=0),
        ),
    ]
