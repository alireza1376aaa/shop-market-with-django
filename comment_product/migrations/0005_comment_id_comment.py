# Generated by Django 3.1.5 on 2021-03-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment_product', '0004_auto_20210301_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='id_comment',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
