# Generated by Django 3.1.5 on 2021-02-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ditails_product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_color', models.CharField(max_length=50, verbose_name='رنگ محصول')),
            ],
            options={
                'verbose_name': 'رنگ محصول',
                'verbose_name_plural': 'رنگ محصولات',
            },
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': 'سایز محصول', 'verbose_name_plural': 'سایز محصولات'},
        ),
    ]