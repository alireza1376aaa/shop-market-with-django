# Generated by Django 3.1.5 on 2021-02-25 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_shop', '0008_auto_20210225_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag_product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 25, 15, 56, 24, 368562), verbose_name='تاریخ تگ'),
        ),
    ]
