# Generated by Django 3.1.5 on 2021-03-01 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_shop', '0031_auto_20210301_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_shop',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 13, 48, 17, 694152), verbose_name='تاریخ محصول'),
        ),
    ]
