# Generated by Django 3.2.8 on 2021-10-19 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_text', models.CharField(max_length=400)),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
    ]
