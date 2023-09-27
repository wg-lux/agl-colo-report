from rest_framework import serializers

from reports.models import Unit

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = [
            "id",
            "name",
            "name_de",
            "name_en",
            "description",
            "abbreviation"
        ]