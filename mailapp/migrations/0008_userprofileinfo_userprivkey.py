# Generated by Django 2.2.7 on 2019-11-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailapp', '0007_auto_20191127_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='userPrivKey',
            field=models.CharField(default='xxxxxxxxxx', max_length=1000),
        ),
    ]
