# Generated by Django 3.2.8 on 2021-10-22 21:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mnotes', '0017_alter_product_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notes',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 21, 51, 5, 856436)),
        ),
        migrations.AlterField(
            model_name='product',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 22, 21, 51, 5, 856436)),
        ),
    ]
