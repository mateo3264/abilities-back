# Generated by Django 4.1 on 2022-09-27 09:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_diary_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
