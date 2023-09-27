from rest_framework import serializers
from .polyp import ColonPolypSerializer
from .patient import PatientSerializer

from .anatomy import (
    OrganComponentSerializer,
    ColonAnatomySerializer
)
from .premedication import PremedicationSerializer
from reports.models import (
    ALTERED_COLON_CHOICES,
    Report,
    Patient,
    OrganComponent,
    ColonAnatomy
)

from warnings import warn
class ReportSerializer(serializers.ModelSerializer):
    # date field with datepicker in format YYYY-MM-DD, default is today
    date_of_procedure = serializers.DateField(
        format="%Y-%m-%d",
        input_formats=["%Y-%m-%d", "iso-8601"],
        required=False,
    )
    
    patient = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all()
    )

    deepest_insertion = deepest_insertion = serializers.PrimaryKeyRelatedField(
        queryset=OrganComponent.objects.all()
    )
    
    colon_anatomy = serializers.PrimaryKeyRelatedField(
        queryset=ColonAnatomy.objects.all()
    )

    altered_colon_anatomy = serializers.ChoiceField(
        choices=ALTERED_COLON_CHOICES,
        default="unknown",
    )

    class Meta:
        model = Report
        fields = [
            "patient",
            "date_of_procedure",
            "altered_colon_anatomy",
            "colon_anatomy",
            "deepest_insertion",
        ]

    def get_deepest_insertion(self, obj):
        # must be named get_<field_name> if used for fieldmethod
        # get deepest insertion 
        
        # check if attribute is available and is not None
        if hasattr(obj, 'colon_anatomy'):
            if obj.colon_anatomy is not None:
                # get the available objects from the colon anatomy
                anatomy:ColonAnatomy = obj.colon_anatomy
                available_segments = anatomy.available_segments.all()
                return [obj.name for obj in available_segments]
    
        # Print a warning to the console
        warn(
            "The Report object with ID {} has no colon anatomy. Returning all OrganComponents".format(obj.id)
        )

        available_segments = OrganComponent.objects.all()

        return [obj.name for obj in available_segments]
        
