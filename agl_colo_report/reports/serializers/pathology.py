from rest_framework import serializers
from ..models import PathologyType

class PathologyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PathologyType
        fields = '__all__'