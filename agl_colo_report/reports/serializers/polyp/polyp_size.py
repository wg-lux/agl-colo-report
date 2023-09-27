from rest_framework import serializers
from reports.models import (
    ColonPolypSize,
    SizeCategory,
)

from ..size import SizeMeasurementSerializer

class ColonPolypSizeSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(ColonPolypSizeSerializer, self).__init__(*args, **kwargs)
        self.fields["categorical"].queryset = SizeCategory.objects.filter(
            classification__name="polyp-size-classification-regular"
        ).distinct()
    
    
    categorical = serializers.PrimaryKeyRelatedField(
        queryset=SizeCategory.objects.all(),
    )
    measurement = SizeMeasurementSerializer()

    class Meta:
        model = ColonPolypSize
        fields = [
            "categorical",
            "measurement",
        ]
