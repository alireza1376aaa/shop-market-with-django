# Generated by Django 3.1.5 on 2021-02-26 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag_shop', '0028_auto_20210226_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag_product',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 26, 18, 40, 24, 440345), verbose_name='تاریخ تگ'),
        ),
    ]
