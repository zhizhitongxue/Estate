from django.shortcuts import render
from rest_framework.generics import GenericAPIView

from users.serializers import IDSerializer


# Create your views here.


class UserInquireView(GenericAPIView):
    serializer_class = IDSerializer

    def get(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
