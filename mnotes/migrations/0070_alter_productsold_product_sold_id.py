# Generated by Django 3.2.8 on 2021-11-01 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0069_productsold_product_sold_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsold',
            name='product_sold_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mnotes.product'),
        ),
    ]