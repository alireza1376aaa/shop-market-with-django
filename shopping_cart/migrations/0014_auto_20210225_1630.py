# Generated by Django 3.1.5 on 2021-02-25 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0013_auto_20210225_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 25, 16, 30, 50, 302071), verbose_name='تاریخ سفارش'),
        ),
    ]
