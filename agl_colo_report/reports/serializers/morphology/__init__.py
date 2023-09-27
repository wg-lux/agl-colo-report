from rest_framework import serializers

from reports.models import ColonPolypMorphology, PolypMorphology

class PolypMorphologySerializer(serializers.ModelSerializer):
        
        class Meta:
            model = PolypMorphology
            fields = "__all__"
