# Generated by Django 4.1 on 2022-08-09 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_ability_bubu_afterwhentoreview_ability'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
