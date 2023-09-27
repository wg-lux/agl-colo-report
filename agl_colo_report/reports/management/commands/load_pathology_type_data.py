from django.conf import settings
import os
from django.core.management.base import BaseCommand
from reports.models import PathologyType  # Replace 'your_app_name' with the actual app name
import yaml

class Command(BaseCommand):
    help = 'Load all .yaml files in the data/pathology-type directory into the PathologyType model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Display verbose output',
        )

    def handle(self, *args, **options):
        verbose = options['verbose']
        
        # Assuming the directory path is in settings as DATA_DIR_INFORMATION_SOURCE
        pathology_types_dir = settings.DATA_DIR_PATHOLOGY_TYPE

        def load_data(model, yaml_data):
            for entry in yaml_data:
                fields = entry.get('fields', {})
                name = fields.pop('name', None)
                
                obj, created = model.objects.get_or_create(name=name, defaults=fields)
                
                if created and verbose:
                    self.stdout.write(self.style.SUCCESS(f'Created {model.__name__} {name}'))
                elif verbose:
                    self.stdout.write(self.style.WARNING(f'Skipped {model.__name__} {name}, already exists'))

        for pathology_type_file in [f for f in os.listdir(pathology_types_dir) if f.endswith('.yaml')]:
            with open(os.path.join(pathology_types_dir, pathology_type_file), 'r') as f:
                yaml_data = yaml.safe_load(f)
            load_data(PathologyType, yaml_data)
