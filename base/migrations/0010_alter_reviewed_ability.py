# Generated by Django 4.1 on 2022-08-27 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_reviewed_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewed',
            name='ability',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.ability'),
        ),
    ]
