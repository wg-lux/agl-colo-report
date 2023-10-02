from rest_framework import serializers
from reports.models import (
    ALTERED_COLON_CHOICES,
    Report,
    Patient,
    OrganComponent,
    ColonAnatomy
)

from warnings import warn
class ReportSerializer(serializers.ModelSerializer):
    date_of_procedure = serializers.DateField(
        format="%Y-%m-%d",
        input_formats=["%Y-%m-%d", "iso-8601"],
        required=False,
    )
    
    # patient = serializers.PrimaryKeyRelatedField(
    #     queryset=Patient.objects.all()
    # )

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

    def __init__(self, *args, **kwargs):
        super(ReportSerializer, self).__init__(*args, **kwargs)

        # If the serializer is initialized with data, check for the 'colon_anatomy' field
        if 'data' in kwargs:
            data = kwargs['data']
            if 'colon_anatomy' in data:
                colon_anatomy_id = data['colon_anatomy']

                # Fetch the ColonAnatomy object and get available segments
                anatomy = ColonAnatomy.objects.get(id=colon_anatomy_id)
                available_segments = anatomy.available_segments.all()

                # Update the queryset for the 'deepest_insertion' field
                self.fields['deepest_insertion'].queryset = available_segments

    class Meta:
        model = Report
        fields = [
            # "patient",
            "id",
            "date_of_procedure",
            "altered_colon_anatomy",
            "colon_anatomy",
            "deepest_insertion",
        ]

    # def get_deepest_insertion(self, obj):
    #     if hasattr(obj, 'colon_anatomy'):
    #         if obj.colon_anatomy is not None:
    #             # get the available objects from the colon anatomy
    #             anatomy:ColonAnatomy = obj.colon_anatomy
    #             available_segments = anatomy.available_segments.all()
    #             return [obj.name for obj in available_segments]
    
    #     # Print a warning to the console
    #     warn(
    #         "The Report object with ID {} has no colon anatomy. Returning all OrganComponents".format(obj.id)
    #     )

    #     available_segments = OrganComponent.objects.all()

    #     return [obj.name for obj in available_segments]
        
