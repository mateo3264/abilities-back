# Generated by Django 4.1 on 2022-08-16 23:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_ability_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='ability',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 16, 18, 5, 21, 681412)),
        ),
        migrations.AddField(
            model_name='answers',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 16, 18, 5, 21, 681412)),
        ),
    ]