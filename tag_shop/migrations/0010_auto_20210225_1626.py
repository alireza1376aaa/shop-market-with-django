# Generated by Django 3.1.5 on 2021-02-25 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_shop', '0009_auto_20210225_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag_product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 25, 16, 26, 54, 364257), verbose_name='تاریخ تگ'),
        ),
    ]
