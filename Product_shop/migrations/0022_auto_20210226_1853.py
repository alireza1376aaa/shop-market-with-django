# Generated by Django 3.1.5 on 2021-02-26 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_shop', '0021_auto_20210225_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_shop',
            name='product_Gender',
            field=models.CharField(choices=[('women', 'زنانه'), ('men', 'مردانه'), ('kids', 'بجه گانه')], default='S', max_length=10, verbose_name='محصول مربوط با '),
        ),
        migrations.AlterField(
            model_name='product_shop',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 26, 18, 53, 18, 972646), verbose_name='تاریخ محصول'),
        ),
    ]
