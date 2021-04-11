# Generated by Django 3.1.5 on 2021-02-27 18:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collect_product', '0001_initial'),
        ('Product_shop', '0027_auto_20210227_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_shop',
            name='collect_products',
        ),
        migrations.AddField(
            model_name='product_shop',
            name='collect',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='collect_product.collect_product', verbose_name='محصول'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product_shop',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 27, 21, 34, 14, 374843), verbose_name='تاریخ محصول'),
        ),
        migrations.DeleteModel(
            name='collect_product',
        ),
    ]