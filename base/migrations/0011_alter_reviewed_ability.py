# Generated by Django 4.1 on 2022-08-27 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_reviewed_ability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewed',
            name='ability',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.ability'),
        ),
    ]
