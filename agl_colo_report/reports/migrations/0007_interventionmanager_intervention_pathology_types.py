# Generated by Django 4.2.5 on 2023-09-26 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_intervention_interventiontype'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterventionManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='intervention',
            name='pathology_types',
            field=models.ManyToManyField(related_name='interventions', to='reports.pathologytype'),
        ),
    ]
