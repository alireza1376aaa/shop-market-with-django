# Generated by Django 3.1.5 on 2021-02-26 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_shop', '0031_auto_20210226_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag_product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 26, 18, 56, 45, 540461), verbose_name='تاریخ تگ'),
        ),
    ]
