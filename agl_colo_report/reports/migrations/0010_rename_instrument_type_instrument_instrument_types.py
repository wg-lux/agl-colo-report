# Generated by Django 4.2.5 on 2023-09-27 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_complicationtype_indication_indicationtype_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instrument',
            old_name='instrument_type',
            new_name='instrument_types',
        ),
    ]