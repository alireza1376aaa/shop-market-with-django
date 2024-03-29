# Generated by Django 3.1.5 on 2021-03-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0004_auto_20210303_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='slider_image1_responsive',
            field=models.ImageField(blank=True, default='defult.jpg', null=True, upload_to='slider', verbose_name='عکس کالکشن ریسپانسیو 1 (171*510)'),
        ),
        migrations.AddField(
            model_name='collection',
            name='slider_image2_responsive',
            field=models.ImageField(blank=True, default='defult.jpg', null=True, upload_to='slider', verbose_name='عکس کالکشن ریسپانسیو 2  (171*510)'),
        ),
        migrations.AddField(
            model_name='collection',
            name='slider_image3_responsive',
            field=models.ImageField(blank=True, default='defult.jpg', null=True, upload_to='slider', verbose_name='عکس کالکشن ریسپانسیو 3 (171*510)'),
        ),
        migrations.AddField(
            model_name='collection',
            name='slider_image4_responsive',
            field=models.ImageField(blank=True, default='defult.jpg', null=True, upload_to='slider', verbose_name='عکس کالکشن ریسپانسیو 4 (171*510)'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='slider_image1',
            field=models.ImageField(blank=True, default='defult.jpg', null=True, upload_to='slider', verbose_name='عکس کالکشن 1(560*380) '),
        ),
        migrations.AlterField(
            model_name='collection',
            name='slider_image2',
            field=models.ImageField(blank=True, default='defult.jpg', null=True, upload_to='slider', verbose_name='عکس کالکشن 2 (265*515)'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='slider_image3',
            field=models.ImageField(blank=True, default='defult.jpg', null=True, upload_to='slider', verbose_name='عکس کالکشن 3 (265*243)'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='slider_image4',
            field=models.ImageField(blank=True, default='defult.jpg', null=True, upload_to='slider', verbose_name='عکس کالکشن 4 (265*790)'),
        ),
    ]
