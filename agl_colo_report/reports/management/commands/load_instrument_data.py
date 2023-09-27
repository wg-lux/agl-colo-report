from django.conf import settings
from django.core.management.base import BaseCommand
from reports.models import Instrument, InstrumentType  # Replace 'your_app_name' with the actual app name
import os
from reports.dataloader_utils import load_model_data

SOURCE_DIR = settings.DATA_DIR_INSTRUMENT

IMPORT_MODELS = [
    "InstrumentType",
    "Instrument"
]

IMPORT_METADATA = {
    "InstrumentType": {
        "dir": os.path.join(SOURCE_DIR, "type"),
        "model": InstrumentType,
        "foreign_keys": [],
        "foreign_key_models": []
    },
    "Instrument": {
        "dir": os.path.join(SOURCE_DIR, "instruments"),
        "model": Instrument,
        "foreign_keys": ["instrument_types"],
        "foreign_key_models": [InstrumentType]
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