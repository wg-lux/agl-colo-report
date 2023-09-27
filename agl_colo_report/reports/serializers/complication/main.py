from rest_framework import serializers
from reports.models import Complication

class ComplicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Complication
        fields = '__all__'
