# Generated by Django 3.1.5 on 2021-03-19 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_prducts', '0002_auto_20210304_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 19, 16, 27, 48, 466746), verbose_name='تاریخ '),
        ),
    ]
