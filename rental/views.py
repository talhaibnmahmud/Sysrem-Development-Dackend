from django.http import JsonResponse
from django.views.generic import ListView
from rest_framework import viewsets

from .models import Division, District
from .serializers import AreaSerializer, DistrictSerializer


# Create your views here.
class RentalListView(ListView):

    def get(self, request, **kwargs):
        items = {}

        divisions = Division.objects.all()
        districts = District.objects.all()

        for division in divisions:
            district = districts.filter(division=division)
            dis = [i.name for i in district]
            items[division.name] = dis

        return JsonResponse(items)


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = AreaSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
