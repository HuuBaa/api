# Generated by Django 2.0.7 on 2018-08-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, help_text='头像', null=True, upload_to='avatar/', verbose_name='头像'),
        ),
    ]
