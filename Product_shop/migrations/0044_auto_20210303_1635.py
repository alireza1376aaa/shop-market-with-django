# Generated by Django 3.1.5 on 2021-03-03 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_shop', '0043_auto_20210303_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_shop',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 3, 16, 35, 11, 710711), verbose_name='تاریخ محصول'),
        ),
    ]
