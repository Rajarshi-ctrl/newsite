# Generated by Django 4.1.5 on 2023-01-21 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=40)),
                ('message', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
            ],
        ),
    ]