from django.conf import settings
import os
from django.core.management.base import BaseCommand
from reports.models import Organ, OrganComponent
import yaml

class Command(BaseCommand):
    help = 'Load all .yaml files in the data/organ directory into the Organ and OrganComponent models'

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Display verbose output',
        )

    def handle(self, *args, **options):
        verbose = options['verbose']

        organ_dir = os.path.join(settings.BASE_DIR, 'data', 'organ')

        def load_data(model, yaml_data):
            for entry in yaml_data:
                fields = entry.get('fields', {})
                name = fields.pop('name', None)
                obj, created = model.objects.get_or_create(name=name, defaults=fields)
                
                if created and verbose:
                    self.stdout.write(self.style.SUCCESS(f'Created {model.__name__} {name}'))
                elif verbose:
                    self.stdout.write(self.style.WARNING(f'Skipped {model.__name__} {name}, already exists'))

        for organ_file in [f for f in os.listdir(organ_dir) if f.endswith('.yaml')]:
            with open(os.path.join(organ_dir, organ_file), 'r') as f:
                yaml_data = yaml.safe_load(f)
            load_data(Organ, yaml_data)

        organ_folders = [d for d in os.listdir(organ_dir) if os.path.isdir(os.path.join(organ_dir, d))]

        for folder in organ_folders:
            folder_path = os.path.join(organ_dir, folder)
            if folder.endswith('-components'):
                for component_file in [f for f in os.listdir(folder_path) if f.endswith('.yaml')]:
                    with open(os.path.join(folder_path, component_file), 'r') as f:
                        yaml_data = yaml.safe_load(f)
                    
                    for entry in yaml_data:
                        fields = entry.get('fields', {})
                        name = fields.pop('name', None)
                        organ_name = fields.pop('organ', None)
                        try:
                            organ_instance = Organ.objects.get_by_natural_key(organ_name)
                        except Organ.DoesNotExist:
                            self.stdout.write(self.style.ERROR(f'Organ {organ_name} does not exist'))
                            # continue
                        fields['organ'] = organ_instance
                        
                        obj, created = OrganComponent.objects.get_or_create(name=name, defaults=fields)
                        
                        if created and verbose:
                            self.stdout.write(self.style.SUCCESS(f'Created OrganComponent {name} from {component_file}'))
                        elif verbose:
                            self.stdout.write(self.style.WARNING(f'Skipped OrganComponent {name} from {component_file}, already exists'))
