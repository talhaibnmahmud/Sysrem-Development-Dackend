from django.urls import path
from knox import views as knox_views

from user.views import LoginAPI, RegistrationAPI


urlpatterns = [
    # path('auth/register/', RegisterAPI.as_view(), name='register'),
    path('auth/registration', RegistrationAPI.as_view(), name='registration'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('auth/logoutall/', knox_views.LogoutAllView.as_view(), name='logout-all'),
]
