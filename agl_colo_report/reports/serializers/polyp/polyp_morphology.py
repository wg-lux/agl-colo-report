from rest_framework import serializers
from reports.models import (
    ColonPolypMorphology,
    MorphologyCategory,
)

class ColonPolypMorphologySerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(ColonPolypMorphologySerializer, self).__init__(*args, **kwargs)
        self.fields['categorical'].queryset = MorphologyCategory.objects.filter(
            classification__name="polyp-morphology-regular"
        ).distinct()

        self.fields['paris'].queryset = MorphologyCategory.objects.filter(
            classification__name="polyp-morphology-paris"
        ).distinct()

    categorical = serializers.PrimaryKeyRelatedField(
        queryset=MorphologyCategory.objects.none(),  # Empty initial queryset
    )

    paris = serializers.PrimaryKeyRelatedField(
        queryset=MorphologyCategory.objects.none(),
    )
    
    class Meta:
        model = ColonPolypMorphology
        fields = [
            "categorical",
            "paris",
            "description",
        ]