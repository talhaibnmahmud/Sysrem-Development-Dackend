from django.urls import path, include
from rest_framework import routers

from .views import RentalListView, AreaViewSet, DistrictViewSet

router = routers.DefaultRouter()
router.register('division', AreaViewSet)
router.register('district', DistrictViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all/', RentalListView.as_view(), name="Rental-List-View"),
]
