# Generated by Django 4.1 on 2022-08-26 21:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewed',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
