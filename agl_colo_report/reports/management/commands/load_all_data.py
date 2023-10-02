from django.core.management import BaseCommand, call_command

class Command(BaseCommand):
    help = 'Run all data loading commands in the correct order'

    def add_arguments(self, parser):
        parser.add_argument(
            '--verbose',
            action='store_true',
            help='Display verbose output for all commands',
        )

    def handle(self, *args, **options):
        verbose = options['verbose']

        # Run the load_unit_data command
        self.stdout.write(self.style.SUCCESS("Running load_unit_data..."))
        call_command('load_unit_data', verbose=verbose)

        # Run the load_pathology_type_data command
        self.stdout.write(self.style.SUCCESS("Running load_pathology_type_data..."))
        call_command('load_pathology_type_data', verbose=verbose)

        # Run the load_size_data command
        self.stdout.write(self.style.SUCCESS("Running load_size_data..."))
        call_command('load_size_data', verbose=verbose)

        # Run the load_examination_data command
        self.stdout.write(self.style.SUCCESS("Running load_examination_data..."))
        call_command('load_examination_data', verbose=verbose)

        # run the load complication data command
        self.stdout.write(self.style.SUCCESS("Running load_complication_data..."))
        call_command('load_complication_data', verbose=verbose)

        # Run the load_indication_data command
        self.stdout.write(self.style.SUCCESS("Running load_indication_data..."))
        call_command('load_indication_data', verbose=verbose)

        # Run the load_instrument_data command
        self.stdout.write(self.style.SUCCESS("Running load_instrument_data..."))
        call_command('load_instrument_data', verbose=verbose)

        # run the load_drug_data command
        self.stdout.write(self.style.SUCCESS("Running load_drug_data..."))
        call_command('load_drug_data', verbose=verbose)
        
        # Run the load_organ_data command
        self.stdout.write(self.style.SUCCESS("Running load_organ_data..."))
        call_command('load_organ_data', verbose=verbose)

        # Run the load_anastomosis_data command
        self.stdout.write(self.style.SUCCESS("Running load_anastomosis_data..."))
        call_command('load_anastomosis_data', verbose=verbose)

        # Run the load_morphology_data command
        self.stdout.write(self.style.SUCCESS("Running load_morphology_data..."))
        call_command('load_morphology_data', verbose=verbose)

        # Run the load_colon_anatomy_data command
        self.stdout.write(self.style.SUCCESS("Running load_colon_anatomy_data..."))
        call_command('load_colon_anatomy_data', verbose=verbose)

        # Rund the load_information_source command
        self.stdout.write(self.style.SUCCESS("Running load_information_source..."))
        call_command('load_information_source', verbose=verbose)

        

        # Run the load_intervention_data command
        self.stdout.write(self.style.SUCCESS("Running load_intervention_data..."))
        call_command('load_intervention_data', verbose=verbose)

        self.stdout.write(self.style.SUCCESS("All data loading commands executed successfully."))
