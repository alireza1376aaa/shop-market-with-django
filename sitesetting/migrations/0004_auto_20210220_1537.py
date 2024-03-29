# Generated by Django 3.1.5 on 2021-02-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesetting', '0003_auto_20210219_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetting',
            name='aparat_address',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='google_locution',
        ),
        migrations.AddField(
            model_name='contact_us',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='خوانده شده / نشده'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='about_office',
            field=models.TextField(default='', verbose_name='درباره شرکت'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='write_ruls',
            field=models.TextField(default='', verbose_name='قوانین کپی رایت'),
        ),
    ]
