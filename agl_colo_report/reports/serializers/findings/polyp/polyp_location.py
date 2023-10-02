from rest_framework import serializers
from reports.models import (
    ColonPolypLocation,
    ColonAnatomy,
    OrganComponent,
)

class ColonPolypLocationSerializer(serializers.ModelSerializer):
    
    def validate_colon_anatomy(self, value):
        if value is None:
            try:
                default_colon_anatomy = ColonAnatomy.objects.get_by_natural_key('colon-normal')
                return default_colon_anatomy
            except ColonAnatomy.DoesNotExist:
                raise serializers.ValidationError('Default ColonAnatomy does not exist.')
        return value

    colon_anatomy = serializers.PrimaryKeyRelatedField(
        queryset=ColonAnatomy.objects.all(),
        required=False  # Make this field optional so validate_colon_anatomy can set the default
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
