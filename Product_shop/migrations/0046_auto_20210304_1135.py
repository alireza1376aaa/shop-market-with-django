# Generated by Django 3.1.5 on 2021-03-04 08:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_shop', '0045_auto_20210304_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_shop',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 11, 35, 50, 188553), verbose_name='تاریخ محصول'),
        ),
    ]
