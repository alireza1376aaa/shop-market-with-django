# Generated by Django 3.1.5 on 2021-02-25 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0007_auto_20210225_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 25, 15, 34, 18, 782743), verbose_name='تاریخ سفارش'),
        ),
    ]
