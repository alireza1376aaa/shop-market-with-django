# Generated by Django 3.1.5 on 2021-03-03 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_shop', '0038_auto_20210301_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_shop',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 3, 12, 27, 43, 150529), verbose_name='تاریخ محصول'),
        ),
    ]