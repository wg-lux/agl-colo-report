from rest_framework import serializers
from reports.models import Examiner

class ExaminerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Examiner
        fields = '__all__'
