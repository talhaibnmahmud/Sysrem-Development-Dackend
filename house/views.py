from django.core import serializers
from django.http import JsonResponse
from django.views.generic import DetailView
from rest_framework import permissions, viewsets

from house.models import House
from house.serializers import HouseSerializer


# Create your views here.
class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HouseDetailView(DetailView):

    def get(self, request, pk=0, **kwargs):
        house = House.objects.filter(id=pk)
        serializer = HouseSerializer(house, many=True)
        return JsonResponse(serializer.data, safe=False)
