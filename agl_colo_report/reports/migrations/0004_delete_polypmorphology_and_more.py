# Generated by Django 4.2.5 on 2023-09-26 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_rename_size_classification_sizecategory_classification_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PolypMorphology',
        ),
        migrations.RenameField(
            model_name='colonpolypsize',
            old_name='size_categorical',
            new_name='categorical',
        ),
        migrations.RenameField(
            model_name='colonpolypsize',
            old_name='size_measurement',
            new_name='measurement',
        ),
        migrations.RemoveField(
            model_name='colonpolypsize',
            name='size_paris',
        ),
        migrations.AlterField(
            model_name='sizecategory',
            name='size_max',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sizecategory',
            name='size_min',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
