# from .polyp import (
#     ColonPolypSerializer,
#     ColonPolypMorphologySerializer,
#     ColonPolypLocationSerializer,
#     ColonPolypSizeSerializer,
# )

from rest_framework import serializers
from reports.models import (
    ReportFindings
)

class ReportFindingsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReportFindings
        fields = '__all__'
