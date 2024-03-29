# Generated by Django 4.1 on 2022-10-26 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_alter_diary_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStudyingTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in_minutes', models.PositiveSmallIntegerField(default=None)),
                ('topics', models.ManyToManyField(to='base.topic')),
            ],
        ),
    ]
