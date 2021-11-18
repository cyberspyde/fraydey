# Generated by Django 3.2.8 on 2021-10-31 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mnotes', '0064_product_product_sold_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_price_sold',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_sold_count',
        ),
        migrations.CreateModel(
            name='ProductSold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_sold_price', models.IntegerField(default=0)),
                ('product_sold_count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]