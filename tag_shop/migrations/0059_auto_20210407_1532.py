# Generated by Django 3.1.5 on 2021-04-07 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_shop', '0058_auto_20210319_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag_product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 7, 15, 32, 18, 982025), verbose_name='تاریخ تگ'),
        ),
    ]
