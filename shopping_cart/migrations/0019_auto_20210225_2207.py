# Generated by Django 3.1.5 on 2021-02-25 18:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0018_auto_20210225_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 25, 22, 7, 3, 919816), verbose_name='تاریخ سفارش'),
        ),
    ]
