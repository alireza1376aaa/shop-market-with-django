# Generated by Django 3.1.5 on 2021-02-26 19:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collect_product', '0001_initial'),
        ('Product_shop', '0024_auto_20210226_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='collect_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='عنوان دسته بندی')),
                ('name', models.CharField(max_length=80, verbose_name='نام دسته بندی در url')),
            ],
            options={
                'verbose_name': 'دسته بندی محصول',
                'verbose_name_plural': 'دسته بندی محصولات',
            },
        ),
        migrations.AlterField(
            model_name='product_shop',
            name='product_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 26, 22, 33, 10, 934468), verbose_name='تاریخ محصول'),
        ),
        migrations.AlterField(
            model_name='product_shop',
            name='xxxxxxxxx',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collect_product.collect_product_type', verbose_name='گ محصول'),
        ),
        migrations.AddField(
            model_name='product_shop',
            name='collect_products',
            field=models.ManyToManyField(to='Product_shop.collect_product', verbose_name='دسته بندی'),
        ),
    ]