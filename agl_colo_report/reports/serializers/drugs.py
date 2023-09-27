from rest_framework import serializers
from .unit import UnitSerializer

from reports.models import (
    Drug
)

class DrugSerializer(serializers.ModelSerializer):
    preferred_unit = UnitSerializer()
    
    class Meta:
        model = Drug
        fields = [
            "id",
            "name",
            "name_de",
            "name_en",
            "description",
            "abbreviation",
            "preferred_unit",
        ]
