# Generated by Django 2.0.7 on 2018-07-16 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_api', '0002_auto_20180716_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testapimodel',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='时间戳', verbose_name='时间戳'),
        ),
    ]
