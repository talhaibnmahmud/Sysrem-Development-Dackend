from rest_framework import serializers

from rental.models import Division, District


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ['id', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'division']
