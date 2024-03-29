# Generated by Django 4.1 on 2022-10-09 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_alter_scheduleabilitieshistory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='ability',
            name='days_to_present_again',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ability',
            name='last_presentation_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
