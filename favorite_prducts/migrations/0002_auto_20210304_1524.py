# Generated by Django 3.1.5 on 2021-03-04 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_prducts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 15, 24, 18, 440487), verbose_name='تاریخ '),
        ),
    ]
