# Generated by Django 3.1.5 on 2021-02-25 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0002_auto_20210225_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 25, 11, 3, 29, 811016), verbose_name='تاریخ سفارش'),
        ),
    ]