# Generated by Django 4.1 on 2022-09-27 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_diary_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 27, 9, 0, 36, 865218)),
        ),
    ]
