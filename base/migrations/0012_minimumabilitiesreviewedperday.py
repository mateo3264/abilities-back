# Generated by Django 4.1 on 2022-09-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_reviewed_ability'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinimumAbilitiesReviewedPerDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateField(auto_now_add=True)),
                ('minimum_abilities_reviewed_per_day', models.IntegerField(default=3)),
            ],
        ),
    ]
