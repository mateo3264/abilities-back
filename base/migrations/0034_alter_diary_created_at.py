# Generated by Django 4.1 on 2022-10-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_alter_diary_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
