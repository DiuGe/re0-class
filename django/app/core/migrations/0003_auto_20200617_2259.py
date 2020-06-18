# Generated by Django 3.0.7 on 2020-06-17 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbase',
            name='login_id',
            field=models.CharField(default='na', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userbase',
            name='login_type',
            field=models.CharField(choices=[['EMAIL', 'EMAIL'], ['WECHAT', 'WECHAT']], default='EMAIL', max_length=255),
        ),
        migrations.AddField(
            model_name='userbase',
            name='wechat_open_id',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='email',
            field=models.EmailField(default='', max_length=255),
        ),
    ]