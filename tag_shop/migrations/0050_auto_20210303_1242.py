# Generated by Django 3.1.5 on 2021-03-03 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_shop', '0049_auto_20210303_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag_product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 3, 12, 42, 40, 575859), verbose_name='تاریخ تگ'),
        ),
    ]
