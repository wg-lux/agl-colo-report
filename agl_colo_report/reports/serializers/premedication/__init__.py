from rest_framework import serializers
from reports.models import (
    DrugApplication,
    Premedication
)

from ..drugs import DrugSerializer
from ..unit import UnitSerializer

class DrugApplicationSerializer(serializers.ModelSerializer):
    drug = DrugSerializer()
    unit = UnitSerializer()
    
    class Meta:
        model = DrugApplication
        fields = [
            "name",
            "name_de",
            "name_en",
            "description",
            "abbreviation",
        ]

class PremedicationSerializer(serializers.ModelSerializer):
    drug_applications = DrugApplicationSerializer(many=True)
    blood_oxygen_monitoring = serializers.BooleanField()
    blood_pressure_monitoring = serializers.BooleanField()
    ecg_monitoring = serializers.BooleanField()

    class Meta:
        model = Premedication
        fields = [
            "drug_applications",
            "blood_oxygen_monitoring",
            "blood_pressure_monitoring",
            "ecg_monitoring",
        ]

