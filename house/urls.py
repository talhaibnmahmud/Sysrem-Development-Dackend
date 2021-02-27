from django.urls import include, path
from rest_framework import routers

from .views import HouseViewSet, HouseDetailView

router = routers.DefaultRouter()
router.register('', HouseViewSet)

urlpatterns = [
    path('', include(router.urls), name='house-list'),
    path('house/<int:pk>/', HouseDetailView.as_view(), name='house-detail'),
]
