# Generated by Django 3.1.5 on 2021-02-25 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_shop', '0020_auto_20210225_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag_product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 25, 22, 38, 14, 619116), verbose_name='تاریخ تگ'),
        ),
    ]
