# Generated by Django 4.2.5 on 2023-09-26 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_delete_polypmorphology_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colonpolypmorphology',
            old_name='morphology_categorical',
            new_name='categorical',
        ),
        migrations.RenameField(
            model_name='colonpolypmorphology',
            old_name='morphology_paris',
            new_name='paris',
        ),
    ]
