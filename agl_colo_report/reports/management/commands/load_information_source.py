from django.conf import settings
import os
from django.core.management.base import BaseCommand
from reports.models import InformationSource  # Replace 'your_app_name' with the actual app name
import yaml

class Command(BaseCommand):
    help = 'Load all .yaml files in the data/information_sources directory into the InformationSource model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Display verbose output',
        )

    def handle(self, *args, **options):
        verbose = options['verbose']
        
        # Assuming the directory path is in settings as DATA_DIR_INFORMATION_SOURCE
        information_sources_dir = settings.DATA_DIR_INFORMATION_SOURCE

        def load_data(model, yaml_data):
            for entry in yaml_data:
                fields = entry.get('fields', {})
                name = fields.pop('name', None)
                
                obj, created = model.objects.get_or_create(name=name, defaults=fields)
                
                if created and verbose:
                    self.stdout.write(self.style.SUCCESS(f'Created {model.__name__} {name}'))
                elif verbose:
                    self.stdout.write(self.style.WARNING(f'Skipped {model.__name__} {name}, already exists'))

        for information_source_file in [f for f in os.listdir(information_sources_dir) if f.endswith('.yaml')]:
            with open(os.path.join(information_sources_dir, information_source_file), 'r') as f:
                yaml_data = yaml.safe_load(f)
            load_data(InformationSource, yaml_data)
