# Generated by Django 3.2.8 on 2021-11-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnotes', '0084_alter_product_isdebt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_count',
            field=models.IntegerField(default=0, error_messages={'password_mismatch': 'Ikki xil parol kiritildi', 'required': 'Siz muhim ma`lumotlarni to`ldirmardingiz!', 'unique': 'Bu nom bilan akkount mavjud, boshqa nom tanlang'}),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, error_messages={'password_mismatch': 'Ikki xil parol kiritildi', 'required': 'Siz muhim ma`lumotlarni to`ldirmardingiz!', 'unique': 'Bu nom bilan akkount mavjud, boshqa nom tanlang'}, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price_initial',
            field=models.IntegerField(default=0, error_messages={'password_mismatch': 'Ikki xil parol kiritildi', 'required': 'Siz muhim ma`lumotlarni to`ldirmardingiz!', 'unique': 'Bu nom bilan akkount mavjud, boshqa nom tanlang'}),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price_told',
            field=models.IntegerField(default=0, error_messages={'password_mismatch': 'Ikki xil parol kiritildi', 'required': 'Siz muhim ma`lumotlarni to`ldirmardingiz!', 'unique': 'Bu nom bilan akkount mavjud, boshqa nom tanlang'}),
        ),
    ]
