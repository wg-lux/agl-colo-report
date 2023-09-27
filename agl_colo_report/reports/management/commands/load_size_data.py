from django.conf import settings
import os
from django.core.management.base import BaseCommand
import yaml
from reports.models import (
    SizeCategory,
    SizeClassification,
    Unit, 
    PathologyType
)

class Command(BaseCommand):
    help = """Load all .yaml files in the data/size directory
    into the SizeCategory and SizeClassification model"""

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Display verbose output',
        )

    def handle(self, *args, **options):
        verbose = options['verbose']
        
        source_dir = settings.DATA_DIR_SIZE

        def load_data_with_foreign_keys(model, yaml_data, foreign_keys, foreign_key_models):
            # Since pathology types is a ManyToMany field, we need to hack arount
            for entry in yaml_data:
                fields = entry.get('fields', {})
                name = fields.pop('name', None)
                many_to_many_tuples = []
                foreign_key_tuples = zip(foreign_keys, foreign_key_models)
                for foreign_key, foreign_key_model in foreign_key_tuples:
                    target_natural_key = fields.pop(foreign_key, None)

                    if isinstance(target_natural_key, list):
                        # the field is a Many to X field.
                        fk_objects = [foreign_key_model.objects.get_by_natural_key(_) for _ in target_natural_key]
                        fk_tuple = (foreign_key, fk_objects)
                        many_to_many_tuples.append(fk_tuple)
                        continue

                    # Use the natural key to look up the related object
                    try:
                        
                        obj = foreign_key_model.objects.get_by_natural_key(target_natural_key)
                    except model.DoesNotExist:
                        self.stderr.write(self.style.ERROR(f'{model.__name__} with natural key {target_natural_key} does not exist. Skipping {name}.'))

                    # Assign the related object to the field
                    fields[foreign_key] = obj

                obj, created = model.objects.get_or_create(name=name, defaults=fields)
                if many_to_many_tuples:
                    for fk, fk_objects in many_to_many_tuples:
                        getattr(obj, fk).set(fk_objects)

                if created and verbose:
                    self.stdout.write(self.style.SUCCESS(f'Created Unit {name}'))
                elif verbose:
                    self.stdout.write(self.style.WARNING(f'Skipped Unit {name}, already exists'))

        # Load SizeClassification
        self.stdout.write("start loading size classification")
        _dir = os.path.join(source_dir, 'classification')
        model = SizeClassification
        foreign_keys = ["pathology_types"]
        foreign_key_models = [PathologyType]
        for file in [f for f in os.listdir(_dir) if f.endswith('.yaml')]:
            with open(os.path.join(_dir, file), 'r') as f:
                yaml_data = yaml.safe_load(f)
            
            load_data_with_foreign_keys(model, yaml_data, foreign_keys, foreign_key_models)

        # Load SizeCategory
        self.stdout.write("start loading size category")
        _dir = os.path.join(source_dir, 'category')
        model = SizeCategory
        foreign_keys = ["unit","classification"]
        foreign_key_models = [Unit, SizeClassification]
        for file in [f for f in os.listdir(_dir) if f.endswith('.yaml')]:
            with open(os.path.join(_dir, file), 'r') as f:
                yaml_data = yaml.safe_load(f)
            
            load_data_with_foreign_keys(model, yaml_data, foreign_keys, foreign_key_models)