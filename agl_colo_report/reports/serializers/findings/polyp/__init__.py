from rest_framework import serializers
from reports.models import ColonPolyp
from .polyp_location import ColonPolypLocationSerializer
from .polyp_morphology import ColonPolypMorphologySerializer
from .polyp_size import ColonPolypSizeSerializer



class ColonPolypSerializer(serializers.ModelSerializer):
    location = ColonPolypLocationSerializer()
    morphology = ColonPolypMorphologySerializer()
    size = ColonPolypSizeSerializer()

    class Meta:
        model = ColonPolyp
        fields = [
            "report",
            "location",
            "size",
            "morphology",
            "description",
        ]
