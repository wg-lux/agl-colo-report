from rest_framework import serializers
from  ...models import ColonPolyp, Report
from ..pathology import PathologyTypeSerializer
from .polyp_location import ColonPolypLocationSerializer
from .polyp_morphology import ColonPolypMorphologySerializer
from .polyp_size import ColonPolypSizeSerializer



class ColonPolypSerializer(serializers.ModelSerializer):
    # pathology_types = PathologyTypeSerializer(many=True)
    location = ColonPolypLocationSerializer()
    morphology = ColonPolypMorphologySerializer()
    size = ColonPolypSizeSerializer()

    ##### REMOVE LATER
    report = serializers.PrimaryKeyRelatedField(
        queryset=Report.objects.all(),
    )

    class Meta:
        model = ColonPolyp
        fields = [
            "report",
            "location",
            "size",
            "morphology",
            "description",
        ]
