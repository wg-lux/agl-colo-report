from django.conf import settings
import os
from django.core.management.base import BaseCommand
from reports.models import Unit  ########## CHANGE ACCORDINGLY ##########
import yaml

class Command(BaseCommand):
    help = 'Load all .yaml files in the settings.DATA_DIR_UNIT into the Unit model' ########## CHANGE ACCORDINGLY ##########

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Display verbose output',
        )

    def handle(self, *args, **options):
        verbose = options['verbose']
        
        sources_dir = settings.DATA_DIR_UNIT ########## CHANGE ACCORDINGLY ##########

        def load_data(model, yaml_data):
            for entry in yaml_data:
                fields = entry.get('fields', {})
                name = fields.pop('name', None)
                
                obj, created = model.objects.get_or_create(name=name, defaults=fields)
                
                if created and verbose:
                    self.stdout.write(self.style.SUCCESS(f'Created {model.__name__} {name}'))
                elif verbose:
                    self.stdout.write(self.style.WARNING(f'Skipped {model.__name__} {name}, already exists'))

        for u in [f for f in os.listdir(sources_dir) if f.endswith('.yaml')]:
            with open(os.path.join(sources_dir, u), 'r') as f:
                yaml_data = yaml.safe_load(f)
            load_data(Unit, yaml_data) ########## CHANGE ACCORDINGLY ##########
