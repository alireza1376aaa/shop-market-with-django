# Generated by Django 3.1.5 on 2021-03-19 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0058_auto_20210304_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 19, 16, 27, 48, 297737), verbose_name='تاریخ سفارش'),
        ),
    ]
