# Generated by Django 3.1.5 on 2021-03-01 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_shop', '0037_auto_20210301_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_shop',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 13, 54, 32, 913592), verbose_name='تاریخ محصول'),
        ),
    ]