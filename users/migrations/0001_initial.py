# Generated by Django 2.2 on 2019-04-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('display_name', models.CharField(max_length=100)),
                ('api_key', models.CharField(max_length=10)),
            ],
        ),
    ]