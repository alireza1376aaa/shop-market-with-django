# Generated by Django 3.1.5 on 2021-03-04 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0054_auto_20210303_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 11, 34, 47, 767982), verbose_name='تاریخ سفارش'),
        ),
    ]
