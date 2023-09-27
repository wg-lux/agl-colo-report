from rest_framework import serializers
from ..anatomy import OrganComponentSerializer
from reports.models import (
    ColonPolypLocation,
    ColonAnatomy,
    OrganComponent,
)

class ColonPolypLocationSerializer(serializers.ModelSerializer):
    # Initialize the queryset in the constructor (__init__ method)
    colon_anatomy = serializers.PrimaryKeyRelatedField(
        queryset=ColonAnatomy.objects.all(),
        default=ColonAnatomy.objects.get_by_natural_key(
            'colon-normal').id,
    )
    
    organ_component = serializers.PrimaryKeyRelatedField(
        queryset=OrganComponent.objects.all()
    )
    
    class Meta:
        model = ColonPolypLocation
        fields = [
            "colon_anatomy",
            "organ_component",
            "description",
        ]
