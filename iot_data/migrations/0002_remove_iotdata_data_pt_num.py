# Generated by Django 2.1.7 on 2019-04-04 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iot_data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iotdata',
            name='data_pt_num',
        ),
    ]
