from rest_framework import serializers
from reports.models import ExaminationTimeType

class ExaminationTimeTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExaminationTimeType
        fields = '__all__'
