from django.conf import settings
from django.core.management.base import BaseCommand
from reports.models import Indication, IndicationType  # Replace 'your_app_name' with the actual app name
import os
from reports.dataloader_utils import load_model_data

SOURCE_DIR = settings.DATA_DIR_INDICATION # e.g. settings.DATA_DIR_INTERVENTION

IMPORT_MODELS = [ # string as model key, serves as key in IMPORT_METADATA
    "IndicationType",
    "Indication",
]

IMPORT_METADATA = {
    "IndicationType": { # same as model name in "import models"
        "dir": os.path.join(SOURCE_DIR, "type"),
        "model": IndicationType, # e.g. Intervention
        "foreign_keys": [], # e.g. ["intervention_types"]
        "foreign_key_models": [] # e.g. [InterventionType]
    },
    "Indication": { # same as model name in "import models"
        "dir": os.path.join(SOURCE_DIR, "indications"), # e.g. "interventions"
        "model": Indication, # e.g. Intervention
        "foreign_keys": ["indication_types"], # e.g. ["intervention_types"]
        "foreign_key_models": [IndicationType] # e.g. [InterventionType]
    },
}

class Command(BaseCommand):
    help = """Load all .yaml files in the data/intervention directory
    into the Intervention and InterventionType model"""

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Display verbose output',
        )

    def handle(self, *args, **options):
        verbose = options['verbose']
        for model_name in IMPORT_MODELS:
            _metadata = IMPORT_METADATA[model_name]
            load_model_data(
                self,
                model_name,
                _metadata,
                verbose
            )