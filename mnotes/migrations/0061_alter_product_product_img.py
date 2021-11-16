# Generated by Django 3.2.8 on 2021-10-26 00:46

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0060_remove_product_countries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.jpg', force_format='JPEG', keep_meta=True, null=True, quality=75, size=[300, 400], upload_to='images'),
        ),
    ]
