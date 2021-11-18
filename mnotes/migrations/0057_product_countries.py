# Generated by Django 3.2.8 on 2021-10-25 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0056_alter_product_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Countries',
            field=models.CharField(choices=[('AUT', 'Austria'), ('DEU', 'Germany'), ('NLD', 'Neitherlands')], default=('AUT', 'Austria'), max_length=100),
        ),
    ]