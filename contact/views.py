from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from contact.serializers import ContactSerializer


# Create your views here.
class ContactView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            return Response({
                'contact': ContactSerializer(contact, context=self.get_serializer_context()).data,
            })

        return Response({
            'message': 'Please check out the Contact form again',
        }, status=400)
