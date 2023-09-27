from rest_framework import serializers
from reports.models import ExaminationTime

class ExaminationTimeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExaminationTime
        fields = '__all__'
