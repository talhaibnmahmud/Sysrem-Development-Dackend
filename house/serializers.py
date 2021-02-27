from rest_framework import serializers

from house.models import House


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        exclude = [
            'created',
            'last_modified',
        ]

