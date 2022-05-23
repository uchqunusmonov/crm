from .serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.response import Response
from chat.models import *

class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    