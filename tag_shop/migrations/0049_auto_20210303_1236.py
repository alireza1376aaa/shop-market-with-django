# Generated by Django 3.1.5 on 2021-03-03 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_shop', '0048_auto_20210303_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag_product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 3, 12, 36, 39, 373199), verbose_name='تاریخ تگ'),
        ),
    ]
