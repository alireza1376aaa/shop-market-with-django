# Generated by Django 3.1.5 on 2021-03-04 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_shop', '0044_auto_20210303_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_shop',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 11, 34, 47, 760982), verbose_name='تاریخ محصول'),
        ),
    ]
