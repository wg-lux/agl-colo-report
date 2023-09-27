from django.conf import settings
import os
from django.core.management.base import BaseCommand
from reports.models import OrganComponent, Anastomosis, ColonAnatomy
import yaml

class Command(BaseCommand):
    help = 'Load all .yaml files in the data/colon_anatomy directory into the ColonAnatomy model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Display verbose output',
        )

    def handle(self, *args, **options):
        verbose = options['verbose']

        colon_anatomy_dir = settings.DATA_DIR_COLON_ANATOMY

        def load_data(yaml_data):
            for entry in yaml_data:
                fields = entry.get('fields', {})
                name = fields.pop('name', None)

                available_segments_names = fields.pop('available_segments', [])
                available_anastomoses_names = fields.pop('available_anastomoses', [])
                
                available_segments = OrganComponent.objects.filter(name__in=available_segments_names)
                available_anastomoses = Anastomosis.objects.filter(name__in=available_anastomoses_names)

                obj, created = ColonAnatomy.objects.get_or_create(name=name, defaults=fields)

                if created:
                    obj.available_segments.set(available_segments)
                    obj.available_anastomoses.set(available_anastomoses)

                    if verbose:
                        self.stdout.write(self.style.SUCCESS(f'Created ColonAnatomy {name}'))
                elif verbose:
                    self.stdout.write(self.style.WARNING(f'Skipped ColonAnatomy {name}, already exists'))

        for colon_anatomy_file in [f for f in os.listdir(colon_anatomy_dir) if f.endswith('.yaml')]:
            with open(os.path.join(colon_anatomy_dir, colon_anatomy_file), 'r') as f:
                yaml_data = yaml.safe_load(f)
            load_data(yaml_data)
