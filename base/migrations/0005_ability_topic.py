# Generated by Django 4.1 on 2022-08-09 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='ability',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='base.topic'),
        ),
    ]
