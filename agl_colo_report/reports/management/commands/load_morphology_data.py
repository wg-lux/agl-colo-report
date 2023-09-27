from django.conf import settings
import os
from django.core.management.base import BaseCommand
import yaml
from reports.models import MorphologyClassification, MorphologyCategory, PathologyType

class Command(BaseCommand):
    help = 'Load all .yaml files in the data/morphology directory into the Morphology model'

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Display verbose output',
        )

    def handle(self, *args, **options):
        verbose = options['verbose']
        
        source_dir = settings.DATA_DIR_MORPHOLOGY

        def load_data(model, yaml_data, foreign_keys, foreign_key_models, foreign_key_is_list):
            for entry in yaml_data:
                fields = entry.get('fields', {})
                name = fields.pop('name', None)
                _pathology_types = []

                key_model_tuples = zip(foreign_keys, foreign_key_models, foreign_key_is_list)
                for key, foreign_key_model, key_is_list in key_model_tuples:
                    # Use the natural key to look up the related object
                    try:
                        if key_is_list:
                            # the field is a Many to X field.
                            target_natural_keys = fields.pop(key, None)

                            objs = []
                            for _query in target_natural_keys:
                                obj = foreign_key_model.objects.get_by_natural_key(_query)
                                objs.append(obj)
                        
                        else:
                            # the field is a One to X field.
                            target_natural_keys = fields.pop(key, None)
                            objs = foreign_key_model.objects.get_by_natural_key(target_natural_keys)
                            ###########HACKY STUFF WEIL SPÄT#################


                        
                    except model.DoesNotExist:
                        self.stderr.write(self.style.ERROR(f'{model.__name__} with natural key {_query} does not exist. Skipping {name}.'))

                    # Assign the related object to the field
                    if key == "pathology_types":
                        _pathology_types = objs
                    else:
                        fields[key] = objs

                obj, created = model.objects.get_or_create(name=name, defaults=fields)
                if _pathology_types and created:
                    obj.pathology_types.set(_pathology_types)
                
                if created and verbose:
                    self.stdout.write(self.style.SUCCESS(f'Created {model.__name__} {name}'))
                elif verbose:
                    self.stdout.write(self.style.WARNING(f'Skipped {model.__name__} {name}, already exists'))

        #  Load morphology classifications
        _dir = os.path.join(source_dir, 'classification')
        foreign_keys = ["pathology_types"]
        foreign_key_models = [PathologyType]
        foreign_key_is_list = [True]

        for source_file in [f for f in os.listdir(_dir) if f.endswith('.yaml')]:
            with open(os.path.join(_dir, source_file), 'r') as f:
                yaml_data = yaml.safe_load(f)
            load_data(MorphologyClassification, yaml_data, foreign_keys, foreign_key_models, foreign_key_is_list)

        #  Load morphology categories
        _dir = os.path.join(source_dir, 'category')
        foreign_keys = ["classification"]
        foreign_key_models = [MorphologyClassification]
        foreign_key_is_list = [False]

        for source_file in [f for f in os.listdir(_dir) if f.endswith('.yaml')]:
            with open(os.path.join(_dir, source_file), 'r') as f:
                yaml_data = yaml.safe_load(f)
            load_data(MorphologyCategory, yaml_data, foreign_keys, foreign_key_models, foreign_key_is_list)
