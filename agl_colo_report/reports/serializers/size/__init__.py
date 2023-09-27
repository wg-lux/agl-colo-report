from rest_framework import serializers
from reports.models import (
    SizeCategory,
    SizeClassification,
    SizeMeasurement,
    Unit
)

class SizeMeasurementSerializer(serializers.ModelSerializer):
    unit = serializers.PrimaryKeyRelatedField(
        queryset=Unit.objects.all()
    )
    
    class Meta:
        model = SizeMeasurement
        fields = [
            "value",
            "unit",
        ]

class SizeCategorySerializer(serializers.ModelSerializer):
    classification = serializers.PrimaryKeyRelatedField(
        queryset=SizeClassification.objects.all()
    )

    unit = serializers.PrimaryKeyRelatedField(
        queryset=Unit.objects.all()
    )
    
    class Meta:
        model = SizeCategory
        fields = [
            "name",
            "name_de",
            "name_en",
            "size_min",
            "size_max",
            "unit",
            "classification"
        ]
