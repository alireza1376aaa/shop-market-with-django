# Generated by Django 3.1.5 on 2021-03-01 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0040_auto_20210228_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 13, 47, 52, 872733), verbose_name='تاریخ سفارش'),
        ),
    ]
