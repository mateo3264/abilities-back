# Generated by Django 4.1 on 2022-10-27 19:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_timestudyingtopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='timestudyingtopic',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
