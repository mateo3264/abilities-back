# Generated by Django 4.1 on 2022-10-01 11:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_ability_answer_correctness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='answer_correctness',
            field=models.PositiveSmallIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MinValueValidator(10)]),
        ),
    ]
