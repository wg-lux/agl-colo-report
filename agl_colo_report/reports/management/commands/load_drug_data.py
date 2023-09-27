from json import load
from django.conf import settings
import os
from django.core.management.base import BaseCommand
from reports.models import Unit, Drug
import yaml

class Command(BaseCommand):
    help = 'Load all .yaml files in the data/drugs directory into the Drug model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Display verbose output',
        )

    def handle(self, *args, **options):
        verbose = options['verbose']

        source_dir = settings.DATA_DIR_DRUG

        def load_data(model, yaml_data):
            for entry in yaml_data:
                fields = entry.get('fields', {})
                name = fields.pop('name', None)
                unit_name = fields.pop('preferred_unit', None)
                try:
                    unit_instance = Unit.objects.get_by_natural_key(unit_name)
                except Unit.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Unit {unit_name} does not exist'))
                    raise Exception(f'Unit {unit_name} does not exist')
                    # continue
                fields['preferred_unit'] = unit_instance
                
                obj, created = Drug.objects.get_or_create(name=name, defaults=fields)
                
                if created and verbose:
                    self.stdout.write(self.style.SUCCESS(f'Created Unit {name}'))
                elif verbose:
                    self.stdout.write(self.style.WARNING(f'Skipped Unit {name}, already exists'))

        for file in [f for f in os.listdir(source_dir) if f.endswith('.yaml')]:
            with open(os.path.join(source_dir, file), 'r') as f:
                yaml_data = yaml.safe_load(f)
            
            load_data(Unit, yaml_data)