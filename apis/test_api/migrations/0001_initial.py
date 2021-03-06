# Generated by Django 2.0.7 on 2018-07-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestApiModel',
            fields=[
                ('id', models.IntegerField(help_text='id名', primary_key=True, serialize=False, verbose_name='id名')),
                ('name', models.CharField(help_text='名字', max_length=100, verbose_name='名字')),
                ('numbers', models.BigIntegerField(help_text='数量', verbose_name='数量')),
                ('time', models.DateTimeField(help_text='时间', verbose_name='时间')),
                ('content', models.TextField(help_text='内容', verbose_name='内容')),
            ],
            options={
                'verbose_name': '测试apiModel',
                'verbose_name_plural': '测试apiModel',
            },
        ),
    ]
