# Generated by Django 3.2.8 on 2021-11-29 14:20

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0109_auto_20211128_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[300, 400], upload_to='images/jlnakukpkg'),
        ),
    ]