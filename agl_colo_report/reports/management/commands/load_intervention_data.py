from django.conf import settings
from django.core.management.base import BaseCommand
from reports.models import Intervention, InterventionType  # Replace 'your_app_name' with the actual app name
from reports.models import (
    PathologyType
)
import os
from reports.dataloader_utils import load_model_data

SOURCE_DIR = settings.DATA_DIR_INTERVENTION

IMPORT_MODELS = [
    "InterventionType",
    "Intervention"
]

IMPORT_METADATA = {
    "InterventionType": {
        "dir": os.path.join(SOURCE_DIR, "type"),
        "model": InterventionType,
        "foreign_keys": [],
        "foreign_key_models": []
    },
    "Intervention": {
        "dir": os.path.join(SOURCE_DIR, "interventions"),
        "model": Intervention,
        "foreign_keys": ["pathology_types","intervention_types"],
        "foreign_key_models": [PathologyType, InterventionType]
    }
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