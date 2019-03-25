# Generated by Django 2.1.7 on 2019-03-25 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='data_flt',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='data',
            name='data_pt_type',
        ),
        migrations.RemoveField(
            model_name='data',
            name='data_str',
        ),
        migrations.AddField(
            model_name='data',
            name='upload_success',
            field=models.BooleanField(default=True),
        ),
    ]
