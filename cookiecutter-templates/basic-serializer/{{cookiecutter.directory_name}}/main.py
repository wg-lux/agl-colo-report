from rest_framework import serializers
from reports.models import {{cookiecutter.model_name}}

class {{cookiecutter.model_name}}Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = {{cookiecutter.model_name}}
        fields = '__all__'
