# Generated by Django 3.1.5 on 2021-03-04 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_shop', '0056_auto_20210304_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag_product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 15, 24, 18, 375483), verbose_name='تاریخ تگ'),
        ),
    ]