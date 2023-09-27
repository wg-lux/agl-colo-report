from django.conf import settings
import os
from django.core.management.base import BaseCommand
from reports.models import AnastomosisType, Anastomosis, OrganComponent
import yaml

class Command(BaseCommand):
    help = 'Load all .yaml files in the data/anastomosis directory into the AnastomosisType and Anastomosis models'

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Display verbose output',
        )

    def handle(self, *args, **options):
        verbose = options['verbose']

        anastomosis_dir = settings.DATA_DIR_ANASTOMOSIS
        anastomosis_types_dir = os.path.join(anastomosis_dir, 'anastomosis-types')
        anastomoses_dir = os.path.join(anastomosis_dir, 'anastomoses')

        def load_data(model, yaml_data):
            for entry in yaml_data:
                fields = entry.get('fields', {})
                name = fields.pop('name', None)
                
                if model == Anastomosis:
                    component_1_name = fields.pop('component_1', None)
                    component_2_name = fields.pop('component_2', None)
                    connection_type_1_name = fields.pop('connection_type_1', None)
                    connection_type_2_name = fields.pop('connection_type_2', None)
                    
                    component_1 = OrganComponent.objects.get_by_natural_key(component_1_name)
                    component_2 = OrganComponent.objects.get_by_natural_key(component_2_name)
                    connection_type_1 = AnastomosisType.objects.get_by_natural_key(connection_type_1_name)
                    connection_type_2 = AnastomosisType.objects.get_by_natural_key(connection_type_2_name)
                    
                    fields['component_1'] = component_1
                    fields['component_2'] = component_2
                    fields['connection_type_1'] = connection_type_1
                    fields['connection_type_2'] = connection_type_2
                
                obj, created = model.objects.get_or_create(name=name, defaults=fields)
                
                if created and verbose:
                    self.stdout.write(self.style.SUCCESS(f'Created {model.__name__} {name}'))
                elif verbose:
                    self.stdout.write(self.style.WARNING(f'Skipped {model.__name__} {name}, already exists'))

        for anastomosis_type_file in [f for f in os.listdir(anastomosis_types_dir) if f.endswith('.yaml')]:
            with open(os.path.join(anastomosis_types_dir, anastomosis_type_file), 'r') as f:
                yaml_data = yaml.safe_load(f)
            load_data(AnastomosisType, yaml_data)

        for anastomosis_file in [f for f in os.listdir(anastomoses_dir) if f.endswith('.yaml')]:
            with open(os.path.join(anastomoses_dir, anastomosis_file), 'r') as f:
                yaml_data = yaml.safe_load(f)
            load_data(Anastomosis, yaml_data)
