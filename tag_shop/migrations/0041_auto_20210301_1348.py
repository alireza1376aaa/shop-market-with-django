# Generated by Django 3.1.5 on 2021-03-01 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_shop', '0040_auto_20210301_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag_product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 1, 13, 48, 17, 686152), verbose_name='تاریخ تگ'),
        ),
    ]
