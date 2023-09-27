from rest_framework import serializers

from reports.models import (
    Organ,
    OrganComponent,
    Anastomosis,
    AnastomosisType,
    ColonAnatomy
)

class OrganSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organ
        fields = '__all__'

class OrganComponentSerializer(serializers.ModelSerializer):    
    organ = Organ()
    
    class Meta:
        model = OrganComponent
        fields = '__all__'

class AnastomosisTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnastomosisType
        fields = '__all__'

class AnastomosisSerializer(serializers.ModelSerializer):
    component_1 = OrganComponentSerializer()
    component_2 = OrganComponentSerializer()
    connection_type_1 = AnastomosisTypeSerializer()
    connection_type_2 = AnastomosisTypeSerializer()

    class Meta:
        model = Anastomosis
        fields = '__all__'

class ColonAnatomySerializer(serializers.ModelSerializer):
    available_segments = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=OrganComponent.objects.all(),
    )
    available_anastomoses = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Anastomosis.objects.all(),
    )

    class Meta:
        model = ColonAnatomy
        fields = '__all__'