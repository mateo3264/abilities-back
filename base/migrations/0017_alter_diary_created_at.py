# Generated by Django 4.1 on 2022-09-24 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_diary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
