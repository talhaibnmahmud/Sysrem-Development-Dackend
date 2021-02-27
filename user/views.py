from django.contrib.auth import login
from django.contrib.auth.models import User
from knox.models import AuthToken
from knox.views import LoginView
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response

from user.models import Customer
from user.serializers import CustomerSerializer, UserSerializer
from user.signals import user_saved


# Create your views here.
# class RegisterAPI(generics.CreateAPIView):
#     permission_classes = (permissions.AllowAny, )
#     serializer_class = CustomerSerializer
#     queryset = Customer.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         # self.user_saved.send(User, user=user)
#         return Response({
#             'user': CustomerSerializer(user, context=self.get_serializer_context()).data,
#         })


class RegistrationAPI(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user_saved.send(
                sender=User,
                instance=user,
                created=True,
                data=request.data
            )

            return Response({
                'user': UserSerializer(user, context=self.get_serializer_context()).data,
                'token': AuthToken.objects.create(user)[1]
            }, status=201)

        return Response({
            'error': 'Could not create user. Please check your data again',
        }, status=409)


class LoginAPI(LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            return super(LoginAPI, self).post(request, format=None)
