from rest_framework import serializers
from reports.models import ComplicationType

class ComplicationTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ComplicationType
        fields = '__all__'
